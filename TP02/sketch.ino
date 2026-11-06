#include <DHT.h>
#include <math.h>

const int PINO_BOTAO = 2;
const int PINO_LED = 8;
const int PINO_POT = A0;
const int PINO_DHT = 4;
DHT dht(PINO_DHT, DHT22);

void setup() {
  Serial.begin(9600);
  pinMode(PINO_BOTAO, INPUT_PULLUP);
  pinMode(PINO_LED, OUTPUT);
  digitalWrite(PINO_LED, LOW);
  dht.begin();
  Serial.println("Estacao de monitoramento - TP02");
}

void loop() {
  bool pressionado = digitalRead(PINO_BOTAO) == LOW;
  digitalWrite(PINO_LED, pressionado ? HIGH : LOW);
  int bruto = analogRead(PINO_POT);
  float temperatura = dht.readTemperature();

  const char *estado;
  if (isnan(temperatura)) {
    estado = "FALHA DE SENSOR";
  } else if (temperatura >= 40.0 || bruto >= 750) {
    estado = "ALARME";
  } else if (temperatura >= 30.0 || bruto >= 400) {
    estado = "ATENCAO";
  } else {
    estado = "NORMAL";
  }

  Serial.print("Botao: ");
  Serial.print(pressionado ? "PRESSIONADO" : "LIBERADO");
  Serial.print(" | LED: ");
  Serial.print(pressionado ? "ON" : "OFF");
  Serial.print(" | Pot: ");
  Serial.print(bruto);
  Serial.print(" | Temp: ");
  if (isnan(temperatura)) Serial.print("INVALIDA");
  else { Serial.print(temperatura, 1); Serial.print(" C"); }
  Serial.print(" | Estado: ");
  Serial.println(estado);
  delay(2000); // DHT22: intervalo de leitura >= 2 s
}
