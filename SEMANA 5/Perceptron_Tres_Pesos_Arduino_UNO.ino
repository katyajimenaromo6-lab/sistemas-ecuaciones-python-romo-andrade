/*
  PERCEPTRON CON TRES PESOS - ARDUINO UNO R3
  X0 = 1; X1 = pulsador D8; X2 = pulsador D7
  Y = LED D4. Pulsadores conectados a GND.
*/

// CAMBIAR UNICAMENTE ESTOS TRES PESOS:
float W0 = -0.3;
float W1 =  0.2;
float W2 =  0.2;

const int PIN_X1 = 8;
const int PIN_X2 = 7;
const int PIN_LED = 4;
const int X0 = 1;

int X1 = 0;
int X2 = 0;
int Y = 0;
float Z = 0;

void setup() {
  Serial.begin(9600);
  pinMode(PIN_X1, INPUT_PULLUP);
  pinMode(PIN_X2, INPUT_PULLUP);
  pinMode(PIN_LED, OUTPUT);
  digitalWrite(PIN_LED, LOW);

  Serial.println("PERCEPTRON - ARDUINO UNO");
  Serial.print("W0 = "); Serial.println(W0, 4);
  Serial.print("W1 = "); Serial.println(W1, 4);
  Serial.print("W2 = "); Serial.println(W2, 4);
  Serial.println("X1  X2  |  Z  |  Y");
}

void loop() {
  // INPUT_PULLUP: pulsador libre = 0; presionado = 1
  X1 = !digitalRead(PIN_X1);
  X2 = !digitalRead(PIN_X2);

  Z = W0 * X0 + W1 * X1 + W2 * X2;
  Y = (Z >= 0) ? 1 : 0;
  digitalWrite(PIN_LED, Y == 1 ? HIGH : LOW);

  static int anteriorX1 = -1;
  static int anteriorX2 = -1;
  static int anteriorY = -1;
  if (X1 != anteriorX1 || X2 != anteriorX2 || Y != anteriorY) {
    Serial.print(X1); Serial.print("   ");
    Serial.print(X2); Serial.print("   |  ");
    Serial.print(Z, 4); Serial.print("  |  ");
    Serial.println(Y);
    anteriorX1 = X1;
    anteriorX2 = X2;
    anteriorY = Y;
  }
  delay(30);
}