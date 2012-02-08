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
#   Utiliza la libreria LCD4bit
#
#   Nerdbots 2008 -2009


#include <LCD4Bit.h> //importa libreria lcd
LCD4Bit lcd = LCD4Bit(2); //cuantas lineas tiene la pantalla

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

void preguntaUno(){
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

void preguntaDos(){
  if (millis() - intervalo > 7000){
      intervalo = millis();
      Serial.println (intervalo);
  }else if (millis() - intervalo ==  1000){
  Serial.println (millis() - intervalo);
    lcd.leftScroll(20,50);
  lcd.clear();
  lcd.printIn("Estar en una base");
  lcd.cursorTo(2,0);
  lcd.printIn("de datos es  ");
  } else if   (millis() - intervalo ==  4500){
  Serial.println (millis() - intervalo);
  lcd.leftScroll(20,50);
  lcd.clear();
  lcd.printIn("pertenecer a");
  lcd.cursorTo(2,0);
  lcd.printIn("una comunidad?");
  } 
}

void preguntaTres(){
  if (millis() - intervalo > 7000){
      intervalo = millis();
      Serial.println (intervalo);
  }else if (millis() - intervalo ==  1000){
  Serial.println (millis() - intervalo);
    lcd.leftScroll(20,50);
  lcd.clear();
  lcd.printIn("Deberia usted    ");
  lcd.cursorTo(2,0);
  lcd.printIn("tener acceso a la");
  } else if   (millis() - intervalo ==  4500){
  Serial.println (millis() - intervalo);
  lcd.leftScroll(20,50);
  lcd.clear();
  lcd.printIn("informacion ");
  lcd.cursorTo(2,0);
  lcd.printIn("de otros?");
  } 
}

void loop(){
  escribeSaludo(); 
  if (Serial.available() > 0) {
        mandaPython = Serial.read();
  }

  if (mandaPyhton == 1){
    preguntaUno();
  } else if (mandaPyhton == 2){
    preguntaDos();
  } else if (mandaPython == 3){
    preguntaTres();
  } else {
    escribeSaludo();
  }
}
