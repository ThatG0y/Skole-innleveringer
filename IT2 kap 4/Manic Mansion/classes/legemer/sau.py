from classes.legemer.spill_objekt import SpillObjekt
import pygame as pg
import random as rd


class Sau(SpillObjekt):
    def __init__(self, vindusobjekt: pg.Surface):
        x = rd.randint(
            0, vindusobjekt.get_width() - self.BREDDE
        )  # tilfeldig koordinat i vinduet
        y = rd.randint(0, vindusobjekt.get_height() - self.HØYDE)
        super().__init__(x, y, (255, 255, 0), vindusobjekt)
