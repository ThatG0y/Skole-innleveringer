import pygame as pg


# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE = 500
BILDER_PER_SEKUND = 24
# Initialiserer/starter pygame
pg.init()
vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
pg.display.set_caption("hjelp meg på ekte liksom")
clock = pg.time.Clock()
fortsett = True


class Ball:
    """Klasse for å representere en ball"""

    def __init__(self, x, y, fart, akselerasjon, radius, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.fart = fart
        self.akselerasjon = akselerasjon
        self.radius = radius
        self.vindusobjekt = vindusobjekt

    def tegn(self):
        """Metode for å tegne ballen"""
        pg.draw.circle(self.vindusobjekt, (255, 69, 0), (self.x, self.y), self.radius)

    def flytt(self):
        """Metode for å flytte ballen"""
        # Sjekker om ballen er utenfor høyre/venstre kant
        if ((self.y - self.radius) <= 0) or (
            (self.y + self.radius) >= self.vindusobjekt.get_height()
        ):
            self.fart = -self.fart
        self.fart += self.akselerasjon

        # Flytter ballen
        self.y += self.fart


# Lager et Ball-objekt
ball = Ball(250, 250, 0.1, 0.981, 20, vindu)

# Gjenta helt til brukeren lukker vinduet
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner og flytter ballen
    ball.tegn()
    ball.flytt()

    # Oppdaterer alt innholdet i vinduet
    pg.display.update()
    clock.tick(BILDER_PER_SEKUND)

# Avslutter pygame
pg.quit()
