/* Perceptron simple entrenado EN ARDUINO UNO R3.
   Dataset adjunto: 102 registros. Monitor Serie: 9600 baudios.
   IMC normalizado /10; glucosa normalizada /100.
   Aprendizaje secuencial, tasa 0.1, pesos iniciales 0.
   NOTA: ejercicio academico, no herramienta de diagnostico medico.
*/
struct Registro {float imc; float glucosa; byte diagnostico;};
const Registro datos[] = {
  {22.49f, 95.12f, 0},
  {24.14f, 88.34f, 0},
  {23.72f, 92.45f, 0},
  {21.87f, 85.67f, 0},
  {22.91f, 97.56f, 0},
  {23.45f, 89.23f, 0},
  {24.67f, 93.78f, 0},
  {22.34f, 91.56f, 0},
  {23.89f, 87.45f, 0},
  {24.56f, 90.12f, 0},
  {22.78f, 94.67f, 0},
  {23.12f, 86.34f, 0},
  {24.23f, 92.89f, 0},
  {23.56f, 88.12f, 0},
  {22.91f, 95.34f, 0},
  {23.67f, 90.78f, 0},
  {24.12f, 89.45f, 0},
  {23.34f, 93.12f, 0},
  {22.56f, 87.89f, 0},
  {23.78f, 91.23f, 0},
  {24.45f, 88.67f, 0},
  {23.89f, 92.34f, 0},
  {22.67f, 90.12f, 0},
  {23.45f, 94.56f, 0},
  {24.23f, 89.78f, 0},
  {23.12f, 87.45f, 0},
  {22.89f, 93.67f, 0},
  {23.56f, 88.12f, 0},
  {24.34f, 91.89f, 0},
  {23.78f, 90.45f, 0},
  {22.45f, 92.12f, 0},
  {23.67f, 89.34f, 0},
  {24.12f, 93.78f, 0},
  {23.89f, 88.56f, 0},
  {22.78f, 91.23f, 0},
  {23.45f, 90.67f, 0},
  {24.23f, 92.34f, 0},
  {23.12f, 89.78f, 0},
  {22.67f, 94.12f, 0},
  {23.56f, 88.45f, 0},
  {24.34f, 91.67f, 0},
  {23.78f, 90.12f, 0},
  {22.45f, 93.56f, 0},
  {23.67f, 89.89f, 0},
  {24.12f, 92.45f, 0},
  {23.89f, 88.67f, 0},
  {22.78f, 91.34f, 0},
  {23.45f, 90.12f, 0},
  {24.23f, 93.56f, 0},
  {23.12f, 89.45f, 0},
  {30.12f, 148.34f, 1},
  {29.45f, 152.67f, 1},
  {31.23f, 160.12f, 1},
  {30.78f, 149.89f, 1},
  {29.67f, 151.23f, 1},
  {30.34f, 155.67f, 1},
  {31.12f, 158.45f, 1},
  {29.89f, 150.12f, 1},
  {30.56f, 153.78f, 1},
  {31.34f, 159.23f, 1},
  {29.78f, 147.89f, 1},
  {30.45f, 154.12f, 1},
  {31.23f, 157.67f, 1},
  {29.56f, 149.34f, 1},
  {30.12f, 152.45f, 1},
  {31.45f, 160.78f, 1},
  {29.67f, 151.89f, 1},
  {30.34f, 155.12f, 1},
  {31.12f, 158.67f, 1},
  {29.89f, 150.45f, 1},
  {30.56f, 153.34f, 1},
  {31.34f, 159.78f, 1},
  {29.78f, 147.45f, 1},
  {30.45f, 154.67f, 1},
  {31.23f, 157.12f, 1},
  {29.56f, 149.89f, 1},
  {30.12f, 152.34f, 1},
  {31.45f, 160.12f, 1},
  {29.67f, 151.56f, 1},
  {30.34f, 155.89f, 1},
  {31.12f, 158.23f, 1},
  {29.89f, 150.67f, 1},
  {30.56f, 153.45f, 1},
  {31.34f, 159.12f, 1},
  {29.78f, 147.67f, 1},
  {30.45f, 154.34f, 1},
  {31.23f, 157.89f, 1},
  {29.56f, 149.12f, 1},
  {30.12f, 152.78f, 1},
  {31.45f, 160.34f, 1},
  {29.67f, 151.45f, 1},
  {30.34f, 155.23f, 1},
  {31.12f, 158.56f, 1},
  {29.89f, 150.89f, 1},
  {30.56f, 153.12f, 1},
  {31.34f, 159.45f, 1},
  {29.78f, 147.34f, 1},
  {30.45f, 154.89f, 1},
  {31.23f, 157.45f, 1},
  {29.56f, 149.67f, 1},
  {30.12f, 152.12f, 1},
  {31.45f, 160.56f, 1},
};
const int N = sizeof(datos) / sizeof(datos[0]);
float W[3] = {0.0f, 0.0f, 0.0f}; // W0, W1, W2
const float tasa = 0.1f;
const int maxEpocas = 1000;
 
int predecir(float imc, float glucosa) {
  float z = W[0] + W[1]*(imc/10.0f) + W[2]*(glucosa/100.0f);
  return z >= 0.0f ? 1 : 0;
}
void entrenar() {
  for (int epoca = 1; epoca <= maxEpocas; epoca++) {
    int errores = 0;
    for (int i=0; i<N; i++) {
      float x1 = datos[i].imc/10.0f;
      float x2 = datos[i].glucosa/100.0f;
      int obtenido = predecir(datos[i].imc, datos[i].glucosa);
      int error = (int)datos[i].diagnostico - obtenido;
      if (error != 0) {
        W[0] += tasa * error;
        W[1] += tasa * error * x1;
        W[2] += tasa * error * x2;
        errores++;
      }
    }
    Serial.print(F("Epoca ")); Serial.print(epoca);
    Serial.print(F(" | Errores durante entrenamiento: ")); Serial.println(errores);
    if (errores == 0) break;
  }
}
void evaluar() {
  int aciertos=0;
  for (int i=0;i<N;i++) {
    if (predecir(datos[i].imc,datos[i].glucosa)==datos[i].diagnostico) aciertos++;
  }
  Serial.println(F("--- RESULTADOS ---"));
  Serial.print(F("Registros: ")); Serial.println(N);
  Serial.print(F("W0 = ")); Serial.println(W[0],6);
  Serial.print(F("W1 = ")); Serial.println(W[1],6);
  Serial.print(F("W2 = ")); Serial.println(W[2],6);
  Serial.print(F("Aciertos: ")); Serial.println(aciertos);
  Serial.print(F("Exactitud (%): ")); Serial.println(100.0f*aciertos/N,2);
  Serial.println(F("Z = W0 + W1*(IMC/10) + W2*(Glucosa/100)"));
  Serial.println(F("Frontera: Z = 0"));
  if (W[2] != 0.0f) {
    Serial.print(F("Glucosa = "));
    Serial.print(-100.0f*W[0]/W[2],6);
    float pendiente = -10.0f*W[1]/W[2];
    if (pendiente >= 0) Serial.print(F(" + "));
    else Serial.print(F(" - "));
    Serial.print(pendiente < 0 ? -pendiente : pendiente,6);
    Serial.println(F(" * IMC"));
  } else Serial.println(F("No es posible despejar glucosa: W2 = 0"));
}
void setup() {
  Serial.begin(9600);
  entrenar();
  evaluar();
}
void loop() {}