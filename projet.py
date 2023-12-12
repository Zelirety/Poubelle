import speech_recognition as sr
import serial

ser = serial.Serial('COM3', 115200, timeout=0)
#r = sr.Recognizer()

while True:
    #with sr.Microphone() as mic:
    #    try:
     #       print("silence, calibration...")
      #      r.adjust_for_ambient_noise(mic, duration=1)
       #     print("calibré, parlez")
        #    audio = r.listen(mic)
         #   text = r.recognize_google(audio, language='fr-FR')
         #   text = text.lower()
         #   print("Vous avez dit "+text+"\n")
         #   ser.write(str.encode(text))
         #   print(ser.readline())
            
            
        #except sr.UnknownValueError:
        #    print("Could not understand audio")
            
        #except sr.RequestError as e:
        #    print("Request error; {0}".format(e))

        if input('appuie : ') == 'ok':
            ser.write(str.encode('allumer moteur'))