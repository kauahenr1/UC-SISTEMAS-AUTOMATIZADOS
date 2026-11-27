# TP11 / P11 — Comissionamento, Testes e Manutencao de Celula Automatizada

Dossie tecnico da celula didatica de separacao e transferencia (USJT — Sistemas Automatizados, Semana 11).
Contem mapeamento de E/S, modelo GRAFCET, simulacao em Ladder/logica de estados, integracao HMI/MQTT, casos de teste T01-T06, diagnostico de falhas e plano de manutencao/backup.

## Arquivos da entrega
- `README.md`: escopo, premissas de operacao, limites da simulacao e guia rapido.
- `io_celula11.csv`: tabela de entradas/saidas, memorias internas e condicao segura.
- `testes_tp11.csv`: casos de teste T01 a T06 com pre-condicoes, estimulos, esperados, obtidos e evidencias.
- `mqtt_celula11.csv`: topicos MQTT, payloads, QoS, retencao e fronteira de autoridade.
- `controle_celula11.py`: simulador da logica de controle (SAFE, RUN, etapas, timeouts, modo manual/automatico e falhas).
- `diagramas_celula11.drawio`: diagrama editavel no diagrams.net com GRAFCET e topologia HMI/Rede/MQTT.
- `plano_manutencao_backup.md`: arvore de diagnostico, plano de manutencao preventiva/preditiva/corretiva e manifesto de backup/rollback.
- `dossie_tp11.xlsx`: planilha de acompanhamento com abas Requisitos, IO, Estados, Testes e MQTT.
- `evidencias/execucao_t01_t06.json`: log JSON da execucao automatizada dos testes.
- `evidencias/fluxo_mensagens.csv`: mapeamento de eventos da celula para topicos e destinos.

## Premissas e limites
- Modelo academico e simulado: nao certifica seguranca de maquina real nem substitui normas ou procedimentos de campo.
- `SAFE = E0_OK AND G1_OK` (sem falha ativa) bloqueia movimentos e derruba o selo de `RUN` de forma prioritaria.
- `Y1` e `Y2` possuem bloqueio mutuo para evitar acionamento simultaneo.
- Falha na rede/broker nao aciona atuadores nem compromete o intertravamento local.
