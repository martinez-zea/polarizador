/*
#    El Polarizador
#    http://nerdbots.info/polarizador
#    Camilo Martinez <cmart AT decoloector DOT net>
#    Gabriel Zea <zea AT randomlab DOT net>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#   Polarizador -- Control LCD 
#   Controla la secuencia de escritura de mensajes en un LCD
#   a partir de mensajes enviados por el puerto serial
#
#   Utiliza la libreria LiquidCristal
#
#   Nerdbots 2008 -2009 
#   martinez-zea 2012
*/

#include <LiquidCrystal.h> //importa libreria lcd

//LiquidCrystal(rs, enable, d4, d5, d6, d7) 
LiquidCrystal lcd(12,2,7,8,9,10);

//comunicacion serial
int mandaPython = 0;

//tiempo
long character = 20;
long scrollChar = 10;
long waitToRead = 1000;
long previousMillisChar = 0;
long previousMillisScrl = 0;
long previousMillisRead =0;

int counter1 = 0;
int counter2 = 0;

void setup(){
  //inicia el serial
  Serial.begin(9600);
  
  //inicial el lcd
  lcd.begin(16,2);
  //escribeSaludo();
}

//Escribe un saludo en el lcd
void escribeSaludo(){
  String soy = "Soy El  ";
  String elPola = "Polarizador   ";
  String identifiquese = "Identifiquese   ";
  String usando = "usando su   ";
  String codigo = "codigo de barras   ";

  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(soy);
  lcd.setCursor(0,1);
  lcd.print(elPola);
  scroll();  
  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(identifiquese);
  lcd.setCursor(0,1);
  lcd.print(usando);
  scroll();
  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(codigo);
  scroll();
}

void preguntaUno(){
  String conciencia = "La conciencia de    ";
  String ser = "ser observado    ";
  String acrecenta = "acrecenta su    ";
  String sensacion = "sensacion de    ";
  String seguridad = "seguridad?    ";

  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(conciencia);
  lcd.setCursor(0,1);
  lcd.print(ser);
  scroll();

  lcd.clear();
  writeToScreen(0, acrecenta);
  writeToScreen(1, sensacion);
  scroll();
  
  lcd.clear();
  writeToScreen(0, seguridad);
  scroll();
}

void preguntaDos(){
  String estar = "Estar en una    ";
  String base = "base de datos    ";
  String pertenecer = "es pertenecer a    ";
  String comunidad = "una comunidad?    ";

  lcd.clear();
  writeToScreen(0, estar);
  writeToScreen(1, base);
  scroll();

  lcd.clear();
  writeToScreen(0, pertenecer);
  writeToScreen(1, comunidad);
  scroll();
}


void preguntaTres(){
  String deberia = "Deberia usted    ";
  String acceso = "tener acceso a    ";
  String informacion = "la informacion   ";
  String otros = "de otros?    ";
  
  lcd.clear();
  writeToScreen(0, deberia);
  writeToScreen(1, acceso);
  scroll();
  
  lcd.clear();
  writeToScreen(0, informacion);
  writeToScreen(1, otros);
  scroll();
}

void writeToScreen(int line, String sentence){
  int s = sentence.length()+1;
  char snc[s]; 
  sentence.toCharArray(snc,s);
  //int counter = 0;
  
  lcd.setCursor(0,line);
  if (counter1 < sizeof(snc)-1){
    unsigned long currentMillis = millis();
    if(currentMillis - previousMillisChar > character){
      previousMillisChar = currentMillis;
      lcd.print(snc[counter1]);
      counter1++;
    }  
  } else {
    counter1 = 0;
  }
}

void scroll(){
 for (int positionCounter = 0; positionCounter < 13; positionCounter++) {
    // scroll one position left:
    lcd.scrollDisplayLeft(); 
    // wait a bit:
    delay(150);
  }
}

void loop(){
  escribeSaludo();

/*  
  if (Serial.available() > 0) {
      Serial.println(Serial.read());
        mandaPython = Serial.read();
  }
 
  if (mandaPython == 49){
    preguntaUno();
  } else if (mandaPython == 50){
    preguntaDos();
  } else if (mandaPython == 51){
    preguntaTres();
  } else {
    escribeSaludo();
  }
 */
}
