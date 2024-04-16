import requests as req
from classes.søk_klasser.søkeresultat import Søkeresultat
from classes.filmklasser.film import Film
from classes.filmklasser.serie import Serie
from utils.settings import API_KEY
import json
import os


class Søk:
    """Klasse for å enkapsulere søkeinformasjon og søkefunksjonalitet"""

    def __init__(self) -> None:
        self.forrige_søk = []
        self.forrige_media = None
        self.api_key = API_KEY

    def hent_data(self, url: str) -> dict | None:
        """Metode for å hente data fra OMDB sin API"""
        resultat = req.get(url)

        if resultat.status_code == 200:  # sjekker at HTTP request til API gikk bra.
            film_data = resultat.json()
            if (
                film_data["Response"] == "False"
            ):  # sjekker om OMDb API tjeneste kall gikk bra.
                print(film_data["Error"])
                return None
            return film_data
        else:
            print("Feil ved henting av filminformasjon.")
            return None

    def søk_tittel(self, tittel: str) -> None:
        """Metode for å søke etter en film med nøkkelord/tittel"""
        url = f"https://www.omdbapi.com/?apikey={self.api_key}&s={tittel}"
        data = self.hent_data(url)
        self._lagre_søk(data, "søk")
        if data == None:
            self.forrige_søk = None
            return None
        else:
            self.forrige_søk = []

        for film in data["Search"]:
            self.forrige_søk.append(self._lag_søkeresultat(film))

    def søk_id(self, id: str) -> dict | None:
        """Metode for å søke etter en film med IMDB-id"""
        url = f"https://www.omdbapi.com/?apikey={self.api_key}&i={id}"
        data = self.hent_data(url)
        if data == None:
            self.forrige_media = None
            return None
        self._lagre_søk(data, "media")
        data["Sett"] = False
        if data["Type"] in ("movie", "game"):
            self.forrige_media = Film.fra_dict(data)
        else:
            self.forrige_media = Serie.fra_dict(data)
        return data

    def _lagre_søk(self, data: dict, navn: str) -> None:
        """Lagre informasjon om et film"""
        adresse = os.path.join(
            os.path.abspath(os.path.dirname("")),
            r"lagring_søk\{}.json".format("".join(navn.split()).strip().lower()),
        )
        with open(adresse, "w") as json_fil:
            json.dump(data, json_fil, indent=4)

    def _lag_søkeresultat(self, objekt: dict) -> Søkeresultat:
        """Metode for å generere søkeresultater"""
        tittel = objekt["Title"]
        år = objekt["Year"]
        imdb_id = objekt["imdbID"]
        type = objekt["Type"]
        poster = objekt["Poster"]
        return Søkeresultat(tittel, år, imdb_id, poster, type)
