from modeller.eier import Eier
from modeller.bankkontoer.bankkonto import BankKonto


class SpareKonto(BankKonto):
    """En underklasse av BankKonto. Klassen representerer en sparekonto i et banksystem.

    Attributes
    ----------
    maksAntallÅrligeUttak : int
        Det maksimale antallet uttak som kontoen lar brukeren ta ut fra kontoen.
    gjennværendeAntallUttak : int
        Det gjennværende antallet uttak som kontoen lar brukeren ta ut fra kontoen.
    eier : Eier
        Et Eier-objekt som inneholder informasjon om eieren.
    kontonummer : str
        Bankkontoens kontonummer
    saldo : float = 0
        Bankkontoens saldo. Satt til 0 by default for at kontoen skal genereres uten penger på saldoen.
    """

    __MAKS_ANTALL_ÅRLIGE_UTTAK = 10

    def __init__(
        self,
        eier: Eier,
        kontonummer: str,
        saldo: float = 0,
    ) -> None:
        """Konstruerer tilstanden til sparekonto-objektet.

        Parameters
        ----------
        eier : Eier
            Et Eier-objekt som inneholder informasjon om eieren.
        kontonummer : str
            Bankkontoens kontonummer
        saldo : float = 0
            Bankkontoens saldo. Satt til 0 by default for at kontoen skal genereres uten penger på saldoen.
        """
        super().__init__(eier, kontonummer, saldo)
        self._gjennværendeAntallUttak = (
            self.__MAKS_ANTALL_ÅRLIGE_UTTAK
        )  # koden reduserer senere gjennværende årlige uttak, fullt utviklet kode burde legge til flere antall uttak 1 gang i året.

    @property
    def gjennværendeAntallUttak(self):
        return self._gjennværendeAntallUttak

    def __str__(self) -> str:
        print("Spare", end="")
        return super().__str__()

    def gjennværendeUttak(self) -> None:
        """Viser antallet pengeuttak brukeren har til gode."""
        print(f"Gjennværende uttak : {self._gjennværendeAntallUttak}")

    def taUtPenger(self, penger: float) -> bool:
        if self._gjennværendeAntallUttak < 1:
            print(f"Du prøver å ta ut {penger}")
            print("Du har ingen gjennværennde uttak for denne terminen")
            print(f"Saldoen er {self._saldo}")
            return False
        if super().taUtPenger(penger):
            self._gjennværendeAntallUttak -= 1
            return True
        return False
