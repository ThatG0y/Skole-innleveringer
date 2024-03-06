import pygame as pg
import math as m
import random as rd
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from classes.bokser.boks import Boks
from classes.bokser.spiller import Spiller
from classes.bokser.matbit import Matbit
from classes.bokser.hinder import Hinder

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE = 500
BILDER_PER_SEKUND = 24


# Initialiserer/starter pygame
class App:
    def __init__(self) -> None:
        pg.init()
        self.vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
        pg.display.set_caption("PacTroll")
        self.clock = pg.time.Clock()
        self.fortsett = True
        self.spiller = Spiller(250, 250, self.vindu)
        self.matbiter = []
        for _ in range(3):
            self.matbiter.append(self.kokkeler_matbit(self.spiller, *self.matbiter))
        self.hinder = []
        self.counter = 0

    def kokkeler_matbit(self, *args):
        overlapp = True
        while overlapp:
            overlapp = False
            matbit = Matbit(self.vindu)
            for boks in args:
                if matbit.sjekk_overlapp(boks):
                    overlapp = True
                    break
        return matbit

    def sjekk_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.fortsett = False
        self.trykkede_taster = pg.key.get_pressed()

    def oppdater_tilstand(self):
        if self.trykkede_taster[K_UP]:
            self.spiller.retning = K_UP
        elif self.trykkede_taster[K_DOWN]:
            self.spiller.retning = K_DOWN
        elif self.trykkede_taster[K_RIGHT]:
            self.spiller.retning = K_RIGHT
        elif self.trykkede_taster[K_LEFT]:
            self.spiller.retning = K_LEFT

        self.spiller.gå_retning()

        for i, matbit in enumerate(
            self.matbiter
        ):  # sjekker om spiller overlapper med mat
            if self.spiller.sjekk_overlapp(matbit):
                self.hinder.append(Hinder(self.vindu, self.matbiter.pop(i)))
                self.matbiter.append(
                    self.kokkeler_matbit(self.spiller, *self.matbiter, *self.hinder)
                )
                self.counter += 1

        for hinder in self.hinder:
            if self.spiller.sjekk_overlapp(hinder):
                if hinder.farlig:
                    print("u lose")
                    print(f"Hjelp {self.counter}")
                    self.fortsett = False
            else:
                hinder.farlig = True

        # legg til death penalty for utenfor boundary
        # add death screen
        # add sprites
        # add score oversikt ingamge?

    @staticmethod
    def tegn_bokser(*args: Boks):
        for boks in args:
            boks.tegn()

    def tegn(self):
        self.vindu.fill((0, 0, 0))
        self.tegn_bokser(self.spiller, *self.matbiter, *self.hinder)
        pg.display.update()

    def run(self):
        while self.fortsett:
            self.sjekk_events()
            self.oppdater_tilstand()
            self.tegn()
            self.clock.tick(BILDER_PER_SEKUND)
        pg.quit()

    # Lager et Spiller-objekt
    # spiller = Spiller(200, 200, 20, (255, 69, 0), vindu, 0.1)
    # Lager et Hinder-objekt
    # hinder = Hinder(
    #     150, 250, 20, (0, 0, 255), vindu, rd.randint(1, 50) / 100, rd.randint(1, 50) / 100
    # ) 0.08, 0.12)
