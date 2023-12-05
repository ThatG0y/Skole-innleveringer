from modeller.artist import Artist


class Platealbum:
    def __init__(
        self, albumnavn: str, artist: Artist, plateselskap: str, utgivelsesår: int
    ) -> None:
        self._albumnavn = albumnavn.title()
        self.artist = artist
        self._plateselskap = plateselskap
        self._utgivelsesår = utgivelsesår

    def __str__(self) -> str:
        return f"""Album:
        Navn:                   {self._albumnavn}
        Artist:                 {self.artist.navn}
        Plateselskap:           {self._plateselskap}
        Utgivelsesår:           {self._utgivelsesår}
        """

    def vis_info(self) -> None:
        print(self)
