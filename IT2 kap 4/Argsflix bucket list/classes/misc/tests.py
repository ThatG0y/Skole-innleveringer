from classes.app import App
from classes.filmklasser.visuell_media import VisuellMedia
from classes.filmklasser.film import Film
from classes.filmklasser.serie import Serie
from classes.misc.bucketlist import Bucketlist
from classes.søk_klasser.søk import Søk
from classes.søk_klasser.søkeresultat import Søkeresultat

# from classes.misc.ratings import Rating


class Test:
    """Klasse for å enkapsulere alle tester knyttet til Argsflix"""

    def __init__(self) -> None:
        self.kjør_alle_tester()

    def _søk_tests(self) -> None:
        søk = Søk()
        assert søk.søk_id("Feil id") == None
        søk.søk_id("tt0120915")  # Star Wars, phantom menace
        try:
            assert (
                søk.forrige_media["Title"]
                == "Star Wars: Episode I - The Phantom Menace"
            )
            assert søk.forrige_media["Year"] == "1999"
            assert søk.forrige_media["Runtime"] == "136 min"
            assert søk.forrige_media["Type"] == "movie"
            assert søk.forrige_media["DVD"] == "10 Apr 2015"
            assert søk.forrige_media["Sett"] == False
            # Hvis kommer hit, søk generert korrekt
        except AssertionError:
            print("Noe gikk galt under henting av data")

    def _visuell_media_tests(self) -> None:
        try:
            media = VisuellMedia("Dis/Connected", "2008", "tt1151327", "-", False)
        except TypeError:
            print("Ikke riktig antall argumenter for VisuellMedia")

        try:
            film = Film(
                "Dis/Connected", "2008", "tt1151327", "-", "198 min", "DVD-ting", False
            )
        except TypeError:
            print("Ikke riktig antall argumenter for Film")

        try:
            serie = Serie("Marvel", "2006", "tt92jj33", "-", "4", False)
        except TypeError:
            print("Ikke riktig antall argumenter for Serie")

    def kjør_alle_tester(self) -> None:
        self._søk_tests()
        self._visuell_media_tests()
