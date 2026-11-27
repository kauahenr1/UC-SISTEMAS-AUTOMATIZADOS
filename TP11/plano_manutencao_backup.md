# Diagnostico, Manutencao e Backup — Celula 11 (TP11)

## Diagnostico por camadas (ex.: M1 nao aciona)
1. **Preservar contexto:** anotar horario, modo (`AUTO`/`MANUAL`), etapa ativa, estado das entradas/saidas e alarmes antes de resetar.
2. **Conter risco:** manter condicao segura (`SAFE` e atuadores em repouso).
3. **Isolar camada:**
   - Bobina logica `M1=0`: conferir `SAFE`, `RUN`, `AUTO`, `STEP_T` e ausencia de `B1`.
   - Logica `=1` e saida fisica `=0`: conferir cartao de saida, LEDs de diagnostico e configuracao de endereco.
   - Saida `=1` e sem tensao no borne: conferir protecao/fusivel, bornes e continuidade de cabo.
   - Tensao presente e motor/contator parado: conferir bobina do contator, circuito de potencia e motor.
4. **Corrigir e verificar:** aplicar reparo pontual, repetir o teste e executar regressao.

## Plano de manutencao
| Conjunto | Falha tipica | Tipo de manutencao | Acompanhamento |
|---|---|---|---|
| Motor M1 / Esteira | Aquecimento, desgaste de rolamento, desalinhamento | Preventiva e preditiva | Corrente, vibracao/temperatura e inspecao visual |
| Atuador A1 | Perda de vedacao, atrito, queda de pressao | Preditiva e preventiva | Tempo de avanco/retorno e pressao de linha |
| Sensores B1, B2, B3 | Desalinhamento, sujeira, falha de cabo | Preventiva e teste de E/S | Coerencia com entradas CLP e contagem de timeouts |
| Valvulas Y1 e Y2 | Travamento ou falha de bobina | Preventiva e corretiva | Tempo de atuacao e verificacao eletrica |
| Rede / Broker / HMI | Queda de enlace ou atualizacao congelada | Monitoramento e corretiva | Timestamp, qualidade do dado e logs de evento |

## Backup e rollback (v1.0.0)
- **Versao base:** `v1.0.0` (2026-11-26)
- **Itens salvos:** `README.md`, `io_celula11.csv`, `testes_tp11.csv`, `mqtt_celula11.csv`, `controle_celula11.py`, `diagramas_celula11.drawio`, `plano_manutencao_backup.md`, `dossie_tp11.xlsx` e `evidencias/`.
- **Restauracao:** recuperar arquivos da versao `v1.0.0`, validar enderecos de E/S e executar `python controle_celula11.py` para conferir os testes `T01` a `T06`.
- **Rollback:** voltar para a versao anterior aprovada, retestar condicoes seguras (`E0_OK`, `G1_OK`) e documentar a reversao.
