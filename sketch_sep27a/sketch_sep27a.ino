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
                }
        }
}
