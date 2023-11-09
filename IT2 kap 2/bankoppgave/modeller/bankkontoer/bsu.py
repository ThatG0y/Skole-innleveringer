from modeller.eier import Eier
from modeller.bankkontoer.bankkonto import BankKonto


class BSUKonto(BankKonto):
    __MAKS_ÅRLIG_SALDO = 5500

    def __init__(self, eier: Eier, kontonummer: str, saldo: float = 0) -> None:
        super().__init__(eier, kontonummer, saldo)
        self._gjennværendeSaldo = (
            self.__MAKS_ÅRLIG_SALDO
        )  # koden reduserer senere gjennværende saldo, siden saldo i seg selv kan være fra f. eks forrige år. i en total gjennomføring av koden vil koden legge til 1 makssaldo til gjennværende saldo 1 gang i året.

    @property
    def gjennværendeSaldo(self):
        return self._gjennværendeSaldo

    def __str__(self) -> str:
        print("BSU", end="")
        return super().__str__()

    def gjennværendeInnskudd(self) -> None:
        print(f"Gjennværende innskudd (kr) : {self._gjennværendeSaldo}")

    def settInnPenger(self, penger: float) -> bool:
        if self._gjennværendeSaldo >= penger:
            self._gjennværendeSaldo -= penger
            return super().settInnPenger(penger)
        print(f"Du prøver å sette inn {penger}")
        print(f"Du kan kun sette inn {self._gjennværendeSaldo}")
        print(f"Saldoen er {self._saldo}")
        print("")
