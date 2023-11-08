from modeller.eier import Eier
from modeller.bankkontoer.bankkonto import BankKonto


class BSUKonto(BankKonto):
    def __init__(
        self, eier: Eier, kontonummer: str, maks_årlig_saldo: int, saldo: float = 0
    ) -> None:
        super().__init__(eier, kontonummer, saldo)
        self._gjennværende_saldo = maks_årlig_saldo  # koden reduserer senere gjennværende_saldo, siden saldo i seg selv kan være fra f. eks forrige år. i en total gjennomføring av koden vil koden legge til 1 makssaldo til gjennværende_saldo 1 gang i året.

    @property
    def gjennværende_saldo(self):
        return self._gjennværende_saldo

    def __str__(self) -> str:
        print("BSU", end="")
        return super().__str__()

    def sett_inn(self, penger: int) -> bool:
        if self._gjennværende_saldo >= penger:
            self._gjennværende_saldo -= penger
            return super().sett_inn(penger)
        print(f"Du prøver å sette inn {penger}")
        print(f"Du kan bare sette inn {self._gjennværende_saldo}")
        print(f"Saldoen er {self._saldo}")
        print("")


if __name__ == "__main__":
    pass
