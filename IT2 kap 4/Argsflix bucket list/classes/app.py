import requests as req
from misc.bucketlist import Bucketlist
import json


class App:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.bucketlist = Bucketlist()

    def hent_film(self, tittel: str) -> object:
        url = f"https://www.omdbapi.com/?apikey={self.api_key}&s={tittel}"
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

    def lagre_film_info(self, data, filename):
        """Lagre informasjon om et film"""
        with open(filename, "w") as json_fil:
            json.dump(data, json_fil, indent=4)
