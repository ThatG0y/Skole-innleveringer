import requests as req
from utils.settings import API_KEY


class Søk:
    def __init__(self) -> None:
        self.film_liste = []
        self.api_key = API_KEY

    def hent_data(self, url: str) -> dict:
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

    def søk_tittel(self, tittel: str) -> dict:
        url = f"https://www.omdbapi.com/?apikey={self.api_key}&s={tittel}"
        data = self.hent_data(url)
        print(data)

    def søk_id(self, id: str) -> dict:
        url = f"https://www.omdbapi.com/?apikey={self.api_key}&i={id}"
        data = self.hent_data(url)
        print(data)
