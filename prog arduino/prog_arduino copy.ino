String str;  

void setup() {
        Serial.begin(115200);      
        pinMode(7, OUTPUT);
}

void loop() {
        if (Serial.available() > 0) {
                str = Serial.readStringUntil('\n');  
             
                if (str == "allumer led"){
                  digitalWrite(7, HIGH);
                }

                 if (str == "éteindre led"){
                  digitalWrite(7, LOW);

                if (str == "ouvrir poubelle"){
                        //OUVRIR
                        //digitalWrite(7, HIGH)
                        //delay(1000)
                        //digitalWrite(7, LOW)

                if (str == "fermer poubelle"){
                        //FERMER
                        //digitalWrite(7, LOW)
                        //delay(1000)
                        //digitalWrite(7, HIGH)
                }
                if (str == "augh"){
                        //AAAUUGH
                        //digitalWrite(7, HIGH)
                        //delay(1000)
                        //digitalWrite(7, HIGH)
                }
                }
        }
}
