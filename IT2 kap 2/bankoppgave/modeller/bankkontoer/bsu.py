from modeller.eier import Eier
from modeller.bankkontoer.bankkonto import BankKonto


class BSUKonto(BankKonto):
    """En underklasse av BankKonto. Klassen representerer en bsukonto i et banksystem.

    Attributes
    ----------
    maksÅrligSaldo : float
        Den maksimale saldoen som kontoen lar brukeren legge til på kontoen.
    gjennværendeSaldo : float
        Den gjennværende saldoen som kontoen lar brukeren legge til på kontoen.
    eier : Eier
        Et Eier-objekt som inneholder informasjon om eieren.
    kontonummer : str
        Bankkontoens kontonummer
    saldo : float = 0
        Bankkontoens saldo. Satt til 0 by default for at kontoen skal genereres uten penger på saldoen.
    """

    __MAKS_ÅRLIG_SALDO = 5500

    def __init__(self, eier: Eier, kontonummer: str, saldo: float = 0) -> None:
        """Konstruerer tilstanden til bsukonto-objektet.

        Parameters
        ----------
        eier : Eier
            Et Eier-objekt som inneholder informasjon om eieren.
        kontonummer : str
            Bankkontoens kontonummer
        saldo : float = 0
            Bankkontoens saldo. Satt til 0 by defult for at kontoen skal genereres uten penger på saldoen.
        """
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
        """Viser mengden kroner brukeren har til gode å sette inn."""
        print(f"Gjennværende innskudd (kr) : {self._gjennværendeSaldo}")

    def settInnPenger(self, penger: float) -> bool:
        if self._gjennværendeSaldo >= penger:
            self._gjennværendeSaldo -= penger
            return super().settInnPenger(penger)
        print(f"Du prøver å sette inn {penger}")
        print(f"Du kan kun sette inn {self._gjennværendeSaldo}")
        print(f"Saldoen er {self._saldo}")
        print("")
