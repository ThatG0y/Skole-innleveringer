from modeller.medlemsmodeller.jente import Jente
from modeller.medlemsmodeller.gutt import Gutt
from modeller.lagmodeller.idrettslag import Idrettslag
import random as rd
from utils.utils import navnelisteGutter as g, navnelisteJenter as j


class Idrettsklubb:
    def __init__(self) -> None:
        self.medlemslisteJenter = [Jente(j[_]) for _ in range(5)]
        self.medlemslisteGutter = [Gutt(g[_]) for _ in range(5)]
        self.spektatorer = []
        self.idrettslag = self.opprettIdrettslag()

    def opprettSpektatorer(
        self, medlemslisteJenter: list[Jente], medlemslisteGutter: list[Gutt]
    ) -> list[list[Jente], list[Gutt]]:
        self.spektatorer.append(medlemslisteJenter.pop(rd.randint(0, 4)))
        self.spektatorer.append(medlemslisteGutter.pop(rd.randint(0, 4)))

        return [medlemslisteJenter, medlemslisteGutter]

    def opprettIdrettslag(self) -> None:
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
            f"Det raskeste laget er derfor Lag {max(lagDict, key=lagDict.get)} med den totale rundetiden {max(lagDict.values())}\n"
        )

    def visKlubbInfo(self) -> None:
        for lag in self.idrettslag:
            lag.visLagInfo()
        print("Spektatorer består av følgende medlemmer:")
        for spektator in self.spektatorer:
            print(spektator.navn)
