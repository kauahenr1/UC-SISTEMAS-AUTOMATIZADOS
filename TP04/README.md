# TP04 - Sistemas Automatizados

## Implementação de lógica combinacional e programação Ladder

### Objetivo
Implementar e simular uma lógica de acionamento de motor utilizando portas lógicas e programação Ladder.

### Expressão lógica
M = S · G · ¬E

### Variáveis
- **S:** Entrada de acionamento.
- **G:** Entrada de habilitação.
- **E:** Entrada de emergência.
- **M:** Saída de acionamento do motor.

### Implementação
O circuito foi desenvolvido utilizando portas lógicas no CircuitVerse e posteriormente representado em linguagem Ladder no PLC Simulator Online.

Na implementação Ladder, foram utilizados dois contatos normalmente abertos (S e G), um contato normalmente fechado (E) e uma bobina de saída (M).

### Testes realizados
**Teste de acionamento:**
- S = 1
- G = 1
- E = 0
- M = 1

**Teste de emergência:**
- S = 1
- G = 1
- E = 1
- M = 0

Os dois testes apresentaram os resultados esperados.

### Simulação Ladder
[Visualizar projeto no PLC Simulator Online](https://app.plcsimulator.online/1VcgdJP2GWJ9Gf7onLUZ)

### Conclusão
A implementação demonstrou o funcionamento da lógica combinacional de acionamento e bloqueio do motor, com resultados compatíveis com a expressão lógica proposta.
