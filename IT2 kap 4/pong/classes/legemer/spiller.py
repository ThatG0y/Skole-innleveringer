from classes.legemer.legeme import Legeme
import pygame as pg
from pygame.locals import K_UP, K_DOWN


class Spiller(Legeme):
    def __init__(self, x: int, y: int, vindusobjekt: pg.Surface):
        super().__init__(x, y, 5, 40, (0, 255, 0), vindusobjekt)
        self.fart_y = 5  # fart og retning for spillerens startsbevegelse
        self.retning = None

    def gå_retning(self) -> None:
        """Metode for å endre spillerens posisjon"""
        if self.retning == K_UP:
            self.y -= self.fart_y
        elif self.retning == K_DOWN:
            self.y += self.fart_y

    def endre_retning(self, retning) -> None:
        """Metode for å endre spillerens fartsretning"""
        self.retning = retning
