from klasser.bestillingsklasser.bestillingvare import BestillingVare
from klasser.person import Person


class Bestilling:
    def __init__(self, kunde: Person) -> None:
        self.kunde = kunde
        self.handlekurv = []

    def __str__(self) -> str:
        print(f"Bestiller:      {self.kunde}")
        for vare in self.handlekurv:
            print(vare)
        return ""

    def legg_til_vare(self, vare: BestillingVare):
        self.handlekurv.append(vare)

    def beregn_total_pris(self) -> int:
        return sum([vare.beregn_pris() for vare in self.handlekurv])
