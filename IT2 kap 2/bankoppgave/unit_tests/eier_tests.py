from modeller.eier import Eier


def unit_tests() -> None:
    eier = Eier("Andreas", "Opdahl", "78678712")
    assert eier.fulltNavn() == "Andreas Opdahl", "Navn ble ikke initialisert riktig"
    assert eier.telefonnummer() == "78678712", "Telefonnummer er ikke riktig"


if __name__ == "__main__":
    pass
