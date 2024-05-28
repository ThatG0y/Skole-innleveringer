from klasser.bilkollektiv.bilklasser.bil import Bil
from pydantic import Field


class Fossilbil(Bil):
    """Klasse som representerer en elbil"""

    bensin_per_km: float = Field(alias="Bensin per km")
    tank: int = Field(alias="Tank")
    drivstoffmengde: int = Field(alias="Drivstoffmengde")
