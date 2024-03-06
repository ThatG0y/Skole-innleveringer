from classes.bokser.boks import Boks
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT


class Spiller(Boks):
    def __init__(self, x, y, vindusobjekt):
        super().__init__(x, y, (0, 255, 0), vindusobjekt)
        self.fart = 10
        self.retning = K_RIGHT

    def gå_retning(self):
        if self.retning == K_UP:
            self.y -= self.fart
        elif self.retning == K_DOWN:
            self.y += self.fart
        elif self.retning == K_LEFT:
            self.x -= self.fart
        elif self.retning == K_RIGHT:
            self.x += self.fart
