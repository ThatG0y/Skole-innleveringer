from utils.utils import navnelisteGutter as g
from utils.utils import navnelisteJenter as j
from modeller.lagmodeller.idrettsklubb import Idrettsklubb
from modeller.lagmodeller.idrettslag import Idrettslag
from modeller.medlemsmodeller.gutt import Gutt
from modeller.medlemsmodeller.jente import Jente


def unitTestsMedlem() -> None:
    pass


def unitTestsLag() -> None:
    lag = Idrettslag()


def unitTestsKlubb() -> None:
    klubb = Idrettsklubb()
    klubb.finnRaskestLag()


def unitTests() -> None:
    unitTestsMedlem()
    unitTestsLag()
    unitTestsKlubb()


def main() -> None:
    unitTests()


if __name__ == "__main__":
    main()
