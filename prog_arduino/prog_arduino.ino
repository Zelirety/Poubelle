String str;  

void setup() {
        Serial.begin(115200);      
        pinMode(7, OUTPUT);
}

void loop() {
        if (Serial.available() > 0) {
                str = Serial.readStringUntil('\n');  
             
                if (str == "allumer moteur"){
                  digitalWrite(7, HIGH);

                  delay(200);
                  digitalWrite(7, LOW);
                  
                }

        }
}
