#include "Ultrasonic.h"
String str;
int status;

Ultrasonic ultrasonic(7);

void setup() {
        Serial.begin(115200);      
        pinMode(8, OUTPUT);
        status = 0; // Le couvercle est fermé
}

void loop() {
        if (Serial.available() > 0) {
                str = Serial.readStringUntil('\n');  
             
                if (str == "ouvrir poubelle" and status == 0){
                  digitalWrite(8, HIGH);
                  status = 1; //Le couvercle est ouvert
                }

                if (str == "fermer poubelle" and status == 1){
                  digitalWrite(8, LOW);
                  delay(3000);
                  status = 0; //Couvercle fermé
                }

        }
        if (status == 0){
          long RangeInInches;
          long RangeInCentimeters;
          
          RangeInCentimeters = ultrasonic.MeasureInCentimeters(); // intervalles nécessaires entre 2 mesures
          Serial.println(RangeInCentimeters);
          delay(250);
        }
      
     
}
