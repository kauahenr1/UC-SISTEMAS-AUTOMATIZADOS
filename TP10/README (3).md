# TP10 - Modbus, OPC UA e MQTT

**Aluno: Kauã Henrique · RA: 824132179**

Material de referência: versão de Denner Ferreira, utilizada em colaboração acadêmica.

## Entrega

Tanque T-101 com nível, temperatura e bomba P-101. O legado fornece dados Modbus; o gateway normaliza nós OPC UA e publica indicadores MQTT. HMI, histórico e manutenção consomem os dados conforme suas permissões. Esta é a simulação estruturada sem comunicação real pedida na P10.

- [mapa_modbus.xlsx](mapa_modbus.xlsx): abas Modbus, OPC_UA, MQTT e Testes.
- [tags_opcua.csv](tags_opcua.csv): cinco nós, tipos, unidades, origem, acesso, qualidade e timestamp.
- [mqtt.drawio](mqtt.drawio), [mqtt.pdf](mqtt.pdf) e [mqtt.png](mqtt.png): zonas, publicador, broker e três consumidores.
- [roteamento.xlsx](roteamento.xlsx): quatro cenários básicos, dez publicações × três filtros, fórmulas de comparação, QoS, riscos e fluxos autorizados.
- [casos_teste.csv](casos_teste.csv): seis casos obrigatórios e doze complementares, com estímulo, esperado, obtido e conclusão.
- [simulador.py](simulador.py): modelo executável com biblioteca padrão Python. Execute `python TP10/simulador.py` na raiz para reproduzir os resultados.
- [Resultados calculados](evidencias/resultados.json) e [matriz de roteamento](evidencias/roteamento-calculado.csv).

## Mapa e normalização

As referências são convenções humanas; a PDU usa offsets iniciados em zero dentro de cada área. Coils, entradas discretas, input registers e holding registers têm espaços separados. SP_NIVEL está em 40001, offset 0; 650 bruto equivale a 65,0 %. TEMP_REAL ocupa offsets 1 e 2 de holding, Float32 IEEE754 com ordem ABCD: words 0x41B4 e 0x0000 representam 22,5 °C. Esse mapa e a ordem de words são hipóteses explícitas deste projeto, a confirmar no manual de um equipamento real.

P101_CMD é solicitação; P101_RUN é retorno. Só o operador autorizado pode escrever comando e setpoint. AccessLevel do nó e permissão da identidade são verificações distintas. Nós com qualidade Bad não alimentam o valor atual da HMI. SourceTimestamp registra aquisição em UTC; dado acima de 5 s é tratado como antigo nesta proposta. O número de namespace 2 é convenção do modelo; em servidor real deve ser resolvido pela URI de namespace estável.

## Contrato MQTT

Raiz: `fabrica/linha1/tanque101`. Publicações `temperatura`, `nivel`, `estado` e `alarme`. Payload JSON contém `source`, `ts` ISO 8601 UTC, `value`, `unit` e `quality`. Alarmes acrescentam `event_id`. Exemplos em [payloads.json](payloads.json) usam dados sintéticos.

Telemetria usa QoS 0, sem RETAIN, pois nova amostra substitui a anterior. Estado atual usa QoS 1 e RETAIN. Alarmes são eventos, QoS 1 sem RETAIN; deduplicar event_id. RETAIN não comprova atualização: consumidor valida timestamp e qualidade. Broker sem persistência perde o estado no reinício, portanto o publisher republica após reconectar. Payload vazio com RETAIN remove o registro retido. O modelo não implementa o protocolo de transporte QoS, TLS ou persistência em disco.

HMI assina o tópico exato de estado; histórico assina `fabrica/linha1/#`; manutenção assina o tópico exato de alarme. O filtro `fabrica/linha1/+/temperatura` é testado para análise seletiva. `+` ocupa um nível e `#` final inclui o pai e descendentes; filtros que começam com curinga não recebem `$SYS`. Filtros distinguem maiúsculas e minúsculas. O modelo rejeita curingas em nomes de publicação.

## Segurança, falha e recuperação

Controle, Integração e Serviços são zonas distintas. Modbus legado fica acessível apenas pelo gateway autorizado; não possui proteção criptográfica neste modelo. OPC UA exige SignAndEncrypt, certificados confiáveis e perfis de leitura/escrita. Broker na Integração usa TLS 8883, identidades individuais e ACLs. Sem acesso MQTT direto a comandos do CLP. Não há senhas, tokens ou certificados privados nesta entrega.

Falha do broker interrompe mensagens aos serviços e marca lacuna no histórico; o controle local permanece independente. Reconexão exige republicação de estado e identificação de lacunas, sem inventar eventos ausentes. Falha do gateway torna suas tags BadCommunicationError, bloqueia comandos dependentes e exige nova leitura válida antes de Good. Os cinco cenários de QoS e a matriz de fluxos/riscos estão na planilha de roteamento.

O arquivo editável foi aberto no diagrams.net; veja a [captura do editor](evidencias/editor-verificado.jpg).

## Evidências e limites

18 testes e 30 pares de roteamento foram executados no modelo local. Fórmulas da planilha comparam esperado e obtido e calculam escala e offset. Este resultado não comprova interoperabilidade, latência, segurança configurada ou desempenho em rede real. Não foram usados broker, CLP ou servidor OPC UA reais.

Fonte: [Calvetti, TP10, páginas 57–69](https://drive.google.com/file/d/1MEfGhZoLmCEYMlEOUefO5vFC_0gPofW-/view). Curingas e retenção conferidos na [especificação MQTT 3.1.1, OASIS](https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html), seções 4.7 e 3.3.1. Os endereços, contratos e permissões foram definidos para este exercício.
