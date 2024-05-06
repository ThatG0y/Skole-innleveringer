import pandas as pd


class Produkt:
    def __init__(self, navn: str, kg_pris: int) -> None:
        self.navn = navn
        self.kg_pris = kg_pris

    def __str__(self) -> str:
        return f"""Navn:        {self.navn}
Kilospris:        {self.kg_pris} kr"""

    @classmethod
    def from_series(cls, data: pd.Series):
        navn = data[1]["Name"]
        kg_pris = data[1]["Kilopris (kroner)"]
        return cls(navn, kg_pris)
