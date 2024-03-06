from classes.bokser.boks import Boks
import pygame as pg
import random as rd


class Matbit(Boks):
    def __init__(self, vindusobjekt: pg.Surface):
        x = rd.randint(0, vindusobjekt.get_width() - self.BREDDE)
        y = rd.randint(0, vindusobjekt.get_height() - self.HØYDE)
        super().__init__(x, y, (255, 255, 0), vindusobjekt)
