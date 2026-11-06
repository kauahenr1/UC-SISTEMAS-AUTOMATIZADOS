# TP01 — Fundamentos dos Sistemas Automatizados

**UC:** Sistemas Automatizados  
**Atividade:** TP01 — Semana 1  
**Professor:** Calvetti

## Objetivo

Representar sistemas automatizados por meio de diagramas funcionais, identificando a fronteira de cada sistema, entradas, processamento, saídas, realimentação, perturbações, falhas e respostas seguras.

> **Nota:** os modelos e testes são propostas conceituais para estudo. Não representam validação física, implementação industrial ou certificação de segurança.

## Arquivos

| Exercício | Arquivo editável | Visualização |
|---|---|---|
| Obrigatório — porta automática | [porta-automatica.drawio](porta-automatica.drawio) | [PNG](porta-automatica.png) |
| Adicional 1 — reservatório | [reservatorio.drawio](reservatorio.drawio) | [PNG](reservatorio.png) |
| Adicional 2 — iluminação | [iluminacao.drawio](iluminacao.drawio) | [PNG](iluminacao.png) |
| Adicional 3 — ventilação (proposta própria) | [proposta-propria.drawio](proposta-propria.drawio) | [PNG](proposta-propria.png) |

Os arquivos `.drawio` podem ser abertos e modificados em https://app.diagrams.net/.

## 1. Porta automática — exercício obrigatório

**Objetivo:** permitir acesso ao edifício sem fechar sobre pessoas.  
**Fronteira:** sensores, controlador, acionamento e folhas da porta; pessoas e obstáculos pertencem ao ambiente externo.  
**Classificação:** automático; controle sequencial com realimentação de posição e de detecção de obstáculos.  
**Entradas:** presença, barreira de segurança, posição da porta e comando de emergência.  
**Processamento:** verificar sinais válidos, comandar abertura, manter aberta durante passagem e fechar após intervalo com área livre.  
**Saídas:** comando do motor, posição da porta e sinalização de falha.  
**Perturbação:** pessoa ou objeto na passagem.  
**Falha:** sensor de segurança inválido.  
**Comportamento seguro proposto:** inibir fechamento, parar/reabrir quando aplicável e sinalizar necessidade de intervenção. A estratégia real depende de análise de risco e requisitos do equipamento.

## 2. Reservatório — adicional 1

**Objetivo:** manter o nível entre 30% e 80%.  
**Fronteira:** sensor, controlador, bomba e reservatório; o consumo é perturbação externa.  
**Classificação:** automático, malha fechada e controle liga/desliga com histerese.  
**Entradas:** nível medido e limites de controle (30% / 80%).  
**Processamento:** ligar bomba abaixo de 30%, manter estado intermediário e desligar ao atingir 80%.  
**Saídas:** comando da bomba e indicação de alarme.  
**Realimentação:** nível do reservatório retorna ao sensor.  
**Falhas:** sensor inválido e nível alto-alto.  
**Resposta segura proposta:** desligar a bomba e emitir alarme; proteção contra operação a seco requer monitoramento adicional da fonte de sucção.

## 3. Iluminação automática — adicional 2

**Objetivo:** reduzir gasto energético sem comprometer a iluminação necessária.  
**Fronteira:** sensores, relógio, controlador, relés e luminárias.  
**Classificação:** automático, programável por horários; lógica booleana.  
**Entradas:** baixa luminosidade (E), presença (P), horário habilitado (H) e modo manual (M).  
**Processamento:** no modo automático, `LIGAR = E ∧ P ∧ H`; no modo manual, o comando do operador prevalece para iluminação comum.  
**Saídas:** luminárias ligadas/desligadas e alerta de falha.  
**Realimentação:** luminosidade do ambiente pode ser medida novamente, observando-se que a medição deve evitar interferência direta da própria luminária.  
**Falha:** sensor de presença ou luminosidade inválido.  
**Resposta segura proposta:** gerar alerta e aplicar estratégia de contingência definida para o local; iluminação de emergência deve ser independente.

## 4. Proposta própria — ventilação automática de sala

**Objetivo e usuário:** manter conforto térmico em uma sala utilizada por estudantes ou trabalhadores.  
**Fronteira:** sensores, controlador e ventilador; calor externo e ocupantes são influências do ambiente.  
**Grau e tipo:** automático e programável (limites configuráveis), com realimentação de temperatura.  
**Entradas:** temperatura e presença.  
**Processamento:** acionar ventilação quando a sala estiver ocupada e a temperatura superar o limite configurado; desligar abaixo de limite inferior para evitar ciclos rápidos.  
**Saídas:** ventilador e indicação de estado.  
**Perturbações:** variação de temperatura externa e número de pessoas.  
**Riscos:** falha de motor, sinal de temperatura inválido e sobreaquecimento do equipamento.  
**Estado seguro proposto:** desligar em falha crítica do motor e emitir alerta.  
**Melhoria possível:** acrescentar diagnóstico de corrente/rotação do motor para confirmar a execução dos comandos e detectar travamentos.

## Análise resumida de falhas

| Situação | Consequência possível | Detecção | Resposta proposta |
|---|---|---|---|
| Sensor da porta inválido | Fechamento perigoso | Sinal ausente ou incoerente | Inibir fechamento e alarmar |
| Obstáculo na porta | Colisão | Barreira de segurança | Parar e reabrir |
| Nível alto-alto | Transbordamento | Sensor de limite independente | Desligar bomba e alarmar |
| Sensor de iluminação inválido | Luz acesa/apagada indevidamente | Diagnóstico de sinal | Alerta e contingência |
| Motor de ventilação travado | Aquecimento ou ausência de fluxo | Monitoramento de corrente/rotação (melhoria) | Desligar e alarmar |
| Perda de energia | Parada inesperada | Ausência de alimentação | Estado mecânico seguro conforme projeto |

## Casos de teste

Consulte [casos-de-teste.md](casos-de-teste.md). Os resultados registrados são **esperados em simulação conceitual**, não observações de testes reais.

## Referência de estudo

Material de aula: **TP01 — Fundamentos dos Sistemas Automatizados**, Semana 1, Prof. Calvetti, 2026. Conteúdo elaborado como modelagem original baseada nos requisitos dos exercícios, sem reprodução dos slides.
