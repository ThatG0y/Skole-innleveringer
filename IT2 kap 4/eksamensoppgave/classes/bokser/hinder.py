from classes.bokser.boks import Boks
from classes.bokser.matbit import Matbit
import pygame as pg


class Hinder(Boks):
    def __init__(self, vindusobjekt: pg.Surface, matbit: Matbit):
        super().__init__(matbit.x, matbit.y, (155, 155, 155), vindusobjekt)
        self.farlig = False  # brukes nåt overlapp mellom spiller og hinder sjekkes
