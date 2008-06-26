#include <LCD4Bit.h> //importa libreria lcd
LCD4Bit lcd = LCD4Bit(2); //cuantas linesas tiene la pantalla

//pines de los botones
int pinBot1 = 4;
int pinBot2 = 5;
//estados de los botones
int state1a = 0; 
int state1b = 0;
int state2a = 0; 
int state2b = 0;

//comunicacion serial
int mandaPython = 0;

//tiempo
long intervalo = 0;

void setup(){
  //modos de los pines
  pinMode(pinBot1, INPUT);
  pinMode(pinBot2, INPUT);
  //inicia el serial
  Serial.begin(9600);
  //inicial el lcd
  lcd.init();
  escribeSaludo();
  //inicia el timepo
  intervalo = millis();
}

//Funcion para escribir la pregnta en lcd
void escribePregunta(){
  if (millis() - intervalo > 7000){
    intervalo = millis();
    //Serial.println (intervalo);
  }
  else if (millis() - intervalo ==  1000){
    //Serial.println (millis() - intervalo);
    lcd.leftScroll(20,50);
    lcd.clear();
    lcd.printIn("La conciencia de ");
    lcd.cursorTo(2,0);
    lcd.printIn("ser observado");
  } 
  else if   (millis() - intervalo ==  4500){
    //Serial.println (millis() - intervalo);
    lcd.leftScroll(20,50);
    lcd.clear();
    lcd.printIn("acrecenta su");
    lcd.cursorTo(2,0);
    lcd.printIn("sensacion de ");
  }  
  else if (millis() - intervalo == 7000){
    //Serial.println (millis() - intervalo);
    lcd.leftScroll(20,50);
    lcd.clear();
    lcd.printIn("seguridad?");
  } 
}

//Escribe un saludo en el lcd
void escribeSaludo(){
  lcd.clear();
  lcd.printIn("Hola");
  lcd.cursorTo(2,0);
  lcd.printIn("El Pola");
}

void leeBotones(){
  //lee el estado de los botones
  state1a = digitalRead(pinBot1);
  state2a = digitalRead(pinBot2);
  //Serial.println(state1a);

  //logica para saber como estan los botones
  if (state1a == 0){
    if (state1b == 1){
      Serial.println("bot1");
    }
  }
  if (state2a == 0){
    if (state2b == 1){
      Serial.println("bot2");
    }
  }
  state1b = state1a;
  state2b = state2a; 
}

void loop(){
  leeBotones(); 
  //control de acciones desde Python
 if (Serial.available()>0){
    mandaPython = Serial.read();
    //Serial.println(mandaPython); 
 }
    //2. escribe la pregunta
    if (mandaPython == 50){    
      escribePregunta();  
    } 

    //3. escribe el saludo 
    if(mandaPython == 51){
      escribeSaludo(); 
    }

  }

