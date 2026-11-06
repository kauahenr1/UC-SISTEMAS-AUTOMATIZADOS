# TP02 — Processos, sensores e transdutores

## Objetivo
Construir e validar no Wokwi uma estação de monitoramento com Arduino Uno, entrada digital (botão), saída digital (LED), entrada analógica (potenciômetro) e sensor de temperatura DHT22. Atividade baseada no material da Semana 2, especialmente nas páginas 45–60.

## Arquivos
- `sketch.ino`: programa Arduino.
- `diagram.json`: componentes e conexões do circuito no Wokwi.
- `libraries.txt`: dependências para o simulador.
- `casos-de-teste.md`: roteiro de validação, ainda sem resultados experimentais.
- `evidencias/`: local reservado para capturas de tela produzidas durante a simulação.

## Ligações
| Componente | Ligação |
|---|---|
| Botão | D2 e GND, com `INPUT_PULLUP` |
| LED | D8 → resistor 220 Ω → ânodo do LED; cátodo → GND |
| Potenciômetro | VCC → 5 V; GND → GND; SIG → A0 |
| DHT22 | VCC → 5 V; GND → GND; SDA → D4 |

## Lógica de funcionamento
- Botão liberado: leitura HIGH e LED apagado; pressionado: LOW e LED aceso.
- Potenciômetro: 0–399 NORMAL; 400–749 ATENÇÃO; 750–1023 ALARME.
- Temperatura: abaixo de 30 °C NORMAL; de 30 °C até abaixo de 40 °C ATENÇÃO; 40 °C ou mais ALARME.
- Prioridade da decisão integrada: **FALHA DE SENSOR > ALARME > ATENÇÃO > NORMAL**. A falha do DHT22 é detectada por `isnan`.
- O botão controla o LED independentemente do estado geral. O Monitor Serial mostra o estado e os valores lidos.

## Como executar no Wokwi
1. Acesse https://wokwi.com/ e crie um projeto **Arduino Uno**.
2. Substitua o conteúdo de `sketch.ino` e `diagram.json` pelos arquivos deste repositório.
3. Inclua `libraries.txt` no projeto com as dependências listadas. Caso necessário, use o Library Manager para instalar a biblioteca DHT e sua dependência.
4. Inicie a simulação, abra o Monitor Serial, altere o potenciômetro e a temperatura do DHT22 e pressione o botão.
5. Preencha os resultados reais em `casos-de-teste.md` e salve capturas de tela em `evidencias/`.
6. Salve o projeto no Wokwi e, se disponível, adicione aqui seu link compartilhável.

## Relação com a instrumentação industrial
O botão representa um sensor discreto; o potenciômetro representa uma variável analógica; o DHT22 fornece temperatura digital; o LED representa um sinalizador; e o Arduino realiza o papel didático de controlador. A simulação não substitui a validação elétrica ou metrológica de equipamentos industriais.

## Situação
**Implementação proposta, aguardando execução e comprovação dos testes no Wokwi.** Não há alegação de testes já realizados.
