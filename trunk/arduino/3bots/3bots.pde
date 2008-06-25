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

void setup(){
  //modos de los pines
  pinMode(pinBot1, INPUT);
  pinMode(pinBot2, INPUT);
  //inicia el serial
  Serial.begin(9600);
  //inicial el lcd
  lcd.init();
    lcd.clear();
 lcd.printIn("Hola");
  lcd.cursorTo(2,0);
 lcd.printIn("El Polarizador");
}

void loop(){
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
