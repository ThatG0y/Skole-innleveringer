import pandas as pd
from klasser.produktklasser.eple import Eple
from klasser.produktklasser.mel import Mel


class App:
    def __init__(self) -> None:
        self.vareoversikt = self.lag_vareoversikt()

    def lag_vareoversikt(self) -> list[Eple | Mel]:
        liste = []
        data = pd.read_csv(r"vareoversikter\vareoversikt_barlind.csv", index_col=[0])
        for vare in data.iterrows():
            if vare[0] in ("Eple"):
                liste.append(Eple.from_series(vare))
            elif vare[0] in ("Mel"):
                liste.append(Mel.from_series(vare))
            else:
                print("Error")

    def bruker_grensesnitt(self) -> None:
        print("Leverandørshiz")
        print()
        print("1 Registrer ny bestilling")
        print("2 Vis total bestillingskostnad ")

    def vis_vareoversikt(self):
        print(f"Produkter:")
        for vare in self.vareoversikt:
            if vare.type in ("Eple"):
                print(
                    f"{vare.type} med navn {vare.navn} har farge {vare.farge} og koster {vare.kg_pris},00 kr per/kg"
                )
            elif vare.type in ("Mel"):
                print(
                    f"{vare.type} med navn {vare.navn} går ut på dato {vare.best_før} og koster {vare.kg_pris},00 kr per/kg"
                )
            else:
                print("error")

    def run(self) -> None:
        pass

    def bestill(self):
        pass
