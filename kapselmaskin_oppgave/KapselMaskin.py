class Drikke:  # Drikke-klasse lar oss lagre en drikkes navn og vannkriterie på samme sted. I tillegg lar den oss lagre hva drikken koster, som er relevant for oppgave 3. Default-verdi for "cost" er 0 fordi de fleste drikkene koster 0 kr.
    def __init__(self, navn: str, vannkriterie: int, cost: int = 0) -> None:
        self.navn = navn
        self.vannkriterie = vannkriterie
        self.cost = cost


class KapselMaskin:  # En kapselmaskin skal kunne lage drikker, og fylle seg selv opp med vann. Lar "produsent" angi størrelsen til vanntanken som parameter
    def __init__(self, makskapasitet: int):
        self.makskapasitet = (
            self.vannmengde
        ) = makskapasitet  # fyller opp vanntanken når maskinen blir startet (vannmengde = makskapasitet)

    def kanLageDrikke(
        self, drikke: Drikke
    ) -> (
        bool
    ):  # sjekker om en drikke kan bli laget. Tar utgangspunikt i vannmengden i vanntanken og vannkriterie for gitt drikke.
        """Sjekker om gitt drikke kan lages utifra vannmengden til KapselMaskinen

        Parameters
        ----------
        drikke : Drikke
            Et Drikke objekt som inneholder attributtene "navn" og "vannkriterie"

        Returns
        -------
        bool
            Returnerer True hvis drikken kan lages, False hvis drikken ikke kan lages
        """
        if self.vannmengde < drikke.vannkriterie:
            print(f"Det er ikke nok vann for en {drikke.navn}")
            print(f"Vannmengde: {self.vannmengde} ml")
            return False
        print(f"Det er nok vann for en {drikke.navn}")
        print(f"Vannmengde: {self.vannmengde-drikke.vannkriterie} ml")
        return True

    def fyllDrikke(
        self, drikke: Drikke
    ) -> (
        None
    ):  # reduserer vannmengden i tanken. Brukes sammen med kanLageDrikke for å simulere at en drikke blir tømt ut av maskinen.
        self.vannmengde -= drikke.vannkriterie

    def lagEspresso(
        self,
    ) -> (
        bool
    ):  # alle lag{drikke} funksjonene lager først et Drikke-objekt med relevant informasjon, og sjekker videre om det fins nok vann for at drikken kan lages.
        """Lager en espresso

        Returns
        -------
        bool
            Returnerer True hvis maskinen har nok vann for en espresso, eller False hvis maskinen ikke har nok vann for en espresso
        """
        espresso = Drikke("Espresso", 40)
        if self.kanLageDrikke(espresso):
            self.fyllDrikke(espresso)
        return self.kanLageDrikke(espresso)

    def lagLungo(self) -> bool:
        """Lager en lungo

        Returns
        -------
        bool
            Returnerer True hvis maskinen har nok vann for en lungo, eller False hvis maskinen ikke har nok vann for en lungo
        """
        lungo = Drikke("Lungo", 110)
        if self.kanLageDrikke(lungo):
            self.fyllDrikke(lungo)
        return self.kanLageDrikke(lungo)

    def fyllVann(
        self, ml: int = 0, maks: bool = True
    ) -> (
        int
    ):  # en funksjon for å fylle vanntanken til maskinen. Default-verdiene er gitt til ml = 0 og maks = True fordi man som regel vil fylle opp vanntanken til makskapasitet når man først fyller den. Om det er særdeles viktig for brukeren å fylle opp kun en viss mengde ml, kan man definere antall ml.
        """Fyller opp vanntanken til KapselMaskinen til makskapasitet eller en brukerdefinert mengde

        Parameters
        ----------
        ml : int, optional
            Antall ml bruker vil fylle på vanntanken, by default 0
        maks : bool, optional
            True hvis bruker vil fylle tanken til makskapasitet, by default True

        Returns
        -------
        int
            Vannmengden i vanntanken til KapselMaskinen
        """
        if (
            maks and ml == 0
        ):  # hvis ikke bruker har definert egen mengde vann -> mengde vann = full tank
            ml = self.makskapasitet - self.vannmengde
        if (
            ml + self.vannmengde > self.makskapasitet
        ):  # sjekker om det er plass i tanken
            print(
                f"Det er ikke plass i tanken for {ml} ml vann. Det er {self.vannmengde} ml i tanken fra før og det er plass til {self.makskapasitet} ml totalt"
            )
            return self.vannmengde
        self.vannmengde += ml
        print(
            f"Du har nå lagt til {ml} ml vann i tanken \nVannmengde: {self.vannmengde} ml"
        )
        return self.vannmengde

    def hentVannmengde(self) -> int:  # lar bruker sjekke vannmengden i kapselmaskinen
        return self.vannmengde


def unitTests() -> None:  # unittests
    maskin = KapselMaskin(1000)

    assert maskin.hentVannmengde() == 1000

    for _ in range(8):
        maskin.lagLungo()

    assert maskin.hentVannmengde() == 120

    maskin.lagEspresso()

    assert maskin.hentVannmengde() == 80

    maskin.lagLungo()

    assert maskin.hentVannmengde() == 80

    maskin.fyllVann(30, maks=False)

    assert maskin.hentVannmengde() == 110

    maskin.lagLungo()

    assert maskin.hentVannmengde() == 0


def main() -> None:
    unitTests()


if __name__ == "__main__":
    main()
