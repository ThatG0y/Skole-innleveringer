from modeller.medlemsmodeller.medlem import Medlem
import random as rd


class Gutt(Medlem):
    """En klasse som representerer en gutt som er medlem av et idrettslag.

    Attributes
    ----------
    navn : str
        Lagmedlemets navn
    rundetid : float
        Hvor raskt lagmedlemmet løper 100 m
    """

    def __init__(self, navn: str) -> None:
        """Konstruerer tilstanden til gutt-lagmedlemsobjektet.

        Parameters
        ----------
        navn : str
            Lagmedlemets navn
        """
        super().__init__(navn)
        self.rundetid = rd.randint(110, 130) / 10
