from pygame import Surface
from classes.legemer.spill_objekt import SpillObjekt

class Spøkelse(SpillObjekt):
    def __init__(self, x: int, y: int, farge: tuple[int, int, int], vindusobjekt: Surface):
        super().__init__(x, y, farge, vindusobjekt)