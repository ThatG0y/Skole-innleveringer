from pydantic import Field

from .modell_1 import Modell


class ArvModell2(Modell):
    """Modellerer enda en modell"""

    attributt: str = Field(alias="Thang")
