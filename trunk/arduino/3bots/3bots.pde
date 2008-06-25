int pinBot1 = 4;
int pinBot2 = 5;
int pinBot3 = 6;

int state1a = 0; 
int state1b = 0;
int state2a = 0; 
int state2b = 0;
int state3a = 0; 
int state3b = 0;

void setup(){
  pinMode(pinBot1, INPUT);
  pinMode(pinBot2, INPUT);
  pinMode(pinBot3, INPUT);
  Serial.begin(9600);
}

void loop(){
  state1a = digitalRead(pinBot1);
  state2a = digitalRead(pinBot1);
  state3a = digitalRead(pinBot1);
  Serial.println(state1a);
  
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
  if (state3a == 0){
    if (state3b == 1){
      Serial.println("bot3");
    }
  }
  state1b = state1a;
  state2b = state2a;
  state3b = state3a;
}
