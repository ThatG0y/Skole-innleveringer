class Eier:
    def __init__(self, fornavn: str, etternavn: str, telefonnummer: str) -> None:
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
