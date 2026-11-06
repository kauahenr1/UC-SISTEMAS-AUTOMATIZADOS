# TP06 — CLP e linguagem Ladder

## Exercício obrigatório — Partida de motor com selo

Atividade da Semana 6 da UC Sistemas Automatizados (Prof. Calvetti, 2026.2).

**Escopo:** somente o exercício obrigatório descrito nas páginas 9 e 10 do gabarito.

## Objetivo

Implementar e testar, no PLC Simulator Online, o comando de um motor elétrico com partida momentânea, retenção por selo, parada prioritária e bloqueio por emergência.

## Programa Ladder

**[Acessar o programa no PLC Simulator Online](https://app.plcsimulator.online/Ei00P5ELFGlTc7ah6zM5)**

O programa foi montado e executado no simulador, utilizando contatos em série e um ramo paralelo para realizar a retenção do motor.

## Tags e convenções

| Tag | Tipo | Significado | Convenção |
|---|---|---|---|
| `START` | Entrada | Botão de partida | `True` enquanto pressionado |
| `STOP_OK` | Entrada | Condição normal de parada | `True` liberado; `False` para parar |
| `EMG_OK` | Entrada | Emergência liberada | `True` normal; `False` em emergência |
| `MOTOR` | Saída | Comando do motor | `True` ligado; `False` desligado |

## Equação lógica

`MOTOR_proximo = EMG_OK AND STOP_OK AND (START OR MOTOR_atual)`

## Funcionamento do circuito

1. Os contatos `EMG_OK` e `STOP_OK` são conectados em série.
2. O contato `START` é conectado em paralelo com um contato auxiliar `MOTOR`.
3. A bobina `MOTOR` é posicionada na saída do circuito.
4. Ao pressionar START, o motor liga.
5. Ao soltar START, o contato auxiliar mantém o motor ligado por meio do selo.
6. Ao acionar STOP ou a emergência, o motor desliga e o selo é desfeito.

```text
|----[ EMG_OK ]----[ STOP_OK ]----+----[ START ]----+----( MOTOR )----|
|                                |                 |
|                                +----[ MOTOR ]----+
```

**Observação:** `[ ]` representa um contato lógico que conduz quando a variável está em `True`.

## Testes executados

Foram realizados cinco testes no PLC Simulator Online, com os seguintes resultados:

| Teste | Descrição | Resultado observado | Situação |
|---|---|---|---|
| T01 | Partida do motor | MOTOR = True | APROVADO |
| T02 | Retenção após soltar START | MOTOR = True | APROVADO |
| T03 | Parada pelo STOP | MOTOR = False | APROVADO |
| T04 | Parada pela emergência | MOTOR = False | APROVADO |
| T05 | Bloqueio de partida com emergência ativa | MOTOR = False | APROVADO |

**Resultado geral: 5 de 5 testes aprovados.**

Os resultados detalhados estão disponíveis no arquivo [casos_teste.csv](casos_teste.csv).

## Evidências dos testes

As capturas de tela foram registradas durante a execução no simulador.

- [T01 — Partida do motor](capturas/T01_partida.png)
- [T02 — Retenção por selo](capturas/T02_selo.png)
- [T03 — Parada pelo STOP](capturas/T03_parada.png)
- [T04 — Estado anterior à emergência](capturas/T04_pre_emergencia.png)
- [T04 — Parada pela emergência](capturas/T04_emergencia.png)
- [T05 — Bloqueio de partida](capturas/T05_bloqueio_partida.png)

As imagens demonstram os estados das variáveis e o comportamento do circuito Ladder durante os testes.

## Arquivos da atividade

- `README.md` — documentação do exercício.
- `GUIA_MONTAGEM.md` — orientações de montagem do circuito.
- `casos_teste.csv` — resultados dos cinco testes.
- `capturas/` — evidências visuais dos testes.

## Limitações

A atividade representa uma simulação acadêmica da lógica de comando. Não demonstra o funcionamento físico de um motor elétrico nem certifica funções de segurança industrial.

Não foram incluídos os exercícios adicionais de RUN/READY, proteção por sobrecarga ou reversão de motor.

## Referência

USJT — UC Sistemas Automatizados, Semana 6, Prof. Calvetti, 2026.2.
