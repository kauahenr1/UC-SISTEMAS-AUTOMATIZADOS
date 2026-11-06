# TP06 — CLP e linguagem Ladder

## Exercício obrigatório — Partida de motor com selo

Atividade da Semana 6 da UC Sistemas Automatizados (Prof. Calvetti, 2026.2). Escopo: **somente o exercício obrigatório** descrito nas páginas 9 e 10 do gabarito.

## Objetivo

Implementar e testar, no [PLC Simulator Online](https://plcsimulator.online), o comando de um motor com partida momentânea, retenção (selo), parada prioritária e bloqueio por emergência.

## Tags e convenções

| Tag | Tipo | Significado | Convenção |
| --- | --- | --- | --- |
| `START` | Entrada | Botão de partida | `1` enquanto pressionado |
| `STOP_OK` | Entrada | Condição de parada saudável | `1` em condição normal; `0` para parar |
| `EMG_OK` | Entrada | Emergência liberada | `1` em condição normal; `0` em emergência |
| `MOTOR` | Saída | Comando do motor | `1` comandado; `0` desligado |

## Equação lógica

`MOTOR_proximo = EMG_OK AND STOP_OK AND (START OR MOTOR_atual)`

## Montagem do rung

1. Insira contatos `EMG_OK` e `STOP_OK` em série, **antes** da ramificação.
2. Após esses permissivos, faça dois ramos paralelos: `START` (superior) e `MOTOR` (inferior, selo).
3. Reúna os ramos e conecte à bobina `MOTOR`.
4. A partida exige ambos os permissivos em `1`; soltar `START` mantém o motor ligado pelo contato de selo. Qualquer permissivo em `0` desliga o motor e desfaz o selo.

```text
|----[ EMG_OK ]----[ STOP_OK ]----+----[ START ]----+----( MOTOR )----|
|                                |                 |
|                                +----[ MOTOR ]----+
```

**Observação:** `[ ]` representa contato lógico que conduz quando a tag vale `1`; não confundir com a característica física do botão.

## Testes obrigatórios

Os cinco casos T01–T05 estão em [`casos_teste.csv`](casos_teste.csv). As colunas `Obtido` e `Situacao` estão vazias até que os testes sejam realmente executados no simulador. Cada teste exige preparar o estado inicial indicado.

## Evidências a completar

- Link compartilhado do programa: **PENDENTE**.
- Arquivo exportado do simulador, se disponível: **PENDENTE**.
- Capturas dos estados de partida, selo, parada e emergência: **PENDENTES**.
- Resultados observados T01–T05: **PENDENTES**.

## Limitações

Esta é uma simulação acadêmica da lógica de comando. Não demonstra rotação física do motor nem certifica função de segurança. O exemplo não inclui os exercícios adicionais `OL_OK`, `RUN`, `READY` ou reversão.

## Referência

USJT, UC Sistemas Automatizados, Semana 6 — *CLP e linguagem Ladder: Gabarito detalhado de TP06*, Prof. Calvetti, 2026.2, páginas 9, 10 e 15.
