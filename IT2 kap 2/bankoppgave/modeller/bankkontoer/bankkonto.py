from modeller.eier import Eier


class BankKonto:
    """En klasse som representerer en bankkonto i et banksystem.

    Attributes
    ----------
    eier : Eier
        Et Eier-objekt som inneholder informasjon om eieren.
    kontonummer : str
        Bankkontoens kontonummer
    saldo : float = 0
        Bankkontoens saldo. Satt til 0 by default for at kontoen skal genereres uten penger på saldoen.
    min_saldo : float
        En negativ minimumsverdi som saldoen kan synke til.
    """

    _min_saldo = -5000

    def __init__(self, eier: Eier, kontonummer: str, saldo: float = 0) -> None:
        """Konstruerer tilstanden til bankkonto-objektet.

        Parameters
        ----------
        eier : Eier
            Et Eier-objekt som inneholder informasjon om eieren.
        kontonummer : str
            Bankkontoens kontonummer
        saldo : float = 0
            Bankkontoens saldo. Satt til 0 by default for at kontoen skal genereres uten penger på saldoen.
        """
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
        """Viser relevant informasjon om eieren av bankkontoen"""
        print(self._eier)

    def visKontoInfo(self) -> None:
        """Viser relevant informasjon om bankkontoen"""
        print(self)

    def settInnPenger(self, penger: float) -> bool:
        """Lar brukeren sette inn et beløp penger på bankkontoens saldo.

        Parameters
        ----------
        penger : float
            Antallet kroner brukeren vil sette inn.

        Returns
        -------
        bool
            Returnerer True hvis transaksjonen var en suksess, returnerer ellers False.
        """
        print(f"Du satt inn {penger}")
        return self._transaksjon_funksjonalitet(penger)

    def taUtPenger(self, penger: float) -> bool:
        """Lar brukeren trekke fra et beløp penger fra bankkontoens saldo:

        Parameters
        ----------
        penger : float
            Antallet kroner brukeren vil trekke ut.

        Returns
        -------
        bool
            Returnerer True hvis transaksjonen var en suksess, returnerer ellers False.
        """
        if self._saldo - self._min_saldo > penger:
            print(f"Du tok ut {penger}")
            return self._transaksjon_funksjonalitet(-penger)
        print(f"Du prøver å ta ut {penger}")
        print("Ikke dekning på konto")
        print(f"Saldoen er {self._saldo}")
        print("")
        return False

    def _transaksjon_funksjonalitet(self, penger: float) -> bool:
        """Hjelpefunksjon for transaksjonsrelaterte metoder. Endrer beløpet på bankkontoens saldo.

        Parameters
        ----------
        penger : float
            Mengden penger som skal legges til / trekkes fra.

        Returns
        -------
        bool
            Returnerer True siden transaksjonen var en suksess.
        """
        self._saldo += penger
        print(f"Ny saldo er {self._saldo}")
        print("")
        return True
