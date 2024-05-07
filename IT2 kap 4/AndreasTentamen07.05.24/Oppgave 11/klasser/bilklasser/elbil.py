from klasser.bilklasser.bil import Bil


class Elbil(Bil):
    def __init__(
        self,
        modell: str,
        registreringsnummer: str,
        pris: float,
        wh_per_km: int,
        batteri: int,
        energinivå: int,
    ) -> None:
        super().__init__("Elbil", modell, registreringsnummer, pris)
        self.wh_per_km = wh_per_km
        self.batteri = batteri
        self.energinivå = energinivå

    def __str__(self) -> str:
        return f"""{super().__str__()}
Wh per km:          {self.wh_per_km}
Batteri:            {self.batteri}
Energinivå:         {self.energinivå}
"""
