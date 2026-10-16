// Perceptron de anemia: inferencia con pesos entrenados en Python.
// Monitor Serie a 9600: Edad,Energia,Frecuencia,Antecedentes
const float W0=0.0, W1=-0.006, W2=-0.030, W3=0.016, W4=0.100;
void setup(){
  Serial.begin(9600); Serial.setTimeout(1000);
  Serial.println(F("Introduzca Edad,Energia,Frecuencia,Antecedentes"));
}
void loop(){
  if(!Serial.available()) return;
  String s=Serial.readStringUntil('\n'); s.trim();
  int a=s.indexOf(','), b=s.indexOf(',',a+1), c=s.indexOf(',',b+1);
  if(a<0||b<0||c<0||s.indexOf(',',c+1)>=0){
    Serial.println(F("Formato: 35,5,90,1")); return;
  }
  String t1=s.substring(0,a),t2=s.substring(a+1,b),t3=s.substring(b+1,c),t4=s.substring(c+1);
  t1.trim();t2.trim();t3.trim();t4.trim();
  if(!t1.length()||!t2.length()||!t3.length()||(t4!="0"&&t4!="1")){
    Serial.println(F("Datos incompletos o antecedentes invalidos")); return;
  }
  float edad=t1.toFloat(), energia=t2.toFloat(), frecuencia=t3.toFloat();
  int ant=t4.toInt();
  if(edad<=0||energia<0||frecuencia<=0){Serial.println(F("Valores fuera de rango"));return;}
  float z=W0+W1*(edad/100.0)+W2*(energia/10.0)+W3*(frecuencia/100.0)+W4*ant;
  int y=z>=0?1:0;
  Serial.print(F("Z = "));Serial.println(z,6);
  Serial.print(F("Y = "));Serial.println(y);
  Serial.println(y?F("Clase: CON ANEMIA (1)"):F("Clase: SIN ANEMIA (0)"));
  Serial.println(F("Uso academico; no es diagnostico medico."));
  Serial.println(F("Ingrese otro registro:"));
}
