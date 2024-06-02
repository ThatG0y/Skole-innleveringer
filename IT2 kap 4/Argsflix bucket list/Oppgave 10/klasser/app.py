from klasser.modeller.modell_1 import Modell
from klasser.modeller.modell_2 import ArvModell
from klasser.modeller.modell_3 import ArvModell2
from klasser.datastruktur import DataStruktur


class App:
    def __init__(self) -> None:
        self.datastruktur = DataStruktur()

    def __str__(self) -> str:
        streng = f"Kjøper: {self.attribut} ({self.attributt2})\n"

        for ting in self.liste_ting:
            streng += f"{ting.attribut}\t({ting.attribut2} kg)\n"

        return streng

    def run(self) -> None:
        self.fortsett = True
        while self.fortsett:
            self.brukervalg()

    def brukervalg(self) -> None:
        self.brukergrensesnitt()
        valg = input("Hva vil du gjøre? ").lower()
        match valg:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "x":
                self.fortsett = False

    @staticmethod
    def brukergrensesnitt() -> None:
        print("1 Valg")
        print("2 Valg")
        print("3 Valg")
        print("4 Valg")
        print("X Avslutt")
