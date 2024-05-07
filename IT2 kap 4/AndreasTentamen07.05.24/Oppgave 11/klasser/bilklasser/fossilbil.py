from klasser.bilklasser.bil import Bil


class Fossilbil(Bil):
    def __init__(
        self,
        modell: str,
        registreringsnummer: str,
        pris: float,
        bensin_per_km: int,
        tank: int,
        drivstoff_mengde: int,
    ) -> None:
        super().__init__("Fossilbil", modell, registreringsnummer, pris)
        self.bensin_per_km = bensin_per_km
        self.tank = tank
        self.drivstoff_mengde = drivstoff_mengde

    def __str__(self) -> str:
        return f"""{super().__str__()}
Bensin per km:      {self.bensin_per_km}
Tank:               {self.tank}
Drivstoff mengde:   {self.drivstoff_mengde}
"""
