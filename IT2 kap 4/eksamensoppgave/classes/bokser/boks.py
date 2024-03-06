import pygame as pg
import math as m


class Boks:
    """Klasse for å representere en ball"""

    BREDDE = 40
    HØYDE = 40

    def __init__(self, x, y, farge, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.farge = farge
        self.vindusobjekt = vindusobjekt

    def tegn(self):
        """Metode for å tegne boksen"""
        pg.draw.rect(
            self.vindusobjekt, self.farge, (self.x, self.y, self.BREDDE, self.HØYDE)
        )

    def sjekk_overlapp(self, annen_boks):
        """Metode for å sjekke om en boks overlapper med en annen boks"""
        if self.overlapp_intervall(
            self.x, self.x + self.BREDDE, annen_boks.x, annen_boks.x + annen_boks.BREDDE
        ) and self.overlapp_intervall(
            self.y, self.y + self.HØYDE, annen_boks.y, annen_boks.y + annen_boks.HØYDE
        ):
            return True
        else:
            return False

    @staticmethod
    def overlapp_intervall(a, b, c, d):
        """Hjelpemetode for å sjekke om en boks overlapper med en annen boks"""
        if d <= a or b <= c:
            return False
        else:
            return True
