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
int mandaPython = 54; //init on Saludo

//tiempo
long waitToRead = 0;
long wait2read = 0;

boolean writing = false;

void setup(){
  //inicia el serial
  Serial.begin(9600);
  
  //inicial el lcd
  lcd.begin(0,2);
  escribeSaludo();
  
  waitToRead = millis();
  wait2read = millis();
}

//Escribe un saludo en el lcd
void escribeSaludo(){
  String soy = "Soy El  ";
  String elPola = "Polarizador   ";
  String identifiquese = "Identifiquese   ";
  String usando = "usando su   ";
  String codigo = "codigo de barras   ";
  
  if(millis() - waitToRead > 6000){
    waitToRead = millis();
  } else if (millis() - waitToRead == 500){
    scroll();
    lcd.clear();
    writeToScreen(0, soy);
    writeToScreen(1, elPola);
  } else if (millis() - waitToRead == 4000){
    scroll();
    lcd.clear();
    writeToScreen(0, identifiquese);
    writeToScreen(1, usando);
  } else if (millis() - waitToRead == 6000){
    scroll();
    lcd.clear();
    writeToScreen(0, codigo);
  }
}


void preguntaUno(){
  String conciencia = "La conciencia de    ";
  String ser = "ser observado    ";
  String acrecenta = "acrecenta su    ";
  String sensacion = "sensacion de    ";
  String seguridad = "seguridad?    ";
  wait2read = millis();
  
  while(writing == true){ 
    if(millis() - wait2read > 9000){
      wait2read = millis();
      writing = false;
    } else if (millis() - wait2read == 1000){
      scroll();
      lcd.clear();
      writeToScreen(0, conciencia);
      writeToScreen(1, ser);
    } else if (millis() - wait2read == 4500){
      scroll();
      lcd.clear();
      writeToScreen(0, acrecenta);
      writeToScreen(1, sensacion);
    } else if (millis() - wait2read == 7000){
      scroll();
      lcd.clear();
      writeToScreen(0, seguridad);
    }else if (millis() - wait2read == 9000){
      scroll();
      lcd.clear();
      //writing = false;
    }
  }    
}

void preguntaDos(){
  String estar = "Estar en una    ";
  String base = "base de datos    ";
  String pertenecer = "es pertenecer a    ";
  String comunidad = "una comunidad?    ";
  wait2read = millis();
  
  while(writing == true){ 
    if(millis() - wait2read > 6000){
      wait2read = millis();
      writing = false;
    } else if (millis() - wait2read == 2000){
      scroll();
      lcd.clear();
      writeToScreen(0, estar);
      writeToScreen(1, base);
    } else if (millis() - wait2read == 4000){
      scroll();
      lcd.clear();
      writeToScreen(0, pertenecer);
      writeToScreen(1, comunidad);
    } else if (millis() - wait2read == 6000){
      scroll();
      lcd.clear();
      //writing = false;
    }
  }
}


void preguntaTres(){
  String deberia = "Deberia usted    ";
  String acceso = "tener acceso a    ";
  String informacion = "la informacion   ";
  String otros = "de otros?    ";
  wait2read = millis();
  
  while(writing == true){ 
    if(millis() - wait2read > 6000){
      wait2read = millis();
      writing = false;
    } else if (millis() - wait2read == 2000){
      scroll();
      lcd.clear();
      writeToScreen(0, deberia);
      writeToScreen(1, acceso);
    } else if (millis() - wait2read == 4000){
      scroll();
      lcd.clear();
      writeToScreen(0, informacion);
      writeToScreen(1, otros);
    } else if (millis() - wait2read == 6000){
      scroll();
      lcd.clear();
      //writing = false;
    }
    
  }  
}

void boton(){
  String presione = "Presione un";
  String responder = "boton para ";
  String pregunta = "responder la ";
  String pregunta2 = "pregunta";
  wait2read = millis();
  
  while(writing == true){
    if(millis() - wait2read > 4500){
      wait2read = millis();
      writing = false;
    } else if (millis() - wait2read == 500){
      scroll();
      lcd.clear();
      writeToScreen(0, presione);
      writeToScreen(1, responder);
    } else if (millis() - wait2read == 3000){
      scroll();
      lcd.clear();
      writeToScreen(0, pregunta);
      writeToScreen(1, pregunta2);
    } else if (millis() - wait2read == 4500){
      scroll();
      lcd.clear();
      writing = false;
    } 
  }    
 }

void gracias(){
  String gracias = "gracias por";
  String uso = "utilizarme ";
  wait2read = millis();
  
  while(writing == true){
    if(millis() - wait2read > 3000){
      wait2read = millis();
      writing = false;
    } else if (millis() - wait2read == 500){
      scroll();
      lcd.clear();
      writeToScreen(0, gracias);
      writeToScreen(1, uso);
    }else if (millis() - wait2read == 3000){
      scroll();
      lcd.clear();
      writing = false;
    } 
  }    
}

void writeToScreen(int line, String sentence){
  lcd.setCursor(0,line);
  lcd.print(sentence);
}

void scroll(){  
    for(int i = 0; i < 17; i++){
      lcd.scrollDisplayLeft();
      delay(50);
    }
}

void loop(){
  if (Serial.available() > 0) {
      mandaPython = Serial.read();
      Serial.println(mandaPython, DEC);
  }
  
  if (mandaPython == 49){
    writing = true;
   // mandaPython = 0;
    preguntaUno();
  } else if (mandaPython == 50){
     writing = true;
    // mandaPython =0;
     preguntaDos();
  } else if (mandaPython == 51){
    writing = true;
    //mandaPython = 0;
    preguntaTres();
  } else if (mandaPython == 52){
    writing = true;
    //mandaPython = 0;
    boton();
  } else if (mandaPython == 53){
    writing = true;
    //mandaPython = 0;
    gracias();
  } else if (mandaPython == 54) {
    escribeSaludo();
  }
}
