import requests as req
from classes.misc.bucketlist import Bucketlist
from classes.søk_klasser.søk import Søk
from classes.filmklasser.film import Film
from classes.filmklasser.serie import Serie
import json


class App:
    def __init__(self) -> None:
        self.bucketlist = Bucketlist(input("Sign up / Login som: "))
        self.søk = Søk()
        self.fortsett = False

    def lagre_søk_info(self, data, filename):
        """Lagre informasjon om et film"""
        with open(filename, "w") as json_fil:
            json.dump(data, json_fil, indent=4)

    def kjør(self):
        self.fortsett = True
        while self.fortsett == True:
            self.valg()

    def valg(self) -> None:
        self.gui()
        valg = input("Hva vil du gjøre: ")

        if valg == "1":
            self.søk.søk_tittel(input("Tittelen du vil søke etter: "))
            if self.søk.forrige_søk == None:
                return None
            for resultat in self.søk.forrige_søk:
                print(resultat)
        elif valg == "2":
            self.søk.søk_id(input("IMDB-iden til filmen du vil slå opp: "))
            if self.søk.forrige_media == None:
                return None
            print(self.søk.forrige_media)
        elif valg == "3":
            self.bucketlist.legg_til_favoritt(
                self.søk.søk_id(
                    input("IMDB-iden til filmen du vil legge til favoritter: ")
                )
            )
        elif valg == "4":
            for media in self.bucketlist.favoritter:
                if media["Type"] in ("movie", "game"):
                    media = Film.fra_dict(media)
                else:
                    media = Serie.fra_dict(media)
                print(media)
        elif valg == "5":
            self.bucketlist.marker_sett(
                input("IMDB-iden til filmen du vil markere som sett: ")
            )
        elif valg == "6":
            self.bucketlist.fjern_favoritt(
                input("IMDB-iden til filmen du vil fjerne fra favoritter: ")
            )
        elif valg.lower() == "x":
            self.fortsett = False
        else:
            print("helt sånn hjelpt meg")

    @staticmethod
    def gui():
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
