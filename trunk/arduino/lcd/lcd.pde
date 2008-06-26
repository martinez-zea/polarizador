#include <LCD4Bit.h> //importa libreria lcd
LCD4Bit lcd = LCD4Bit(2); //cuantas linesas tiene la pantalla

//comunicacion serial
int mandaPython = 0;

//tiempo
long intervalo = 0;
long intervalo2 = 0;

void setup(){
  //inicia el serial
  Serial.begin(9600);
  //inicial el lcd
  lcd.init();
  escribeSaludo();
  //inicia el tiempo
  intervalo = millis();
  intervalo2 = millis();
}

//Escribe un saludo en el lcd
void escribeSaludo(){
  if (millis() - intervalo2 > 6000){
    intervalo2 = millis();
  } 
  else if (millis() - intervalo2 == 2000){
  lcd.leftScroll(20,50);
  lcd.clear();
  lcd.printIn("Soy El ");
  lcd.cursorTo(2,0);
  lcd.printIn("Polarizador");
  }
  else if (millis() - intervalo2 == 4000){
  lcd.leftScroll(20,50);
  lcd.clear();
  lcd.printIn("Identifiquese ");  
  lcd.cursorTo(2,0);
  lcd.printIn("Usando su");
  }
  else if (millis() - intervalo2 == 6000){
    lcd.leftScroll(20,50);
  lcd.clear();
  lcd.printIn("Codigo de barras");
  }
}

void escribePregunta(){
  if (millis() - intervalo > 7000){
      intervalo = millis();
      Serial.println (intervalo);
  }else if (millis() - intervalo ==  1000){
  Serial.println (millis() - intervalo);
    lcd.leftScroll(20,50);
  lcd.clear();
  lcd.printIn("La conciencia de ");
  lcd.cursorTo(2,0);
  lcd.printIn("ser observado");
  } else if   (millis() - intervalo ==  4500){
  Serial.println (millis() - intervalo);
  lcd.leftScroll(20,50);
  lcd.clear();
  lcd.printIn("acrecenta su");
  lcd.cursorTo(2,0);
  lcd.printIn("sensacion de ");
  }  else if (millis() - intervalo == 7000){
 Serial.println (millis() - intervalo);
    //delay(2000);
  lcd.leftScroll(20,50);
  lcd.clear();
  lcd.printIn("seguridad?");
 } 
}

void loop(){
 escribeSaludo(); 
 
}
