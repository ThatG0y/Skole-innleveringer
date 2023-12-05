from modeller.artist import Artist
from modeller.platealbum.platealbum import Platealbum


class Platesamling:
    def __init__(
        self, eiernavn: str, plater: Platealbum = [], artister: Artist = []
    ) -> None:
        self._eiernavn = eiernavn
        self._plater = []
        self._artister = []
        self._artistoversikt = {}
        self._lag_artistoversikt(artister, plater)

    def __str__(self) -> str:
        print(f"Platesamling:")
        for artist in self._artister:
            print(artist)
            for plate in self._artistoversikt[artist]:
                print(plate)
        return ""

    def _lag_artistoversikt(
        self, artister: Artist = False, plater: Platealbum = False
    ) -> None:
        if artister:
            self._artister.append(artister)
            self._artister = list(set(self._artister))
        if plater:
            self._plater.append(plater)
            self._plater = list(set(self._plater))
            if plater.artist not in self._artister:
                self._artister.append(plater.artist)

        self._artistoversikt = {artist: [] for artist in self._artister}
        for plate in self._plater:
            if plate.artist in [artist for artist in self._artistoversikt.keys()]:
                if plate not in [album for album in self._artistoversikt[plate.artist]]:
                    self._artistoversikt[plate.artist].append(plate)
            else:
                self._artistoversikt[plate.artist] = [plate]

        print(self)

    def registrer_platealbum(self, platealbum: Platealbum) -> None:
        self._lag_artistoversikt(plater=[platealbum])

    def registrer_artist(self, artist: Artist) -> None:
        self._lag_artistoversikt(plater=[artist])

    def vis_alle_plater(self) -> None:
        print(f"Plater:                   {self._plater}")

    def vis_alle_artister(self) -> None:
        print(f"Artister:                   {self._artister}")

    def vis_alle_artistens_plater(self, artist: Artist) -> None:
        print(f"{artist.navn}:                   {self._artistoversikt[artist]}")
