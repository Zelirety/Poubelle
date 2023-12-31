import speech_recognition as sr #pip install SpeechRecognition et pip install pyaudio
import serial #pip install pyserial
import pygame as pg
import pickle as kl
from debug import *
from Button import *
import sys

pg.init()

ser = serial.Serial('COM4', 115200, timeout=0) #Mise en relation avec le port série (changer le 1er paramètre en fonction de l'ordinateur)
r = sr.Recognizer() #Initialisation de SpeechRecognition

def get_font(size):
    return pg.font.Font(None, size)


class Graphic_interface:
    def __init__(self):
        self.ligne = 0
        self.profondeur = 19

        self.day_1 = 200
        self.day_2 = 100
        self.day_3 = 200
        self.day_4 = 300
        self.day_5 = 400
        self.day_6 = 200
        self.day_7 = 400
        self.day_list = [self.day_1, self.day_2, self.day_3, self.day_4, self.day_5, self.day_6, self.day_7]
        self.screen = pg.display.set_mode((1280, 720))
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 30)
        self.bin = pg.image.load('graphics/U.png')
        self.info_percent = 20
        self.info_history = 500
        with open('list', 'rb') as f:
            self.day_list = kl.load(f)

    def run(self):
        while True:
            #---------Reconaissance vocale----------------
            with sr.Microphone() as mic:
                try:
                    print("silence, calibration...")
                    r.adjust_for_ambient_noise(mic, duration=0.5)
                    print("calibré, parlez")
                    audio = r.listen(mic)
                    text = r.recognize_google(audio, language='fr-FR')
                    text = text.lower()
                    print("Vous avez dit "+text+"\n")
                    ser.write(str.encode(text))
                    
                except sr.UnknownValueError:
                    print("Audio non compréhensible")
                    
                except sr.RequestError as e:
                    print("Request error; {0}".format(e))

            if (ser.in_waiting > 0):
                self.ligne = str(ser.readline())[2:-5]


            #---------Affichage----------------
            self.day_list[6] -= 10
            self.info_history -= 10
            self.info_percent =  int(self.ligne)
            
            pg.draw.rect(self.screen, 'grey', pg.Rect(40, 40, 1200, 640))

            percentage_value = 100 - self.info_percent/self.profondeur*100
            self.screen.blit(self.bin, (700, 250))
            pg.draw.rect(self.screen, 'brown',
                         pg.Rect(765, round(self.info_percent * 27), 260, 540 - round(self.info_percent * 27)))
            percentage = pg.font.Font(None, 60).render(f'{(str(round(percentage_value)))}%', True, 'White')
            self.screen.blit(percentage, (860, 610))
            if percentage_value >= 100:
                self.screen.blit(pg.font.Font(None, 80).render("POUBELLE PLEINE !", True, 'RED'),
                                 (680, 130))
            elif percentage_value >= 60:
                self.screen.blit(pg.font.Font(None, 50).render("Poubelle bientot remplie", True, 'Orange'),
                                 (680, 130))

            pg.draw.rect(self.screen, 'black', pg.Rect(40, 500, 580, 25))

            pg.draw.rect(self.screen, 'yellow', pg.Rect(60, self.day_list[0], 60, 500 - self.day_list[0]))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(140, self.day_list[1], 60, 500 - self.day_list[1]))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(220, self.day_list[2], 60, 500 - self.day_list[2]))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(300, self.day_list[3], 60, 500 - self.day_list[3]))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(380, self.day_list[4], 60, 500 - self.day_list[4]))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(460, self.day_list[5], 60, 500 - self.day_list[5]))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(540, self.info_history, 60, 500 - self.info_history))
            moyenne = ((500 - self.day_list[0] + 500 - self.day_list[1] + 500 - self.day_list[2] +
                        500 - self.day_list[3] + 500 - self.day_list[4] + 500 - self.day_list[5] +
                        500 - self.day_list[6]) / 7) / 10
            self.screen.blit(pg.font.Font(None, 40).render("Nombre d'ouvertures journalières", True, 'black'),
                             (50, 540))
            self.screen.blit(pg.font.Font(None, 30).render(f"{round((500 - self.info_history) / 10)}", True, 'white'),
                             (560, 503))
            self.screen.blit(pg.font.Font(None, 30).render(f"{round((500 - self.day_list[5]) / 10)}", True, 'white'),
                             (480, 503))
            self.screen.blit(pg.font.Font(None, 30).render(f"{round((500 - self.day_list[4]) / 10)}", True, 'white'),
                             (400, 503))
            self.screen.blit(pg.font.Font(None, 30).render(f"{round((500 - self.day_list[3]) / 10)}", True, 'white'),
                             (320, 503))
            self.screen.blit(pg.font.Font(None, 30).render(f"{round((500 - self.day_list[2]) / 10)}", True, 'white'),
                             (240, 503))
            self.screen.blit(pg.font.Font(None, 30).render(f"{round((500 - self.day_list[1]) / 10)}", True, 'white'),
                             (160, 503))
            self.screen.blit(pg.font.Font(None, 30).render(f"{round((500 - self.day_list[0]) / 10)}", True, 'white'),
                             (80, 503))
            self.screen.blit(
                pg.font.Font(None, 40).render(f"Cette semaine : {round(moyenne)} ouvertures en moyennes", True,
                                              'black'),
                (50, 100))
            if moyenne < 5:
                self.screen.blit(pg.font.Font(None, 40).render("Vous utilisez peu la poubelle", True, 'blue'),
                                 (50, 150))
            elif moyenne < 15:
                self.screen.blit(pg.font.Font(None, 40).render("Vous utilisez modérement la poubelle", True, 'green'),
                                 (50, 150))
            elif moyenne < 25:
                self.screen.blit(pg.font.Font(None, 40).render("Vous utilisez souvent la poubelle", True, 'orange'),
                                 (50, 150))
            else:
                self.screen.blit(pg.font.Font(None, 40).render("Vous êtes accro à la poubelle, consultez", True, 'red'),
                                 (50, 150))

            MOUSE_POS = pg.mouse.get_pos()
            QUIT = Button(image=None, pos=(130, 650),
                          text_input="QUIT", font=get_font(80), base_color="Black", hovering_color="Yellow")
            QUIT.changeColor(MOUSE_POS)
            QUIT.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    for i in range(6):
                        self.day_list[i] = self.day_list[i + 1]
                    self.day_list[6] = 500
                    with open('list', 'wb') as f:
                        kl.dump(self.day_list, f)
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if QUIT.checkForInput(MOUSE_POS):
                        for i in range(6):
                            self.day_list[i] = self.day_list[i + 1]
                        self.day_list[6] = 500
                        with open('list', 'wb') as f:
                            kl.dump(self.day_list, f)
                        pg.quit()
                        sys.exit()

            debug1(self.day_list)
            pg.display.flip()
            self.clock.tick(60)


graphic_interface = Graphic_interface()
graphic_interface.run()
