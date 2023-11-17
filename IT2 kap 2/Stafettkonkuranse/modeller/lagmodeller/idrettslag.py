from modeller.medlemsmodeller.jente import Jente
from modeller.medlemsmodeller.gutt import Gutt


class Idrettslag:
    def __init__(
        self, lagnavn: str, medlemslisteJente: list[Jente], medlemslisteGutt: list[Gutt]
    ) -> None:
        self.lagnavn = lagnavn
        self.medlemslisteJente = medlemslisteJente
        self.medlemslisteGutt = medlemslisteGutt

    def beregnTotalRundetid(self) -> float:
        totalMedlemsliste = self.medlemslisteGutt + self.medlemslisteJente
        totalRundetid = 0
        for medlem in totalMedlemsliste:
            print(f"{medlem.navn} løper 100 m på {medlem.rundetid} sekunder")
            totalRundetid += medlem.rundetid
        print("")
        print(f"Lag {self.lagnavn} løper 4x100 m på {totalRundetid} sekunder tilsammen")
        print("")
        return totalRundetid

    def visLagInfo(self) -> None:
        totalMedlemsListe = self.medlemslisteJente + self.medlemslisteGutt
        print(f"Lag {self.lagnavn} består av følgende medlemmer:")
        for medlem in totalMedlemsListe:
            print(f"{medlem.navn:10} : {medlem.rundetid:5} sekunder")
        print("")
