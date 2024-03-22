from classes.legemer.legeme import Legeme
import pygame as pg
import random as rd


class Ball(Legeme):
    def __init__(self, vindusobjekt: pg.Surface) -> None:
        self.fart_x = 8
        self.fart_y = rd.randint(-8, 8)
        super().__init__(250, 250, 10, 10, (0, 255, 0), vindusobjekt)

    def motsatt_retning_x(self) -> None:
        self.fart_x = -self.fart_x

    def motsatt_retning_y(self) -> None:
        self.fart_y = -self.fart_y

    def tilfeldig_fart_y(self) -> None:
        self.fart_y = rd.randint(-8, 8)

    def gå_retning(self) -> None:
        self.x += self.fart_x
        self.y += self.fart_y
