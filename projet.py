import speech_recognition as sr #pip install SpeechRecognition et pip install pyaudio
import serial #pip install pyserial

ser = serial.Serial('COM4', 115200, timeout=0) #Mise en relation avec le port série (changer le 1er paramètre en fonction de l'ordinateur)
r = sr.Recognizer() #Initialisation de SpeechRecognition
profondeur_poubelle = 20 #Mesure en cm

while (True):
    with sr.Microphone() as mic:
        try:
            print("silence, calibration...")
            r.adjust_for_ambient_noise(mic, duration=1)
            print("calibré, parlez")
            audio = r.listen(mic)
            text = r.recognize_google(audio, language='fr-FR')
            text = text.lower()
            print("Vous avez dit "+text+"\n")
            ser.write(str.encode(text))
            
        except sr.UnknownValueError:
            print("Could not understand audio")
            
        except sr.RequestError as e:
            print("Request error; {0}".format(e))

        if (ser.in_waiting > 0):
            ligne = str(ser.readline())[2:-5]
            