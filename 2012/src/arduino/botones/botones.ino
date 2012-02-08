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

#   Polarizador -- Lectura / envio del estado de los botones 
#   Lee el estado de dos botones y los envia por el puerto serial
#
#   Nerdbots 2008 -2009
*/

//pines de los botones
int pinBot1 = 2;
int pinBot2 = 3;
//estados de los botones
int state1a = 0; 
int state1b = 0;
int state2a = 0; 
int state2b = 0;

//comunicacion serial
int mandaPython = 0;


void setup(){
  //modos de los pines
  pinMode(pinBot1, INPUT);
  pinMode(pinBot2, INPUT);
  //inicia el serial
  Serial.begin(9600);

}

void leeBotones(){
  //lee el estado de los botones
  state1a = digitalRead(pinBot1);
  state2a = digitalRead(pinBot2);
  //Serial.println(state1a);

  //logica para saber como estan los botones
  if (state1a == 0){
    if (state1b == 1){
      Serial.println("1");
    }
  }
  if (state2a == 0){
    if (state2b == 1){
      Serial.println("2");
    }
  }
  state1b = state1a;
  state2b = state2a; 
delay(100);
}

void loop(){
 leeBotones();


  }

