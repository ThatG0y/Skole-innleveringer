class Bil:
    def __init__(
        self, type: str, modell: str, registreringsnummer: str, pris: float
    ) -> None:
        self.type = type
        self.modell = modell
        self.registreringsnummer = registreringsnummer
        self.pris = pris

    def __str__(self) -> str:
        return f"""Type:           {self.type}
Modell:             {self.modell}
Reg.Nr:             {self.registreringsnummer}
Pris per km:        {self.modell}"""

    def hent_info(self) -> None:
        print(self)
