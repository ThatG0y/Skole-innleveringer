from klasser.produktklasser.produkt import Produkt
import datetime
import pandas as pd


class Mel(Produkt):
    def __init__(self, navn: str, kg_pris: int, best_før: datetime.datetime) -> None:
        super().__init__(navn, kg_pris)
        self.best_før = best_før
        self.type = "Mel"

    def __str__(self) -> str:
        return f"""Type:        {self.type}
        {super().__str__()}"""

    @classmethod
    def from_series(cls, data: pd.Series):
        navn = data[1]["Name"]
        kg_pris = data[1]["Kilopris (kroner)"]
        best_før = data[1]["Best før"]
        return cls(navn, kg_pris, best_før)
