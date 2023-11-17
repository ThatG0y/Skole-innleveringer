from modeller.medlemsmodeller.medlem import Medlem
import random as rd


class Gutt(Medlem):
    def __init__(self, navn: str) -> None:
        super().__init__(navn)
        self.rundetid = rd.randint(11, 13)
