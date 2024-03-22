import pygame as pg
from pygame.locals import K_UP, K_DOWN, K_q, K_z, K_o, K_m
from classes.legemer.legeme import Legeme
from classes.legemer.spiller import Spiller


class App:

    VINDU_BREDDE = 1000  # størrelsen til spill-vinduet
    VINDU_HOYDE = 650
    BILDER_PER_SEKUND = 24  # bildefrekvens

    def __init__(self) -> None:
        """Konstruktør"""
        pg.init()
        pg.display.set_caption("Pong")

        self.vindu = pg.display.set_mode((self.VINDU_BREDDE, self.VINDU_HOYDE))
        self.clock = pg.time.Clock()
        self.fortsett = True

        # generer nødvendige objekter
        self.spiller = Spiller(
            int(self.VINDU_BREDDE / 2), int(self.VINDU_HOYDE / 2), self.vindu
        )
        self.matbiter = []
        for _ in range(3):
            self.matbiter.append(self.lag_matbit(self.spiller, *self.matbiter))
        self.hinder = []
        self.counter = Counter(self.vindu)

    def lag_matbit(self, *args) -> Matbit:
        """Metode for å lage et nytt Matbit-objekt"""
        overlapp = True
        while overlapp:  # logikk for å ikke få overlappende figurer
            overlapp = False
            matbit = Matbit(self.vindu)
            for boks in args:
                if matbit.sjekk_overlapp(boks):
                    overlapp = True
                    break
        return matbit

    def sjekk_events(self):
        """Metode for å sjekke etter utløste events"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.fortsett = False
        self.trykkede_taster = pg.key.get_pressed()

    def oppdater_tilstand(self):
        """Metode for å endre spillets tilstand"""
        # endrer retningen til spilleren utifra tastetrykk
        if self.trykkede_taster[K_UP] or self.trykkede_taster[K_w]:
            self.spiller.endre_retning(K_UP)
        elif self.trykkede_taster[K_DOWN] or self.trykkede_taster[K_s]:
            self.spiller.endre_retning(K_DOWN)
        elif self.trykkede_taster[K_RIGHT] or self.trykkede_taster[K_d]:
            self.spiller.endre_retning(K_RIGHT)
        elif self.trykkede_taster[K_LEFT] or self.trykkede_taster[K_a]:
            self.spiller.endre_retning(K_LEFT)

        self.spiller.gå_retning()

        for i, matbit in enumerate(
            self.matbiter
        ):  # sjekker om spiller overlapper med mat
            if self.spiller.sjekk_overlapp(matbit):
                self.hinder.append(Hinder(self.vindu, self.matbiter.pop(i)))
                self.matbiter.append(
                    self.lag_matbit(self.spiller, *self.matbiter, *self.hinder)
                )
                self.counter.value += 1
                self.spiller.øk_hastighet()

        for hinder in self.hinder:  # sjekker om spilleren har truffet et hinder
            if self.spiller.sjekk_overlapp(hinder):
                if hinder.farlig:
                    print("Spillet er over")
                    print(f"Du fikk følgende score: {self.counter.value}")
                    self.fortsett = False
            else:
                hinder.farlig = True

        if not (  # sjekker om spiller har truffet kanten av vinduet
            0 <= self.spiller.x <= self.VINDU_BREDDE - self.spiller.BREDDE
        ) or not (0 <= self.spiller.y <= self.VINDU_HOYDE - self.spiller.HØYDE):
            print("Spillet er over")
            print(f"Du fikk følgende score: {self.counter.value}")
            self.fortsett = False

    @staticmethod
    def tegn_bokser(*args: Legeme):
        """Metode for å tegne alle boks-objekter i spillet"""
        for boks in args:
            boks.tegn()

    def tegn(self):
        """Metode for å tegne spillets nåværende tilstand"""
        self.vindu.fill((0, 0, 0))
        self.tegn_bokser(self.spiller, *self.matbiter, *self.hinder)
        self.counter.tegn()
        pg.display.update()

    def run(self):
        """Metode for å kjøre spillet"""
        while self.fortsett:
            self.sjekk_events()
            self.oppdater_tilstand()
            self.tegn()
            self.clock.tick(self.BILDER_PER_SEKUND)
        pg.quit()
