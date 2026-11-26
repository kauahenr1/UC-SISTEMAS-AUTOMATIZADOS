"""Modelo local da TP10. Não abre sockets nem usa servidores industriais."""
import csv
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = 'fabrica/linha1/tanque101'

def matches(topic, topic_filter):
    if not topic or '+' in topic or '#' in topic or not topic_filter:
        raise ValueError('Tópico ou filtro inválido')
    levels = topic_filter.split('/')
    for i, level in enumerate(levels):
        if ('#' in level and (level != '#' or i != len(levels)-1)) or ('+' in level and level != '+'):
            raise ValueError('Curinga deve ocupar um nível; # deve ser final')
    if topic.startswith('$') and levels[0] in ('#', '+'):
        return False
    names = topic.split('/')
    for i, level in enumerate(levels):
        if level == '#':
            return True
        if i >= len(names) or (level != '+' and level != names[i]):
            return False
    return len(names) == len(levels)

class ModbusModel:
    def __init__(self):
        self.holding = {0:650,1:0x41B4,2:0x0000}
    def read_holding(self, offset, count):
        if count < 1 or count > 125:
            return {'exception':3}
        if any(a not in self.holding for a in range(offset, offset+count)):
            return {'exception':2}
        return [self.holding[a] for a in range(offset,offset+count)]

def consume(value, quality):
    return value if quality == 'Good' else None

class BrokerModel:
    """ACL e retenção em memória; QoS e TLS são decisões documentadas."""
    def __init__(self):
        self.retained = {}
        self.available = True
    def publish(self, identity, topic, payload, retain=False):
        if not self.available:
            return 'INDISPONIVEL'
        if identity != 'pub-t101' or not topic.startswith(BASE+'/'):
            return 'NEGADO'
        if retain:
            if topic != BASE+'/estado':
                return 'RETAIN_RECUSADO_PELO_CONTRATO'
            if payload == '':
                self.retained.pop(topic,None)
            else:
                self.retained[topic] = payload
        return 'ACEITO'
    def subscribe(self, identity, topic_filter):
        allowed = {'hmi':BASE+'/estado','historico':'fabrica/linha1/#','manutencao':BASE+'/alarme'}
        if not self.available:
            return 'INDISPONIVEL'
        if allowed.get(identity) != topic_filter:
            return 'NEGADO'
        return [(topic,value) for topic,value in self.retained.items() if matches(topic,topic_filter)]

def generate():
    evidence=ROOT/'evidencias'; evidence.mkdir(exist_ok=True)
    tests=[]
    def record(id_,stimulus,expected,actual):
        ok = expected == actual
        tests.append([id_,stimulus,str(expected),str(actual),'PASSOU' if ok else 'FALHOU','Modelo local Python; sem rede real'])
        assert ok, (id_,expected,actual)
    modbus=ModbusModel()
    record('T01','FC03; referência 40001; offset 0; escala 0,1 %',65.0,modbus.read_holding(0,1)[0]*.1)
    record('T02','FC03; offset 99 inexistente',{'exception':2},modbus.read_holding(99,1))
    record('T03','Consumidor recebe 92,0 com qualidade Bad',None,consume(92.0,'Bad'))
    messages=[BASE+'/temperatura','fabrica/linha2/tanque101/temperatura',BASE+'/nivel']
    record('T04','Filtro fabrica/linha1/+/temperatura aplicado a três tópicos',[BASE+'/temperatura'],[t for t in messages if matches(t,'fabrica/linha1/+/temperatura')])
    broker=BrokerModel()
    state={'source':'T-101/P101_RUN','ts':'2026-11-20T04:00:00Z','value':True,'unit':'1','quality':'Good'}
    broker.publish('pub-t101',BASE+'/estado',state,True)
    record('T05','Nova assinatura hmi depois de publicar estado retido',[(BASE+'/estado',state)],broker.subscribe('hmi',BASE+'/estado'))
    record('T06','Identidade hmi tenta publicar estado','NEGADO',broker.publish('hmi',BASE+'/estado',state))
    record('T07','Good permite consumo',22.5,consume(22.5,'Good'))
    words=modbus.read_holding(1,2)
    record('T08','TEMP_REAL em dois words ABCD',22.5,struct.unpack('>f',struct.pack('>HH',*words))[0])
    record('T09','Filtro # inclui o nível pai',True,matches('fabrica/linha1','fabrica/linha1/#'))
    record('T10','Filtro + exige um nível',False,matches('fabrica/linha1','fabrica/linha1/+'))
    record('T11','Curinga na raiz não recebe $SYS',False,matches('$SYS/broker/uptime','#'))
    record('T12','Filtro + casa nível vazio existente',True,matches('fabrica//estado','fabrica/+/estado'))
    broker.available=False
    record('T13','Broker indisponível','INDISPONIVEL',broker.publish('pub-t101',BASE+'/estado',state,True))
    broker=BrokerModel() # reinício sem persistência
    record('T14','Reinício sem persistência; nova assinatura',[],broker.subscribe('hmi',BASE+'/estado'))
    broker.publish('pub-t101',BASE+'/estado',state,True)
    record('T15','Republicação após reconectar',[(BASE+'/estado',state)],broker.subscribe('hmi',BASE+'/estado'))
    broker.publish('pub-t101',BASE+'/estado','',True)
    record('T16','Payload vazio com RETAIN remove estado',[],broker.subscribe('hmi',BASE+'/estado'))
    record('T17','Contrato recusa retenção de evento de alarme','RETAIN_RECUSADO_PELO_CONTRATO',broker.publish('pub-t101',BASE+'/alarme',{'event_id':'E1'},True))
    ids=['E1','E1','E2']; seen=set(); processed=[]
    for id_ in ids:
        if id_ not in seen: processed.append(id_); seen.add(id_)
    record('T18','Consumidor deduplica event_id repetido',['E1','E2'],processed)
    topics=[BASE+'/temperatura','fabrica/linha2/tanque101/temperatura','fabrica/linha1/motor03/estado','fabrica/linha1',BASE+'/estado',BASE+'/alarme',BASE+'/nivel','fabrica/linha1/tanque102/temperatura',BASE+'/temperatura/media','$SYS/broker/uptime']
    filters=['fabrica/linha1/+/temperatura','fabrica/linha1/#',BASE+'/alarme']
    expected=[[True,True,False],[False,False,False],[False,True,False],[False,True,False],[False,True,False],[False,True,True],[False,True,False],[True,True,False],[False,True,False],[False,False,False]]
    routes=[]
    for i,topic in enumerate(topics):
        for j,f in enumerate(filters):
            actual=matches(topic,f); assert actual == expected[i][j]
            routes.append([topic,f,'SIM' if expected[i][j] else 'NAO','SIM' if actual else 'NAO',
                           'Filtro de temperatura da linha 1; exatamente quatro níveis' if j==0 else '# inclui o pai e descendentes da linha 1' if j==1 else 'Somente o tópico exato de alarme do tanque 101'])
    def save_csv(path,heads,rows):
        with path.open('w',encoding='utf-8-sig',newline='') as f:
            w=csv.writer(f,lineterminator='\n'); w.writerow(heads); w.writerows(rows)
    save_csv(ROOT/'casos_teste.csv',['ID','Estímulo','Esperado','Obtido','Conclusão','Método'],tests)
    save_csv(evidence/'roteamento-calculado.csv',['Publicação','Filtro','Esperado manual','Obtido algoritmo','Justificativa'],routes)
    (evidence/'resultados.json').write_bytes(json.dumps({'tests':tests,'routes':routes},ensure_ascii=False,indent=2).encode('utf-8'))
    print(f'{len(tests)} testes e {len(routes)} pares tópico/filtro passaram no modelo local.')

if __name__ == '__main__':
    generate()
