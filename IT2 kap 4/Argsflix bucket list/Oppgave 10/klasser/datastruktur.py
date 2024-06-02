import json
from klasser.modeller.modell_1 import Modell
from klasser.modeller.modell_2 import ArvModell
from klasser.modeller.modell_3 import ArvModell2
from verktoy import absolutt_bane
from innstillinger import RELATIV_DATAFIL_BANE


class DataStruktur:
    """Klasse for å representere tilstand og hente data"""

    def __init__(self) -> None:
        self.pp = {}

        with open(
            absolutt_bane(RELATIV_DATAFIL_BANE), encoding="utf-8-sig"
        ) as data_fil:
            data = json.load(data_fil)

        for element in data:
            if element == "yo":
                self.pp["mama"] = "yes"
            elif element == "mama":
                self.pp["papa"] = "yes"

    def vis_biler(self) -> None:
        """Metode for å vise alle biler i bilparken"""
        for bil in self.biler.values():
            print(bil)

    def lagre_info(self) -> None:
        """Metode for å oppdatere informasjonen om bilene i bilparken"""
        json_data = [bil.model_dump(by_alias=True) for bil in self.biler.values()]

        with open(absolutt_bane(RELATIV_DATAFIL_BANE), "w") as bildata_fil:
            json.dump(json_data, bildata_fil)
