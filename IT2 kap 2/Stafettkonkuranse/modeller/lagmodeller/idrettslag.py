from modeller.medlemsmodeller.jente import Jente
from modeller.medlemsmodeller.gutt import Gutt


class Idrettslag:
    """En klasse som representerer et idrettslag.

    Attributes
    ----------
    lagnavn : str
        Lagets navn
    medlemslisteJente: list[Jente]
        En liste med kvinnelige lagmedlemmer
    medlemslisteGutt: list[Gutt]
        En liste med mannlige lagmedlemmer
    """

    def __init__(
        self, lagnavn: str, medlemslisteJente: list[Jente], medlemslisteGutt: list[Gutt]
    ) -> None:
        """Konstruerer tilstanden til lag-objektet.

        Parameters
        ----------
        lagnavn : str
            Lagets navn
        medlemslisteJente: list[Jente]
            En liste med kvinnelige lagmedlemmer
        medlemslisteGutt: list[Gutt]
            En liste med mannlige lagmedlemmer
        """
        self.lagnavn = lagnavn
        self.medlemslisteJente = medlemslisteJente
        self.medlemslisteGutt = medlemslisteGutt

    def __str__(self) -> str:
        return f"""Idrettslag {self.lagnavn}:
    Medlemsliste    : {sorted([medlem.navn for medlem in [*self.medlemslisteJente + self.medlemslisteGutt]])}    
    """

    def beregnTotalRundetid(self) -> float:
        """Beregner den totale rundetiden til idrettslaget

        Returns
        -------
        float
            Den totale rundetiden til idrettslaget
        """
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
        """Viser lagets tilstand"""
        totalMedlemsListe = self.medlemslisteJente + self.medlemslisteGutt
        print(f"Lag {self.lagnavn} består av følgende medlemmer:")
        for medlem in totalMedlemsListe:
            print(f"{medlem.navn:10} : {medlem.rundetid:5} sekunder")
        print("")
