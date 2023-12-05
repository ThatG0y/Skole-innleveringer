from modeller.platealbum.platealbum import Platealbum
from modeller.artist import Artist


class LPAlbum(Platealbum):
    __PLATETYPE = "LP"

    def __init__(
        self,
        albumnavn: str,
        artist: Artist,
        plateselskap: str,
        utgivelsesår: int,
        farge: str,
        avspillingshastighet: int,
    ) -> None:
        super().__init__(albumnavn, artist, plateselskap, utgivelsesår)
        self._farge = farge
        if not avspillingshastighet in (33, 45):
            while True:
                try:
                    riktig_avspillingshastighet = int(
                        input("Ugyldig avspillingshastighet, vennligst skriv en ny: ")
                    )
                    assert riktig_avspillingshastighet in (33, 45)
                    self._avspillingshastighet = riktig_avspillingshastighet
                    break
                except ValueError:
                    continue
                except AssertionError:
                    continue
        else:
            self._avspillingshastighet = avspillingshastighet

    def __str__(self) -> str:
        print("LP-", end="")
        super().__str__()
        print(f"Platetype:              {self.__PLATETYPE}")
        print(f"Farge:                  {self.__PLATETYPE}")
        print(f"Avspillingshastighet:   {self.__PLATETYPE}")
