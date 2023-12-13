#include "Ultrasonic.h"
String str;  

Ultrasonic ultrasonic(7);

void setup() {
        Serial.begin(115200);      
        pinMode(8, OUTPUT);
}

void loop() {
        if (Serial.available() > 0) {
                str = Serial.readStringUntil('\n');  
             
                if (str == "allumer moteur"){
                  digitalWrite(8, HIGH);
                  //Serial.write()
                  delay(200);
                  digitalWrite(8, LOW);
                  
                }

        }
     long RangeInInches;
     long RangeInCentimeters;
    
     RangeInCentimeters = ultrasonic.MeasureInCentimeters(); // two measurements should keep an interval
     String range_to_string = String(RangeInCentimeters);
     Serial.write("hello"));//0~400cm
     //Serial.println(" cm");
     delay(250);
}
