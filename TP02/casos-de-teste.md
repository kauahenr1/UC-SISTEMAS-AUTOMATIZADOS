# TP02 — Casos de teste

**Status:** testes planejados, ainda não executados. Preencher as colunas de resultado e evidência após simular no Wokwi.

| ID | Potenciômetro (aprox.) | Temperatura | Botão | Estado esperado | LED esperado | Resultado observado | Evidência |
|---|---:|---|---|---|---|---|---|
| T1 | 200 | 25 °C | Liberado | NORMAL | Apagado | Pendente | — |
| T2 | 500 | 25 °C | Liberado | ATENÇÃO | Apagado | Pendente | — |
| T3 | 800 | 25 °C | Liberado | ALARME | Apagado | Pendente | — |
| T4 | 200 | 35 °C | Liberado | ATENÇÃO | Apagado | Pendente | — |
| T5 | 200 | 45 °C | Liberado | ALARME | Apagado | Pendente | — |
| T6 | 200 | 25 °C | Pressionado | NORMAL | Aceso | Pendente | — |
| T7 | 200 | Leitura inválida | Liberado | FALHA DE SENSOR | Apagado | Pendente | — |
| L1 | 399 | 25 °C | Liberado | NORMAL | Apagado | Pendente | — |
| L2 | 400 | 25 °C | Liberado | ATENÇÃO | Apagado | Pendente | — |
| L3 | 749 | 25 °C | Liberado | ATENÇÃO | Apagado | Pendente | — |
| L4 | 750 | 25 °C | Liberado | ALARME | Apagado | Pendente | — |
| L5 | 200 | 30 °C | Liberado | ATENÇÃO | Apagado | Pendente | — |
| L6 | 200 | 40 °C | Liberado | ALARME | Apagado | Pendente | — |

**Observação:** os valores do potenciômetro são leituras do ADC (0–1023), não posições físicas exatas. Para T7, simule uma falha de leitura do DHT22 e verifique o resultado. Não marque como aprovado sem observar a saída no Monitor Serial.
