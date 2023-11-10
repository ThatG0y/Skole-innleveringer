from modeller.eier import Eier
from modeller.bankkontoer.bsu import BSUKonto


def unit_tests() -> None:
    konto = BSUKonto(Eier("Andreas", "Opdahl", "78678712"), "5130000032223")
    assert konto.saldo == 0, "saldoen er ikke satt til 0 ved opprettelse"
    konto.settInnPenger(1000)
    assert (
        konto.saldo == 1000.0
    ), "funksjonen 'sett_inn()' legger ikke til saldoer riktig"
    konto.settInnPenger(2000)
    assert (
        konto.saldo == 3000.0
    ), "funksjonen 'sett_inn()' legger ikke til saldoer riktig"
    konto.taUtPenger(1500)
    assert konto.saldo == 1500.0, "funksjonen 'ta_ut()' trekker ikke fra saldoen riktig"
    konto.taUtPenger(2500)
    assert (
        konto.saldo == -1000.0
    ), "funksjonen 'ta_ut()' trekker ikke fra saldoen riktig"
    konto.settInnPenger(2501)
    assert (
        konto.saldo == -1000.0
    ), "funksjonen 'sett_inn()' trekker ikke fra saldoen riktig i henhold til utvidet funksjonalitet"


if __name__ == "__main__":
    unit_tests()
