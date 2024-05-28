from datetime import datetime
from klasser.reservasjonssystem.bruker import Bruker
from pydantic import BaseModel, Field


class Reservasjon(BaseModel):
    """Klasse for å representere en reservasjon i et reservasjonssystem"""

    reservasjon_ID: int = Field(alias="ReservasjonsID")
    bruker: Bruker = Field(alias="Bruker")
    registreringsnummer: str = Field(alias="Registreringsnummer")
    start_tid: datetime = Field(alias="Start tid")
    slutt_tid: datetime = Field(alias="Slutt tid")

    def __str__(self) -> str:
        data = self.model_dump(by_alias=True)
        string = ""
        for nøkkel, verdi in data.items():
            string += f"{nøkkel}: {verdi}\n"

        return string
