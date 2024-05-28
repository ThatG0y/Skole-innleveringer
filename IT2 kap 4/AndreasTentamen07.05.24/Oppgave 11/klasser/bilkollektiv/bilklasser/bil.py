from pydantic import BaseModel, Field


class Bil(BaseModel):
    """Klasse som representerer en bil"""

    type: str = Field(alias="Type")
    modell: str = Field(alias="Modell")
    registreringsnummer: str = Field(alias="Registreringsnummer")
    pris_per_km: float = Field(alias="Pris per km")

    def __str__(self) -> str:
        data = self.model_dump(by_alias=True)
        string = ""
        for nøkkel, verdi in data.items():
            string += f"{nøkkel}: {verdi}\n"

        return string

    def hent_info(self) -> None:
        """Metode for å vise bil-informasjon"""
        print(self)
