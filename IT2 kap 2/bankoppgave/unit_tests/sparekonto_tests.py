from modeller.eier import Eier
from modeller.bankkontoer.sparekonto import SpareKonto


def unit_tests() -> None:
    konto = SpareKonto(Eier("Andreas", "Opdahl", "78678712"), "5130000032223", 5)
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
    for _ in range(4):
        konto.ta_ut(1)
    assert konto.saldo == -1003, "funksjonen 'ta_ut()' trekker ikke fra saldoen riktig"


if __name__ == "__main__":
    pass
