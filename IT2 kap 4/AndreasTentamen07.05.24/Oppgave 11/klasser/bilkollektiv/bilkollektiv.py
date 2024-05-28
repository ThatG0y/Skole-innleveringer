import json
from klasser.bilkollektiv.bilklasser.bil import Bil
from klasser.bilkollektiv.bilklasser.elbil import Elbil
from klasser.bilkollektiv.bilklasser.fossilbil import Fossilbil
from settings import bilkollektiv_data_path


class BilKollektiv:
    """Klasse for å representere et bilkollektiv"""

    def __init__(self) -> None:
        self.biler: dict[str, Bil] = {}

        with open(bilkollektiv_data_path, encoding="utf-8-sig") as bildata_fil:
            data = json.load(bildata_fil)

        for bil in data:
            if bil["Type"] == "Elbil":
                self.biler[bil["Registreringsnummer"]] = Elbil(**bil)
            elif bil["Type"] == "Fossil":
                self.biler[bil["Registreringsnummer"]] = Fossilbil(**bil)

    def vis_biler(self) -> None:
        """Metode for å vise alle biler i bilparken"""
        for bil in self.biler.values():
            print(bil)

    def lagre_info(self) -> None:
        """Metode for å oppdatere informasjonen om bilene i bilparken"""
        json_data = [bil.model_dump(by_alias=True) for bil in self.biler.values()]

        with open(bilkollektiv_data_path, "w") as bildata_fil:
            json.dump(json_data, bildata_fil)
