import os
import json


class Bucketlist:
    """Klasse for å representere en samling filmer/serier"""

    def __init__(self, navn: str) -> None:
        self.endre_bruker(navn)
        self._oppdater_bucketlist()

    def legg_til_favoritt(self, film: dict) -> None:
        """Metode for å legge til en media i bucketlist"""
        film["Sett"] = False
        for media in self.favoritter:
            if media["imdbID"] == film["imdbID"]:
                return None
        self.favoritter.append(film)
        self._oppdater_bucketlist()

    def endre_bruker(self, navn: str) -> None:
        """Metode for å endre gjeldende bruker"""
        self.navn = navn
        self.adresse = os.path.join(
            os.path.abspath(os.path.dirname("")),
            r"bucketlists\{}.json".format("".join(self.navn.split()).strip().lower()),
        )
        self.favoritter = self._hent_bucketlist()

    def _fins_lagret_bucketlist(self) -> bool:
        """Hjelpemetode for å sjekke etter lagret brukerinformasjon"""
        try:
            with open(self.adresse, "x"):
                return False
        except FileExistsError:
            return True

    def _hent_bucketlist(self) -> list[dict]:
        """Hjelpemetode for å hente lagret brukerinformasjon"""
        if self._fins_lagret_bucketlist():
            with open(self.adresse, "r") as data:
                return json.load(data)["Favoritter"]
        else:
            return []

    def _oppdater_bucketlist(self) -> None:
        """Hjelpemetode for å oppdatere en json-fil etter bucketlistens tilstand"""
        with open(self.adresse, "w") as json_fil:
            json.dump({"Favoritter": self.favoritter}, json_fil, indent=4)

    def marker_sett(self, imdb_id: str) -> None:
        """Metode for å markere et gitt media i bucketlisten som "sett" """
        for film in self.favoritter:
            if film["imdbID"] == imdb_id:
                film["Sett"] = True
        self._oppdater_bucketlist()

    def fjern_favoritt(self, imdb_id: str) -> None:
        """Metode for å fjerne et media fra bucektlisten"""
        for index, film in enumerate(self.favoritter):
            if film["imdbID"] == imdb_id:
                self.favoritter.pop(index)
        self._oppdater_bucketlist()
