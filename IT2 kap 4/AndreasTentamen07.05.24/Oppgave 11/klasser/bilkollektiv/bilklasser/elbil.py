from klasser.bilkollektiv.bilklasser.bil import Bil
from pydantic import Field


class Elbil(Bil):
    """Klasse som representerer en elbil"""

    wattimer_per_km: int = Field(alias="Watt-timer per km")
    batteri: int = Field(alias="Batteri")
    energinivå: int = Field(alias="Energinivå")
