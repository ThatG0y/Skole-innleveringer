import pygame as pg


class Counter:
    def __init__(self, vindusobjekt: pg.Surface) -> None:
        """Konstruktør"""
        self.value = 0
        self.vindusobjekt = vindusobjekt
        self.font = pg.font.SysFont("Impact", 24)

    def tegn(self) -> None:
        """Metode for å tegne/skrive counter"""
        bilde = self.font.render(f"Poeng: {self.value}", True, (255, 255, 255))
        self.vindusobjekt.blit(
            bilde, (10, 10)
        )  # setter koordinaten til counter (øverst til venstre hjørne)
