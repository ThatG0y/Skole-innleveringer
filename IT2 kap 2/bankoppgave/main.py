from unit_tests.eier_tests import unit_tests as eier_tests
from unit_tests.bankkonto_tests import unit_tests as konto_tests
from unit_tests.bsu_tests import unit_tests as bsu_tests
from unit_tests.sparekonto_tests import unit_tests as sparekonto_tests


# for UML sjekk master > UML-folder > Oppgave bank
def unit_tests() -> None:
    eier_tests()
    konto_tests()
    bsu_tests()
    sparekonto_tests()


def main() -> None:
    unit_tests()


if __name__ == "__main__":
    main()
