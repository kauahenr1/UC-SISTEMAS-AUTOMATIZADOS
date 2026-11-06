# TP03 — Sinais Analógicos e Digitais

## Objetivo

Implementar e simular um sistema de aquisição de sinais analógicos e digitais utilizando Arduino Uno, com leitura de sensores, conversão de valores e classificação dos estados de operação.

## Plataforma utilizada

- Wokwi — Simulador de Arduino
- Arduino Uno
- Linguagem C/C++
- GitHub — Documentação e armazenamento dos arquivos

## Componentes utilizados

- Arduino Uno
- Potenciômetro
- Botão (Pushbutton)
- LED vermelho
- Resistor de 220 Ω
- Sensor DHT22

## Entradas e saídas

| Componente | Pino | Função |
|---|---|---|
| Potenciômetro | A0 | Entrada analógica |
| Botão | D2 | Entrada digital |
| Sensor DHT22 | D4 | Leitura de temperatura |
| LED | D8 | Saída digital |

## Conversão dos sinais

O valor analógico do potenciômetro varia de 0 a 1023.

**Percentual:**

Percentual = (Leitura / 1023) × 100

**Temperatura simulada:**

Temperatura = Percentual × 1 °C

**Corrente simulada (4–20 mA):**

Corrente = 4 + (Percentual / 100) × 16

**Tensão simulada (0–10 V):**

Tensão = (Percentual / 100) × 10

## Estados de operação

| Estado | Condição |
|---|---|
| NORMAL | Percentual abaixo de 70% |
| ATENÇÃO | Percentual de 70% até abaixo de 85% |
| PERIGO | Percentual igual ou superior a 85% |
| FALHA | Leitura inválida simulada |

A condição de falha pode ser simulada enviando `F` pelo Monitor Serial e restaurada enviando `R`.

## Simulação no Wokwi

[**Acessar projeto TP03 — Sinais Analógicos e Digitais**](https://wokwi.com/projects/479961293259119617)

## Arquivos da atividade

- `sketch.ino` — Programação do Arduino.
- `diagram.json` — Circuito e conexões.
- `libraries.txt` — Bibliotecas utilizadas.
- `tabela_es.csv` — Classificação das entradas e saídas.
- `planilha_tp03.xlsx` — Amostras, cálculos e gráfico.
- `casos_de_teste.csv` — Planejamento e registro dos testes.
- `evidencias/` — Capturas de tela da simulação.

## Resultados e conclusão

Esta seção será preenchida após a execução dos testes, coleta das amostras e validação dos resultados obtidos no simulador.
