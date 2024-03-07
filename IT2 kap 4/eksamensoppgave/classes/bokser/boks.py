from __future__ import (
    annotations,
)  # lar meg type-hinte klassen jeg skriver i (se linje 31)
import pygame as pg


class Boks:
    """Klasse for å representere en ball"""

    BREDDE = 40  # høyde og bredde for klosser
    HØYDE = 40

    def __init__(
        self, x: int, y: int, farge: tuple[int, int, int], vindusobjekt: pg.Surface
    ):
        """Konstruktør"""
        self.x = x  # posisjon og farge
        self.y = y
        self.farge = farge
        self.vindusobjekt = (
            vindusobjekt  # vindu trengs for visuell framstilling i pygame
        )

    def tegn(self) -> None:
        """Metode for å tegne boksen"""
        pg.draw.rect(  # tegner et rektangel
            self.vindusobjekt, self.farge, (self.x, self.y, self.BREDDE, self.HØYDE)
        )

    def sjekk_overlapp(
        self, annen_boks: Boks
    ) -> bool:  # sjekker om boksen overlapper med en annen boks
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
    def overlapp_intervall(a: int, b: int, c: int, d: int) -> bool:
        """Hjelpemetode for å sjekke om en boks overlapper med en annen boks"""
        if d <= a or b <= c:  # sjekker for overlappende intervaller
            return False
        else:
            return True
