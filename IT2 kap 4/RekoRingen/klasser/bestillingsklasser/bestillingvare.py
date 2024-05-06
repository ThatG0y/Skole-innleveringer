from klasser.produktklasser.eple import Eple
from klasser.produktklasser.mel import Mel


class BestillingVare:
    def __init__(self, vare: Eple | Mel, antall_kg: int) -> None:
        self.vare = vare
        self.antall_kg = antall_kg

    def __str__(self) -> str:
        print(self.vare)
        return f"""Antall kg:   {self.antall_kg}"""

    def beregn_pris(self) -> int:
        return self.vare.kg_pris * self.antall_kg
