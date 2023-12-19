import pygame as pg
import pickle as kl
from debug import *
from Button import *
import sys

pg.init()


def get_font(size):
    return pg.font.Font(None, size)


class Graphic_interface:
    def __init__(self):
        self.day_1 = 200
        self.day_2 = 100
        self.day_3 = 200
        self.day_4 = 300
        self.day_5 = 400
        self.day_6 = 200
        self.day_7 = 400
        self.day_list = [self.day_1,self.day_2,self.day_3,self.day_4,self.day_5,self.day_6,self.day_7]
        self.screen = pg.display.set_mode((1280, 720))
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 30)
        self.bin = pg.image.load('graphics/U.png')
        self.info_percent = 540
        self.info_history = 500
        with open('list', 'rb') as f:
            self.day_list = kl.load(f)

    def run(self):
        while True:
            pg.draw.rect(self.screen, 'grey', pg.Rect(40, 40, 1200, 640))

            percentage_value = -(self.info_percent/2.7-200)
            self.screen.blit(self.bin,(700,250))
            pg.draw.rect(self.screen, 'brown', pg.Rect(765, self.info_percent, 260, 540 - self.info_percent))
            percentage = pg.font.Font(None, 60).render(f'{(str(round(percentage_value)))}%', True, 'White')
            self.screen.blit(percentage, (860, 610))

            pg.draw.rect(self.screen, 'black', pg.Rect(40,500, 580, 25))

            pg.draw.rect(self.screen, 'yellow', pg.Rect(60, self.day_list[0], 60,500 - self.day_list[0]))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(140, self.day_list[1], 60, 500 - self.day_list[1]))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(220, self.day_list[2], 60, 500 - self.day_list[2]))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(300, self.day_list[3], 60,500 - self.day_list[3] ))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(380, self.day_list[4], 60, 500 - self.day_list[4]))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(460, self.day_list[5], 60, 500 - self.day_list[5]))
            pg.draw.rect(self.screen, 'yellow', pg.Rect(540, self.info_history, 60, 500 - self.info_history))
            moyenne = ((500 - self.day_list[0] + 500 - self.day_list[1] +500 - self.day_list[2] +
                       500 - self.day_list[3] + 500 - self.day_list[4] + 500 - self.day_list[5] +
                       500 - self.day_list[6])/7)/10
            self.screen.blit(pg.font.Font(None, 40).render("Nombre d'ouvertures journalières", True, 'black'),
                             (50, 540))
            self.screen.blit(pg.font.Font(None, 40).render(f"Moyenne de cette semaine :{round(moyenne)} ", True, 'black'),
                             (50, 100))
            if moyenne < 5 :
                self.screen.blit(pg.font.Font(None, 40).render("Vous utilisez peu la poubelle", True, 'blue'),
                                 (50, 150))
            elif moyenne < 15 :
                self.screen.blit(pg.font.Font(None, 40).render("Vous utilisez modérement la poubelle", True, 'green'),
                                 (50, 150))
            elif moyenne < 25 :
                self.screen.blit(pg.font.Font(None, 40).render("Vous utilisez souvent la poubelle", True, 'orange'),
                                 (50, 150))
            else:
                self.screen.blit(pg.font.Font(None, 40).render("Vous êtes accro à la poubelle, consultez", True, 'red'),
                                 (50, 150))

            MOUSE_POS = pg.mouse.get_pos()
            RESET = Button(image=None, pos=(150, 650),
                           text_input="RESET", font=get_font(80), base_color="Black", hovering_color="Yellow")
            RESET.changeColor(MOUSE_POS)
            RESET.update(self.screen)

            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                self.day_list[6] -= 1
                self.info_percent -= 1
                self.info_history -= 10
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
                    pass
            debug1(self.day_list)
            pg.display.flip()
            self.clock.tick(60)


graphic_interface = Graphic_interface()
graphic_interface.run()
