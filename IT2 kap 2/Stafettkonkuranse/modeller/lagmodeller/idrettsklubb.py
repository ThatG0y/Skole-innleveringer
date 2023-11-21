from modeller.medlemsmodeller.jente import Jente
from modeller.medlemsmodeller.gutt import Gutt
from modeller.lagmodeller.idrettslag import Idrettslag
import random as rd
from utils.utils import navnelisteGutter as g, navnelisteJenter as j


class Idrettsklubb:
    """En klasse som representerer en idrettsklubb.

    Attributes
    ----------
    medlemslisteJente: list[Jente]
        En liste med kvinnelige lagmedlemmer
    medlemslisteGutt: list[Gutt]
        En liste med mannlige lagmedlemmer
    spektatorer : list[Gutt|Jente]
        En liste med spektatorer
    lagliste : liste[Idrettslag]
        En liste med klubbens lag
    """

    def __init__(self) -> None:
        """Konstruerer tilstanden til klubb-objektet."""
        self.medlemslisteJenter = [Jente(j[_]) for _ in range(5)]
        self.medlemslisteGutter = [Gutt(g[_]) for _ in range(5)]
        self.spektatorer = []
        self.idrettslag = self.opprettIdrettslag()

    def __str__(self) -> str:
        print(f"Idrettsklubb:")
        print(f"    Lagliste        : {[lag.lagnavn for lag in self.idrettslag]}")
        print("")
        for lag in self.idrettslag:
            print(lag)
        print(
            f"Spektatorer         : {[spektator.navn for spektator in self.spektatorer]}"
        )
        return ""

    def opprettSpektatorer(
        self, medlemslisteJenter: list[Jente], medlemslisteGutter: list[Gutt]
    ) -> list[list[Jente], list[Gutt]]:
        """Oppretter en liste med spektatorer av overflødige klubbmedlemmer

        Parameters
        ----------
        medlemslisteJenter : list[Jente]
            Klubbens medlemmsliste for jenter
        medlemslisteGutter : list[Gutt]
            Klubbens medlemmsliste for gutter

        Returns
        -------
        list[list[Jente], list[Gutt]]
            En oppdatert medlemsliste som ikke inneholder spekatorene
        """
        self.spektatorer.append(medlemslisteJenter.pop(rd.randint(0, 4)))
        self.spektatorer.append(medlemslisteGutter.pop(rd.randint(0, 4)))

        return [medlemslisteJenter, medlemslisteGutter]

    def opprettIdrettslag(self) -> list[Idrettslag, Idrettslag]:
        """Oppretter klubbens idrettslag

        Returns
        -------
        list[Idrettslag, Idrettslag]
            Returnerer klubbens to idrettslag

        """
        medlemslisteJenter, medlemslisteGutter = self.opprettSpektatorer(
            self.medlemslisteJenter[:], self.medlemslisteGutter[:]
        )
        medlemslisteJenter[rd.randint(0, len(medlemslisteJenter) - 1)].rundetid = 10
        medlemslisteGutter[rd.randint(0, len(medlemslisteGutter) - 1)].rundetid = 10
        halvMedlemslisteGutter = [
            medlemslisteGutter.pop(rd.randint(0, len(medlemslisteGutter) - 1))
            for _ in range(2)
        ]
        halvMedlemslisteJenter = [
            medlemslisteJenter.pop(rd.randint(0, len(medlemslisteJenter) - 1))
            for _ in range(2)
        ]
        return [
            Idrettslag("A", halvMedlemslisteJenter, halvMedlemslisteGutter),
            Idrettslag("B", medlemslisteJenter, medlemslisteGutter),
        ]

    def finnRaskestLag(self) -> None:
        """Beregner laget med lavest total rundetid"""
        lagDict = {lag.lagnavn: lag.beregnTotalRundetid() for lag in self.idrettslag}
        print(
            f"Det raskeste laget er derfor Lag {min(lagDict, key=lagDict.get)} med den totale rundetiden {min(lagDict.values())} sekunder\n"
        )

    def visKlubbInfo(self) -> None:
        """Viser klubbens lag, spektatorer, medlemmer og rundetider"""
        for lag in self.idrettslag:
            lag.visLagInfo()
        print("Spektatorer består av følgende medlemmer:")
        for spektator in self.spektatorer:
            print(spektator.navn)
        print("")
