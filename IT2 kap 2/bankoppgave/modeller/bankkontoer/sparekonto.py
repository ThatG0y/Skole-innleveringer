from modeller.eier import Eier
from modeller.bankkontoer.bankkonto import BankKonto


class SpareKonto(BankKonto):
    __MAKS_ANTALL_ÅRLIGE_UTTAK = 10

    def __init__(
        self,
        eier: Eier,
        kontonummer: str,
        saldo: float = 0,
    ) -> None:
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
