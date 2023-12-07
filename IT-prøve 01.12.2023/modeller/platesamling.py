from modeller.artist import Artist
from modeller.platealbum.platealbum import Platealbum


# to do: dokumentasjon, korreksjon av protected vs public noen steder (evt laget noen hent_navn() funksjoner osv), og generell opprydding
class Platesamling:
    def __init__(
        self, eiernavn: str, plater: Platealbum = [], artister: Artist = []
    ) -> None:
        self._eiernavn = eiernavn
        self._plater = []
        self._artister = []
        self._artistoversikt = {}
        self._lag_artistoversikt(artister, plater)
        print(self)

    def __str__(self) -> str:
        print(f"Platesamling:\n")
        for artist in self._artister:
            print(artist)
            for plate in self._artistoversikt[artist]:
                print(plate)
            print("---------------------------------------------")
        return ""

    def _lag_artistoversikt(
        self, artister: Artist = False, plater: Platealbum = False
    ) -> None:
        if artister and artister.navn not in [artist.navn for artist in self._artister]:
            self._artister.append(artister)
        if plater and plater._albumnavn not in [
            plate._albumnavn for plate in self._plater
        ]:
            self._plater.append(plater)
            if plater.artist.navn not in [artist.navn for artist in self._artister]:
                self._artister.append(plater.artist)

        self._artistoversikt = {artist: [] for artist in self._artister}
        for plate in self._plater:
            for artist in self._artistoversikt.keys():
                if plate.artist.navn == artist.navn:
                    if plate._albumnavn not in [
                        album._albumnavn for album in self._artistoversikt[artist]
                    ]:
                        self._artistoversikt[artist].append(plate)

    def registrer_platealbum(self, platealbum: Platealbum) -> None:
        self._lag_artistoversikt(plater=platealbum)

    def registrer_artist(self, artist: Artist) -> None:
        self._lag_artistoversikt(artister=artist)

    def vis_alle_plater(self) -> None:
        print("Plater:\n")
        for plate in self._plater:
            print(plate)
            print("---------------------------------------------\n")

    def vis_alle_artister(self) -> None:
        print("Artister:\n")
        for artist in self._artister:
            print(artist)
            print("---------------------------------------------\n")

    def vis_alle_artistens_plater(self, artist: Artist) -> None:
        for artister in self._artistoversikt.keys():
            if artist.navn == artister.navn:
                print(
                    f"{artister.navn+':':32}{[plate._albumnavn for plate in self._artistoversikt[artister]]}\n"
                )
                print("---------------------------------------------\n")

                return None
        print(
            f"Ingen artister med navnet '{artist.navn}' er registrert i platesamlingen"
        )
