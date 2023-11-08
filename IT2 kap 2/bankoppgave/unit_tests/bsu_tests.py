from modeller.eier import Eier
from modeller.bankkontoer.bsu import BSUKonto


def unit_tests() -> None:
    konto = BSUKonto(Eier("Andreas", "Opdahl", "78678712"), "5130000032223", 5000)
    assert konto.saldo == 0, "saldoen er ikke satt til 0 ved opprettelse"
    konto.sett_inn(1000)
    assert (
        konto.saldo == 1000.0
    ), "funksjonen 'sett_inn()' legger ikke til saldoer riktig"
    konto.sett_inn(2000)
    assert (
        konto.saldo == 3000.0
    ), "funksjonen 'sett_inn()' legger ikke til saldoer riktig"
    konto.ta_ut(1500)
    assert konto.saldo == 1500.0, "funksjonen 'ta_ut()' trekker ikke fra saldoen riktig"
    konto.ta_ut(2500)
    assert (
        konto.saldo == -1000.0
    ), "funksjonen 'ta_ut()' trekker ikke fra saldoen riktig"
    konto.sett_inn(2001)
    assert (
        konto.saldo == -1000.0
    ), "funksjonen 'sett_inn()' trekker ikke fra saldoen riktig i henhold til "


if __name__ == "__main__":
    pass
