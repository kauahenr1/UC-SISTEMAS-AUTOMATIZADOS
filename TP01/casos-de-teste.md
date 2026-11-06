# TP01 — Casos de teste e resultados esperados

**Natureza da verificação:** validação teórica dos modelos. Os cenários abaixo ainda não foram executados em equipamentos físicos ou em simulação funcional.

## Porta automática (obrigatório)

| Caso | Entrada / condição | Resposta esperada | Status |
|---|---|---|---|
| P1 | Presença detectada, sensores válidos | Abrir porta | Não executado |
| P2 | Passagem concluída, área livre | Fechar após espera | Não executado |
| P3 | Obstáculo durante fechamento | Parar e reabrir | Não executado |
| P4 | Sensor de barreira inválido | Impedir fechamento automático e alarmar | Não executado |
| P5 | Emergência acionada | Priorizar estado seguro especificado | Não executado |

## Reservatório (adicional 1)

| Caso | Entrada / condição | Resposta esperada | Status |
|---|---|---|---|
| R1 | Nível 25%, sensor válido | Ligar bomba | Não executado |
| R2 | Nível 55%, bomba já ligada | Manter bomba ligada | Não executado |
| R3 | Nível 80% | Desligar bomba | Não executado |
| R4 | Sensor inválido | Desligar bomba e alarmar | Não executado |
| R5 | Nível alto-alto | Desligar bomba e alarmar | Não executado |

## Iluminação (adicional 2 — quatro casos)

| Caso | Escuro | Presença | Horário habilitado | Modo | Resposta esperada | Status |
|---|---|---|---|---|---|---|
| I1 | Sim | Sim | Sim | Automático | Acender | Não executado |
| I2 | Não | Sim | Sim | Automático | Apagar | Não executado |
| I3 | Sim | Não | Sim | Automático | Apagar após temporização | Não executado |
| I4 | Sim | Sim | Não | Automático | Apagar | Não executado |

**Verificações adicionais:** modo manual deve respeitar o comando autorizado; falha de sensor deve gerar diagnóstico e estratégia de contingência definida.

## Ventilação (adicional 3)

| Caso | Condição | Resposta esperada | Status |
|---|---|---|---|
| V1 | Sala ocupada, temperatura acima do limite superior | Ligar ventilador | Não executado |
| V2 | Temperatura abaixo do limite inferior | Desligar ventilador | Não executado |
| V3 | Sensor de temperatura inválido | Emitir alerta; não usar leitura inválida | Não executado |
| V4 | Motor travado detectado | Desligar acionamento e alarmar | Não executado |

## Registro de execução

Após abrir os arquivos `.drawio`, revisar os fluxos e executar simulações ou verificações, substituir o status de cada caso por **Aprovado**, **Reprovado** ou **Não aplicável**, acrescentando observações e evidências reais. Não declarar testes aprovados sem execução.
