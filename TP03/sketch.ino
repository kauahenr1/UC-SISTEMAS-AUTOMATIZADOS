#include <DHT.h>
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
const int BTN = 2, POT = A0, LED = 8;
bool falhaSimulada = false;
unsigned long amostra = 0;
void setup() {
  pinMode(BTN, INPUT_PULLUP);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  dht.begin();
  Serial.println("amostra,botao,bruto,percentual,temp_sim_C,corrente_mA,tensao_V,estado,dht_C");
  Serial.println("# Digite F para simular falha de leitura; R para restaurar");
}
void loop() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == 'F' || c == 'f') falhaSimulada = true;
    if (c == 'R' || c == 'r') falhaSimulada = false;
  }
  bool pressionado = digitalRead(BTN) == LOW;
  int bruto = falhaSimulada ? -1 : analogRead(POT);
  float percentual = 100.0f * bruto / 1023.0f;
  float temperatura = percentual; // faixa de engenharia 0 a 100 C
  float corrente = 4.0f + 16.0f * percentual / 100.0f;
  float tensao = 10.0f * percentual / 100.0f;
  const char* estado;
  if (bruto < 0 || bruto > 1023) estado = "FALHA";
  else if (percentual >= 85.0f) estado = "PERIGO";
  else if (percentual >= 70.0f) estado = "ATENCAO";
  else estado = "NORMAL";
  digitalWrite(LED, pressionado ? HIGH : LOW);
  float tempDHT = dht.readTemperature();
  Serial.print(++amostra); Serial.print(',');
  Serial.print(pressionado ? 1 : 0); Serial.print(',');
  Serial.print(bruto); Serial.print(',');
  Serial.print(percentual, 2); Serial.print(',');
  Serial.print(temperatura, 2); Serial.print(',');
  Serial.print(corrente, 2); Serial.print(',');
  Serial.print(tensao, 2); Serial.print(',');
  Serial.print(estado); Serial.print(',');
  if (isnan(tempDHT)) Serial.println("NA"); else Serial.println(tempDHT, 1);
  delay(500);
}
