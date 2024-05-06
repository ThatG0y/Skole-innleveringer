from klasser.produktklasser.produkt import Produkt
import pandas as pd


class Eple(Produkt):
    def __init__(self, navn: str, kg_pris: int, farge: str) -> None:
        super().__init__(navn, kg_pris)
        self.farge = farge
        self.type = "Eple"

    def __str__(self) -> str:
        return f"""Type:        {self.type}
        {super().__str__()}"""

    @classmethod
    def from_series(cls, data: pd.Series):
        navn = data[1]["Name"]
        kg_pris = data[1]["Kilopris (kroner)"]
        farge = data[1]["Farge"]
        return cls(navn, kg_pris, farge)
