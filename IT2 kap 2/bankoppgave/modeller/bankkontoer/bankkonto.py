from modeller.eier import Eier


class BankKonto:
    _min_saldo = -5000

    def __init__(self, eier: Eier, kontonummer: str, saldo: float = 0) -> None:
        self._eier = eier
        self._kontonummer = kontonummer
        if saldo < self._min_saldo:
            raise ValueError("For lavt saldobeløp!")
        else:
            self._saldo = saldo
        print("Nyopprettet ", end="")
        print(self)

    def __str__(self) -> str:
        return f"""Konto:
    Eier        : {self._eier.fulltNavn()}
    Kontonummer : {self._kontonummer}
    Saldo       : {self._saldo:.2f}
    """

    @property
    def min_saldo(self):
        return self._min_saldo

    @property
    def eier(self):
        return self._eier

    @property
    def kontonummer(self):
        return self._kontonummer

    @property
    def saldo(self):
        return self._saldo

    # @saldo.setter
    # def saldo(self, ny_saldo):
    #     if ny_saldo < self.__MIN_SALDO:
    #         raise ValueError("For lavt saldobeløp!")
    #     else:
    #         self._saldo = ny_saldo

    def visEierInfo(self) -> None:
        print(self._eier)

    def visKontoInfo(self) -> None:
        print(self)

    def settInnPenger(self, penger: float) -> bool:
        print(f"Du satt inn {penger}")
        return self._transaksjon_funksjonalitet(penger)

    def taUtPenger(self, penger: float) -> bool:
        if self._saldo - self._min_saldo > penger:
            print(f"Du tok ut {penger}")
            return self._transaksjon_funksjonalitet(-penger)
        print(f"Du prøver å ta ut {penger}")
        print("Ikke dekning på konto")
        print(f"Saldoen er {self._saldo}")
        print("")
        return False

    def _transaksjon_funksjonalitet(self, penger: float) -> bool:
        self._saldo += penger
        print(f"Ny saldo er {self._saldo}")
        print("")
        return True
