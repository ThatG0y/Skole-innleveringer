from utils.utils import navnelisteGutter as g
from utils.utils import navnelisteJenter as j
from modeller.lagmodeller.idrettsklubb import Idrettsklubb
from modeller.lagmodeller.idrettslag import Idrettslag
from modeller.medlemsmodeller.gutt import Gutt
from modeller.medlemsmodeller.jente import Jente


def unitTestsMedlem() -> None:
    kar = Gutt("Jens")
    karinne = Jente("Jenny")

    assert kar.navn == "Jens", "Navn blir ikke initialisert riktig for Gutt klassen"
    assert (
        karinne.navn == "Jenny"
    ), "Navn blir ikke initialisert riktig for Jente klassen"

    assert 11 <= kar.rundetid <= 13, "Gutt klassen genererer feil rundetid"
    assert 11.5 <= karinne.rundetid <= 13.5, "Jente klassen genererer feil rundetid"


def unitTestsLag() -> None:
    medlemsliste = [Jente(j[0]), Jente(j[1]), Gutt(g[0]), Gutt(g[1])]
    lag = Idrettslag("A", [*medlemsliste[:2]], [*medlemsliste[2:]])


def unitTestsKlubb() -> None:
    klubb = Idrettsklubb()
    klubb.finnRaskestLag()


def unitTests() -> None:
    unitTestsMedlem()
    unitTestsLag()
    unitTestsKlubb()
