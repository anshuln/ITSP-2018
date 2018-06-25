#include <SoftwareSerial.h>

int stepPin1 = 10;
int dirPin1 = 11;
int stepPin2 = 2;
int dirPin2 = 3;
int stepTime = 12;

char inChar = '\0';

SoftwareSerial BT(5, 6); //TX, RX from Arduino POV

void setup() {  
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600);
  BT.begin(9600);
}


void loop() {
  getInput();
  while(Serial.available() == 0);
  moveMotors();
  Serial.print('f');  
}

int getInput() {
  while(BT.available()) {
    inChar = (char)BT.read();
    if(inChar >= '1' && inChar <= '6') {
      Serial.print(inChar);
      return 1;
    }
  }
  return 0;
}

void moveMotors() {
  while(Serial.available()){
    if(Serial.read()==int('l')) {
      digitalWrite(dirPin1, HIGH);
      digitalWrite(stepPin1, HIGH);
      delay(stepTime);
    }
    if(Serial.read()==int('r')) {
      digitalWrite(dirPin1, LOW);
      digitalWrite(stepPin1, HIGH);
      delay(stepTime);
    }
    if(Serial.read()==int('u')) {
      digitalWrite(dirPin2, HIGH);
      digitalWrite(stepPin2, HIGH);
      delay(stepTime);
    }
    if(Serial.read()==int('d')) {
      digitalWrite(dirPin2, LOW);
      digitalWrite(stepPin2, HIGH);
      delay(stepTime);
    }
    if(Serial.read()==int('p')){
      pick();
  }
 }
}
void pick(){
}

