from classes.legemer.legeme import Legeme
import pygame as pg


class Ramme(Legeme):
    def __init__(self, vindusobjekt: pg.Surface):
        super().__init__(50, 200, 900, 450(0, 0, 0), vindusobjekt)
        self.farlig = False  # brukes nåt overlapp mellom spiller og hinder sjekkes

    def tegn(self):
        pg.draw.rect(
            self.vindusobjekt, (0, 255, 0), (self.x, self.y, self.bredde, self.høyde)
        )
        pg.draw.rect(
            self.vindusobjekt,
            (0, 0, 0),
            (self.x - 1, self.y - 1, self.bredde - 1, self.høyde - 1),
        )
