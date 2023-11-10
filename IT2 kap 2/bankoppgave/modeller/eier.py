class Eier:
    """En klasse som representerer en person som eier noe.

    Attributes
    ----------
    fornavn : str
        Fornavnet til personen.
    etternavn : str
        Etternavnet til personen.
    telefonnummer : int
        Telefonnummeret til personen.
    """

    def __init__(self, fornavn: str, etternavn: str, telefonnummer: str) -> None:
        """Konstruerer tilstanden til Eier-objektet.

        Parameters
        ----------
        fornavn : str
            Fornavnet til personen.
        etternavn : str
            Etternavnet til personen.
        telefonnummer : int
            Telefonnummeret til personen.
        """
        self._fornavn = fornavn.strip().title()
        self._etternavn = etternavn.strip().title()
        self._telefonnummer = telefonnummer

    def __str__(self) -> str:
        return f"""Eier:
    Navn            : {self.fulltNavn()} 
    Telefonnummer   : {self._telefonnummer}
    """

    def fulltNavn(self) -> str:
        """Viser eierens fulle navn."""
        return f"{self._fornavn} {self._etternavn}"

    def visInfo(self) -> str:
        """Viser eierens fornavn, etternavn og telefonnummer."""
        return self
