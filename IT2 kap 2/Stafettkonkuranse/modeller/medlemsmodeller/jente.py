from modeller.medlemsmodeller.medlem import Medlem
import random as rd


class Jente(Medlem):
    """En klasse som representerer en jente som er medlem av et idrettslag.

    Attributes
    ----------
    navn : str
        Lagmedlemets navn
    rundetid : float
        Hvor raskt lagmedlemmet løper 100 m
    """

    def __init__(self, navn: str) -> None:
        """Konstruerer tilstanden til jente-lagmedlemsobjektet.

        Parameters
        ----------
        navn : str
            Lagmedlemets navn
        """
        super().__init__(navn)
        self.rundetid = rd.randint(115, 135) / 10
