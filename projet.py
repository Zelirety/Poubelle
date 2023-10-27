import speech_recognition as sr
import serial

ser = serial.Serial('COM9', 115200, timeout=0)
r = sr.Recognizer()

while True:
    with sr.Microphone() as mic:
        try:
            print("Silence please, calibrating...")
            r.adjust_for_ambient_noise(mic, duration=2)
            print("calibrated, speak now...")
            audio = r.listen(mic)
            text = r.recognize_google(audio)
            text = text.lower()
            print("You said "+text+"\n")
            ser.write(str.encode(text))
            
            
        except sr.UnknownValueError:
            print("Could not understand audio")
            
        except sr.RequestError as e:
            print("Request error; {0}".format(e))