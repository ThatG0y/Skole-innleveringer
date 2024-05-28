from pydantic import BaseModel, Field


class Bruker(BaseModel):
    """Klasse som representerer en system-bruker"""

    navn: str = Field(alias="Navn")
    epost: str = Field(alias="E-post")
    tlf_nummer: int = Field(alias="Telefonnummer")

    def __str__(self) -> str:
        data = self.model_dump(by_alias=True)
        string = ""
        for nøkkel, verdi in data.items():
            string += f"{nøkkel}: {verdi}\n"

        return string

    def hent_info(self) -> None:
        """Metode for å vise informasjon om brukeren"""
        print(self)
