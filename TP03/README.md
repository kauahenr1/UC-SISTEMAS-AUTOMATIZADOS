# TP03 — Sinais Analógicos e Digitais

## Objetivo
Adquirir sinais digitais e analógicos no Wokwi, escalonar a leitura ADC para percentual e temperatura de 0–100 °C, simular 4–20 mA e 0–10 V, classificar estados e documentar testes e tendência.

## Arquivos
- `diagram.json`: circuito Wokwi com Arduino Uno, botão D2, potenciômetro A0, DHT22 D4 e LED D8 com resistor.
- `sketch.ino`: leitura e impressão serial CSV a 9600 bit/s.
- `libraries.txt`: dependências do DHT22.
- `tabela_es.csv`: classificação de entradas, saídas e variáveis internas.
- `casos_de_teste.csv`: testes previstos; preencher resultados observados.
- `planilha_tp03.xlsx`: modelo com fórmulas e gráfico; substituir amostras de demonstração pelas reais.
- `evidencias/`: capturas a inserir após a execução.

## Equações
- Percentual = 100 × bruto / 1023
- Temperatura simulada (°C) = percentual
- Corrente (mA) = 4 + 16 × percentual / 100
- Tensão (V) = 10 × percentual / 100

## Estados
- FALHA: bruto inválido (<0 ou >1023)
- NORMAL: 0% até menos de 70%
- ATENÇÃO: 70% até menos de 85%
- PERIGO: 85% até 100%

O ADC real do Arduino Uno retorna apenas 0–1023. Para exercitar o tratamento de FALHA, o código aceita `F` pelo Monitor Serial para injetar leitura inválida (-1) e `R` para restaurar.

## Procedimento
1. Abrir um projeto Arduino Uno no Wokwi, colar `diagram.json`, `sketch.ino` e instalar as bibliotecas.
2. Iniciar a simulação e abrir Monitor Serial a 9600 baud.
3. Variar o potenciômetro entre mínimo, meio, máximo e limites de 70% e 85%; pressionar e liberar o botão.
4. Registrar pelo menos 10 leituras reais e substituir as amostras ilustrativas na planilha.
5. Conferir fórmulas, gráfico de tendência, 4–20 mA e 0–10 V, e preencher os casos de teste com observado/situação.
6. Registrar prints e links públicos abaixo.

## Links e evidências (preencher após simulação)
- Projeto público Wokwi: https://wokwi.com/projects/479961293259119617
- Planilha on-line com fórmulas: PENDENTE
- Prints do circuito, serial, testes e gráfico: PENDENTE

## Conclusão
PENDENTE — registrar resultados reais e comentar tendência, limites e eventuais divergências após os testes.

> As amostras pré-preenchidas na planilha são apenas exemplos calculados, não medições efetuadas.
