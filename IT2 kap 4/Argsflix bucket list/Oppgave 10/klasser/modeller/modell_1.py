from pydantic import BaseModel, Field


class Modell(BaseModel):
    """Modellerer en modell"""

    attributt_1: str = Field(alias="Ting")
    attributt_2: int = Field(alias="Tang")

    def __str__(self) -> str:
        data = self.model_dump(by_alias=True)
        # streng = f"Type: {self.__class__.__name__}\n"
        streng = ""
        for nøkkel, verdi in data.items():
            streng += f"{nøkkel}: {verdi}\n"

        return streng
