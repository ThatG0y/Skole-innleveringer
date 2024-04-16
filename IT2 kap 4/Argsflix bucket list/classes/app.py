from classes.misc.bucketlist import Bucketlist
from classes.søk_klasser.søk import Søk
from classes.filmklasser.film import Film
from classes.filmklasser.serie import Serie


class App:
    """Klasse for å enkapsulere all informasjon og funksjonalitet knyttet til Argsflix-applikasjonen"""

    def __init__(self) -> None:
        self.bucketlist = Bucketlist(input("Sign up / Login som: "))
        self.søk = Søk()
        self.fortsett = False

    def kjør(self) -> None:
        """Metode for å sette- og holde programmet i gang"""
        self.fortsett = True
        while self.fortsett == True:
            self._valg()

    def _valg(self) -> None:
        """Metode for funksjonalitet knyttet til brukerinteraksjon"""
        self._gui()
        valg = input("Hva vil du gjøre: ")

        if valg == "1":  # Søker etter søkeord
            self.søk.søk_tittel(input("Tittelen du vil søke etter: "))
            if (
                self.søk.forrige_søk == None
            ):  # Hvis noe gikk galt under innhenting av data, ikke print søkeresultat
                return None
            for resultat in self.søk.forrige_søk:
                print(resultat)  # Printer alle søkeresultater

        elif valg == "2":  # Søk/hent informasjon med IMDB-id
            self.søk.søk_id(input("IMDB-iden til filmen du vil slå opp: "))
            if (
                self.søk.forrige_media == None
            ):  # Hvis noe gikk galt under innhenting av data, ikke print søkeresultat
                return None
            print(self.søk.forrige_media)  # Printer søkeresultatet

        elif valg == "3":  # Legger til film i favoritter
            self.bucketlist.legg_til_favoritt(
                self.søk.søk_id(  # Bruker IMDB-id for å indikere filmen vi vil legge til
                    input("IMDB-iden til filmen du vil legge til favoritter: ")
                )
            )
            print(
                "\nDu la til '{}' i din Bucketlist\n".format(
                    self.søk.forrige_media.tittel
                )
            )

        elif valg == "4":  # Viser favoritter
            valg_1 = input("Vil du se filtrert versjon av favoritter y/n: ")
            if valg_1.lower() == "y":
                valg_2 = input("'Sett' versjon eller 'ikke sett' versjon s/i: ")
                if valg_2.lower() == "s":
                    self._vis_favoritter_valg(sett=True, valg=True)
                elif valg_2.lower() == "i":
                    self._vis_favoritter_valg(sett=False, valg=True)
                else:
                    print("Ugyldig input. Viser ufiltrert: ")
                    self._vis_favoritter_valg()
            else:
                self._vis_favoritter_valg()

        elif valg == "5":  # Marker favoritt-film som sett
            self.bucketlist.marker_sett(  # Bruker IMDB-id for å indikere hvilken film vi har sett
                input("IMDB-iden til filmen du vil markere som sett: ")
            )

        elif valg == "6":  # Fjerner favorittfilm
            self.bucketlist.fjern_favoritt(  # Bruker IMDB-id for å indikere hvilken film vi vil fjerne
                input("IMDB-iden til filmen du vil fjerne fra favoritter: ")
            )

        elif valg.lower() == "x":  # Avslutter programmet
            self.fortsett = False

        else:  # Gitt dårlig input -> start på nytt
            print("Ikke gyldig input")

    def _vis_favoritter_valg(self, sett: bool = False, valg: bool = False) -> None:
        for media in self.bucketlist.favoritter:
            if not valg:
                if media["Type"] in ("movie", "game"):
                    media = Film.fra_dict(media)  # Utskrift for film/spill
                else:
                    media = Serie.fra_dict(media)  #
                print(media)
            else:
                if media["Type"] in ("movie", "game") and media["Sett"] == sett:
                    media = Film.fra_dict(media)  # Utskrift for film/spill
                elif media["Type"] in ("series") and media["Sett"] == sett:
                    media = Serie.fra_dict(media)  # Utskrift for serie
                else:
                    continue
                print(media)

    @staticmethod
    def _gui() -> None:  # Brukergrensesnitt
        """Statisk metode for å representere brukergrensesnitt"""
        print()
        print("Her kan du hente informasjon om film:")
        print("1 Søk")
        print("2 Hent film-info")
        print("3 Legg til favoritter")
        print("4 Vis favoritter")
        print("5 Marker favoritt som sett")
        print("6 Fjern favoritt")
        print("X Avslutt")
        print()
