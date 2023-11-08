from KapselMaskin import KapselMaskin, Drikke


class KunderKapselMaskin(
    KapselMaskin
):  # lager en subclass av KapselMaskin som lar kunder kjøpe espresso for penger, økt funksjonalitet for behandling av transaksjoner
    def __init__(
        self, makskapasitet: int = 1500
    ):  # Gir maskinen en  pengeoversikt. Pengeoversikten er kun for de midlertidige transaksjonene, ikke en oversikt over hvor mye maskinen har tjent totalt.
        super().__init__(makskapasitet)
        self.maskin_beløp = 0

    def fyllDrikke(
        self, drikke: Drikke
    ) -> (
        None
    ):  # samme funksjonalitet som i forelderklassen KapselMaskin, men gjør også bruker obs på om det er lite vann i tanken etter drikken blir tømt, og trekker drikke-kostnader fra maskinkontoen
        if self.vannmengde - drikke.vannkriterie <= 100:
            print("Det er 100 ml eller mindre i vanntanken")
        self.maskin_beløp -= drikke.cost
        return super().fyllDrikke(drikke)

    def lagEspresso(
        self,
    ) -> bool:  # økt funksjonalitet i henhold til drikke-kostnad og transaksjoner
        espresso = Drikke("Espresso", 40, cost=42)
        if espresso.cost > self.maskin_beløp:  # sjekker om det er nok penger i maskinen
            print(
                f"Kun {self.maskin_beløp} kr er satt inn, du trenger {espresso.cost} kr for en {espresso.navn}"
            )
            return False
        if self.kanLageDrikke(espresso):
            self.fyllDrikke(espresso)
            self.tilbakebetale()
            return True
        self.tilbakebetale()
        return False

    def mottaBetaling(self, beløp: int = 0) -> None:
        if (
            beløp == 0
        ):  # om det ikke er gitt noe beløp, eller beløpet er 0 spør koden etter input
            beløp = input("Vennligst sett inn penger: ")
        try:
            beløp = int(beløp)
            assert beløp in (1, 20, 50)  # akseptert valuta
        except AssertionError:
            print("Ugyldig valuta. Maskin aksepterer kun 50-lapp, 20-krone, og 1-krone")
            return None
        except ValueError:
            print("Ugyldig valuta. Maskin aksepterer kun 50-lapp, 20-krone, og 1-krone")
            return None
        print(f"Du har satt inn {beløp} kr")
        self.maskin_beløp += beløp

    def tilbakebetale(self) -> None:  # tømmer maskinkontoen
        if self.maskin_beløp <= 0:
            return None
        print(f"Her har du resten av pengene dine tilbake: {self.maskin_beløp} kr ")
        self.maskin_beløp = 0


def unitTests() -> None:
    maskin = KunderKapselMaskin()
    assert maskin.hentVannmengde() == 1500
    maskin.lagEspresso()
    assert maskin.hentVannmengde() == 1500
    for _ in range(12):
        maskin.mottaBetaling(1)
    maskin.mottaBetaling(20)
    assert maskin.maskin_beløp == 32
    maskin.lagEspresso()
    assert maskin.maskin_beløp == 32
    for _ in range(3):
        maskin.mottaBetaling(1)
        maskin.mottaBetaling(20)
    maskin.lagEspresso()
    assert maskin.maskin_beløp == 0
    assert maskin.hentVannmengde() == 1460
    for _ in range(13):
        maskin.lagLungo()
    maskin.mottaBetaling(50)
    maskin.lagEspresso()


def main() -> None:
    unitTests()


if __name__ == "__main__":
    main()
