#include <Servo.h>

Servo steer;
Servo esc; //ESC - Electronic Speed Controller | This is attached to the motor propelling the rover
           // 1000 Microseconds = Full speed Backwards (Motor spins Counterclockwise?)
           // 1500 microseconds = Neutral
           // 2000 Microseconds = Full speed Forward (Motor spins Clockwise?)
int Steer_Position = 0;

void setup(){
  Serial.begin(9600);
  steer.attach(4);
  esc.attach(5);

  steer.write(93);
  esc.writeMicroseconds(1500);
  delay(2000);
}

void loop(){
  
  for(int pos = 1500 ; pos <= 1700; pos+=50){
    esc.writeMicroseconds(pos);
    Serial.println(pos);
    delay(1500);
  }
  esc.writeMicroseconds(1500);
  delay(100000);
}