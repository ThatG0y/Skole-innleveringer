from klasser.bilklasser.bil import Bil
from klasser.misc.medlem import Medlem
import datetime


class Reservasjon:
    def __init__(self, bil: Bil, medlem: Medlem, dato: datetime.datetime) -> None:
        self.bil = bil
        self.medlem = medlem
        self.dato = dato

    def __str__(self) -> str:
        return f"""Bil:         
    {self.bil}
Reservert av:           
    {self.medlem}
Dato:
    {self.dato}
"""

    def vis_info(self):
        print(self)
