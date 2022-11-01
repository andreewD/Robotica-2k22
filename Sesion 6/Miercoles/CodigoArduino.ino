#include <Servo.h>
#define Trigger 3
#define Echo  4
// Define las llantas
#define LlantaIA  7
#define LlantaIR  6
#define LlantaDA  5
#define LlantaDR  4
//Define los sensores
#define Si 13
#define Sc 12
#define Sd 11
//variables
int sA,sB,sC;
int velocidad = 0;
int Estabilizador = 0;
int Graduador,Referencia;
unsigned long Tiempo;
int Centraliza = 0;
int Direccion = 0;
//velocidad
#define PwmI 10
#define PwmD 9
Servo jkr;
int Distancia;
void setup(){
  //para el sensor ultrasonido
  pinMode(Trigger,OUTPUT);
  pinMode(Echo,INPUT);
  pinMode(A0,INPUT);
  //para las llantas
  pinMode(LlantaIA,OUTPUT);
  pinMode(LlantaIR,OUTPUT);
  pinMode(LlantaDA,OUTPUT);
  pinMode(LlantaDR,OUTPUT);
  //para los sensores
  pinMode(Si,INPUT);
  pinMode(Sc,INPUT);
  pinMode(Sd,INPUT);
  //configuracion pwm
  pinMode(PwmI,OUTPUT);
  pinMode(PwmD,OUTPUT);
  //Velocidad de comunicacion
  Serial.begin(9600);
  //jkr.attach(3);
  //jkr.write(90);
  }
  void loop(){
    // Leer los sensores
    sA = digitalRead(Si);
    sB = digitalRead(Sc);
    sC = digitalRead(Sd);
    //Sensor Central
    if (sA==LOW && sB==HIGH && sC==LOW){
      analogWrite(PwmI,100);
      analogWrite(PwmD,100);
      digitalWrite(LlantaIA,HIGH);
      digitalWrite(LlantaIR,LOW);

      digitalWrite(LlantaDA,HIGH);
      digitalWrite(LlantaDR,LOW);

      Referencia = 0;
      Graduador = 0;
      Estabilizador = 0;
      delay(300);
      Direccion = 0;      
    }
    //Sensor central izquierda
    if (sA==HIGH && sB==HIGH && sC==LOW){
      analogWrite(PwmI,50);
      analogWrite(PwmD,150+Graduador);
      digitalWrite(LlantaIA,HIGH);
      digitalWrite(LlantaIR,LOW);

      digitalWrite(LlantaDA,HIGH);
      digitalWrite(LlantaDR,LOW);

      delay(100);
      analogWrite(PwmI,30);
      analogWrite(PwmD,100+Graduador);

      digitalWrite(LlantaIA,HIGH);
      digitalWrite(LlantaIR,LOW);
      digitalWrite(LlantaDA,HIGH);
      digitalWrite(LlantaDR,LOW);
    }
    //Sensor central derecha
    if (sA==LOW && sB==HIGH && sC==HIGH){
      analogWrite(PwmI,150+Graduador);
      analogWrite(PwmD,50);
      digitalWrite(LlantaIA,HIGH);
      digitalWrite(LlantaIR,LOW);

      digitalWrite(LlantaDA,HIGH);
      digitalWrite(LlantaDR,LOW);

      Referencia = 0;
      delay(100);
      analogWrite(PwmI,100 + Graduador);
      analogWrite(PwmD,30);

      digitalWrite(LlantaIA,HIGH);
      analogWrite(LlantaIR,LOW);
      digitalWrite(LlantaDA,HIGH);
      digitalWrite(LlantaDR,LOW);
      Referencia = 0;
    }
    //Sensor izquierda
    if (sA==HIGH && sB==LOW && sC==LOW){
      analogWrite(PwmI,15);
      analogWrite(PwmD,140 + Graduador);
      digitalWrite(LlantaIA,HIGH);
      digitalWrite(LlantaIR,LOW);

      digitalWrite(LlantaDA,HIGH);
      digitalWrite(LlantaDR,LOW);
      Estabilizador = 1;
    }
    // SensorDerecha
    if (sA==LOW && sB==LOW && sC==HIGH){
      analogWrite(PwmI,140 + Graduador);
      analogWrite(PwmD,15);
      digitalWrite(LlantaIA,HIGH);
      digitalWrite(LlantaIR,LOW);

      digitalWrite(LlantaDA,HIGH);
      digitalWrite(LlantaDR,LOW);
      Estabilizador = 2;
    }
    //Estabilizada
    if (sA==HIGH && sB==HIGH && sC==HIGH){
      if (Estabilizador == 1){
        analogWrite(PwmI,80);
        analogWrite(PwmD,100);
        digitalWrite(LlantaIA,HIGH);
        digitalWrite(LlantaIR,LOW);
        digitalWrite(LlantaDA,LOW);
        digitalWrite(LlantaDR,HIGH);
        Referencia = 0;
        Graduador = 0;
        delay(700);
      }
      if (Estabilizador == 2){
        analogWrite(PwmI,100);
        analogWrite(PwmD,80);
        digitalWrite(LlantaIA,LOW);
        digitalWrite(LlantaIR,HIGH);
        digitalWrite(LlantaDA,HIGH);
        digitalWrite(LlantaDR,LOW);
        Referencia = 0;
        Graduador = 0;
        delay(700);
      }
    }
    if (sA==LOW && sB==LOW && sC==LOW){
      if (Estabilizador == 1){
        analogWrite(PwmI,20);
        analogWrite(PwmD,200);
        digitalWrite(LlantaIA,HIGH);
        digitalWrite(LlantaIR,LOW);
        digitalWrite(LlantaDA,HIGH);
        digitalWrite(LlantaDR,LOW);
        Referencia = 0;
        Graduador = 0;        
      }
      if (Estabilizador == 2){
        analogWrite(PwmI,200);
        analogWrite(PwmD,20);
        digitalWrite(LlantaIA,HIGH);
        digitalWrite(LlantaIR,LOW);
        digitalWrite(LlantaDA,HIGH);
        digitalWrite(LlantaDR,LOW);
        Referencia = 0;
        Graduador = 0;        
      }
    }
 }