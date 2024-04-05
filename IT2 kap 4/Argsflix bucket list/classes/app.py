import requests as req
from misc.bucketlist import Bucketlist
from classes.søk_klasser.søk import Søk
import json


class App:
    def __init__(self) -> None:
        self.bucketlist = Bucketlist()
        self.søk = Søk()

    def lagre_film_info(self, data, filename):
        """Lagre informasjon om et film"""
        with open(filename, "w") as json_fil:
            json.dump(data, json_fil, indent=4)

    @staticmethod
    def gui():
        print()

    def run(self):
        pass
