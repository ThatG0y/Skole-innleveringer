from modeller.platealbum.platealbum import Platealbum
from modeller.artist import Artist


class CDAlbum(Platealbum):
    __PLATETYPE = "CD"

    def __init__(
        self, albumnavn: str, artist: Artist, plateselskap: str, utgivelsesår: int
    ) -> None:
        super().__init__(albumnavn, artist, plateselskap, utgivelsesår)

    def __str__(self) -> str:
        print("CD-", end="")
        super().__str__()
        print(f"Platetype:              {self.__PLATETYPE}")
