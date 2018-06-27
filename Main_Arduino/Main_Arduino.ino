#include <SoftwareSerial.h>

const int stepPin1 = 10;
const int dirPin1 = 11;
const int stepPin2 = 2;
const int dirPin2 = 3;
const int stepTime = 12;


SoftwareSerial BT(5, 6); //TX, RX from Arduino POV

int getInput();
void moveMotors(char);
void pick();

void setup() {  
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);

  Serial.begin(9600);
  BT.begin(9600);
}

void loop() {
  while(getInput());
  while(Serial.available() == 0);
  char inChar = '\0';
  while(inChar != 'x') {
    inChar = Serial.read();
    moveMotors(inChar);
  }
}

int getInput() {
  char inChar = '\0';
  while(BT.available()) {
    inChar = (char)BT.read();
    if(inChar >= '1' && inChar <= '6') {
      Serial.print(inChar);
      return 1;
    }
  }
  return 0;
}

void moveMotors(char inChar) {
  if(inChar == 'l') {
    digitalWrite(dirPin1, HIGH);
    digitalWrite(stepPin1, HIGH);
    delay(stepTime);
    digitalWrite(stepPin1, LOW);
    delay(stepTime);
  }
  if(inChar == 'r') {
    digitalWrite(dirPin1, LOW);
    digitalWrite(stepPin1, HIGH);
    delay(stepTime);
    digitalWrite(stepPin1, LOW);
    delay(stepTime);
  }
  if(inChar == 'u') {
    digitalWrite(dirPin2, HIGH);
    digitalWrite(stepPin2, HIGH);
    delay(stepTime);
    digitalWrite(stepPin2, LOW);
    delay(stepTime);
  }
  if(inChar == 'd') {
    digitalWrite(dirPin2, LOW);
    digitalWrite(stepPin2, HIGH);
    delay(stepTime);
    digitalWrite(stepPin2, LOW);
    delay(stepTime);
  }
  if(inChar == 'p') {
    pick();
  }
}
void pick() {
  delay(1000);
}
