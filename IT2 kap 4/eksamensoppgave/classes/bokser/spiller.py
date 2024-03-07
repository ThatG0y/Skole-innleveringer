from classes.bokser.boks import Boks
import pygame as pg
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT


class Spiller(Boks):
    def __init__(self, x: int, y: int, vindusobjekt: pg.Surface):
        super().__init__(x, y, (0, 255, 0), vindusobjekt)
        self.fart = 5  # fart og retning for spillerens startsbevegelse
        self.retning = K_RIGHT

    def gå_retning(self) -> None:
        """Metode for å endre spillerens posisjon"""
        if self.retning == K_UP:
            self.y -= self.fart
        elif self.retning == K_DOWN:
            self.y += self.fart
        elif self.retning == K_LEFT:
            self.x -= self.fart
        elif self.retning == K_RIGHT:
            self.x += self.fart

    def endre_retning(self, retning) -> None:
        """Metode for å endre spillerens fartsretning"""
        self.retning = retning

    def øk_hastighet(self) -> None:
        """Metode for å endre spillerens fart"""
        self.fart += 0.5
