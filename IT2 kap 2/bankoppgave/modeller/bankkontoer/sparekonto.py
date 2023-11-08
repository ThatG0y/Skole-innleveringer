from modeller.eier import Eier
from modeller.bankkontoer.bankkonto import BankKonto


class SpareKonto(BankKonto):
    def __init__(
        self,
        eier: Eier,
        kontonummer: str,
        maks_antall_årlige_uttak: int,
        saldo: float = 0,
    ) -> None:
        super().__init__(eier, kontonummer, saldo)
        self._gjennværende_antall_uttak = maks_antall_årlige_uttak  # koden reduserer senere gjennværende_årlige_uttak, fullt utviklet kode burde legge til flere antall uttak 1 gang i året.

    @property
    def gjennværende_antall_uttak(self):
        return self._gjennværende_antall_uttak

    def __str__(self) -> str:
        print("Spare", end="")
        return super().__str__()

    def ta_ut(self, penger: int) -> bool:
        if self._gjennværende_antall_uttak < 1:
            print(f"Du prøver å ta ut {penger}")
            print("Du har ingen gjennstående uttak for denne terminen")
            print(f"Saldoen er {self._saldo}")
            return False
        if super().ta_ut(penger):
            self._gjennværende_antall_uttak -= 1
            return True
        return False


if __name__ == "__main__":
    pass
