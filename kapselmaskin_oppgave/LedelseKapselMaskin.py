from KapselMaskin import KapselMaskin, Drikke


class LedelseKapselMaskin(
    KapselMaskin
):  # samme funksjonalitet som KapselMaskin, men flere drikker
    def __init__(self, makskapasitet: int = 1500):
        super().__init__(makskapasitet)

    def lagTe(self) -> bool:
        te = Drikke("Te", 200)
        if self.kanLageDrikke(te):
            self.fyllDrikke(te)

    def lagVann(self) -> bool:
        vann = Drikke("Vann", 150)
        if self.kanLageDrikke(vann):
            self.fyllDrikke(vann)


def unitTests() -> None:
    maskin = LedelseKapselMaskin()
    assert maskin.hentVannmengde() == 1500
    maskin.lagTe()
    assert maskin.hentVannmengde() == 1300
    for _ in range(9):
        maskin.lagVann()
    assert maskin.hentVannmengde() == 100


def main() -> None:
    unitTests()


if __name__ == "__main__":
    main()
