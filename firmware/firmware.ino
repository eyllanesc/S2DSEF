#include "I2Cdev.h"
#include "MPU6050.h"

#include "Wire.h"

MPU6050 accelgyro;

int16_t ax, ay, az;
int16_t gx, gy, gz;

char inByte;

#define LED_PIN 13
bool blinkState = false;

void setup() {
  Wire.begin();
  Serial.begin(9600);
  accelgyro.initialize();
  pinMode(LED_PIN, OUTPUT);
}

void loop() {}

void serialEvent() {  
  while (Serial.available()) {
    inByte = Serial.read();        
    if( inByte == '0' ){
      accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
      Serial.print(ax); 
      Serial.print(" ");
      Serial.print(ay); 
      Serial.print(" ");
      Serial.println(az); 
      blinkState = !blinkState;
      digitalWrite(LED_PIN, blinkState);
    }
  }
}
