from klasser.reservasjonssystem.reservasjonssystem import Reservasjonssystem
from klasser.reservasjonssystem.reservasjon import Reservasjon
from klasser.reservasjonssystem.bruker import Bruker
from datetime import datetime


class App:
    """Klasse for den brukerrettede delen av et reservasjonssystem"""

    def __init__(self) -> None:
        self.reservasjonssystem = Reservasjonssystem()
        self.bruker = self.generer_bruker()
        self.reservasjonsID = 0

    def run(self) -> None:
        """Metode for å sette reservasjonsappen i gang"""
        self.fortsett = True
        while self.fortsett == True:
            self.valg()

    def valg(self) -> None:
        """Metode for å enkapsulere den overordnede funksjonaliteten til appen"""
        self.brukergrensesnitt()
        valget = input("Hva vil du gjøre? ").lower()
        print()
        match valget:
            case "1":
                start_tid, slutt_tid = self.sett_reservasjonsintervall()
                ureserverte_biler = self.reservasjonssystem.vis_ureserverte_biler(
                    self.bruker, start_tid, slutt_tid
                )
                if len(ureserverte_biler) == 0:
                    print(
                        "Beklager, det fins ingen ledige biler innenfor det tidsintervallet"
                    )
                    print()
                    return
                print("Dette er en oversikt over ledige biler:")
                print()
                print(ureserverte_biler)
                print()
                self.reservasjonsID += 1
                reservasjon = self.generer_reservasjon(
                    ureserverte_biler, start_tid, slutt_tid
                )
                self.reservasjonssystem.legg_til_reservasjon(reservasjon)
                print(reservasjon)
            case "2":
                if self.hent_reservasjoner():
                    id = self.bekreft_gyldig_id()
                    self.reservasjonssystem.fjern_reservasjon(id)
                    print("Reservasjonen fjernet!")
                    print()
            case "3":
                if self.hent_reservasjoner():
                    id = self.bekreft_gyldig_id()
                    self.beregn_innleverings_kvittering(id)
            case "x":
                self.fortsett = False

    def generer_bruker(self) -> Bruker:
        """Metode for å generere en app-bruker"""
        while True:
            try:
                navn, epost, tlf = (
                    input(
                        "Vennligst skriv inn Navn, E-Mail, og Telefonnummer separert med komma: "
                    )
                    .title()
                    .replace(" ", "")
                    .split(",")
                )
                bruker = Bruker(
                    **{"Navn": navn, "E-post": epost.lower(), "Telefonnummer": tlf}
                )
                print()
                print(bruker)
                if input("Ser dette korrekt ut (y/n)? ").lower() == "y":
                    print()
                    return bruker
                else:
                    continue
            except ValueError:
                print("Ikke gyldig brukerinput, prøv igjen")
                continue

    def generer_reservasjon(
        self, ureserverte_biler: list[str], start_tid: datetime, slutt_tid: datetime
    ) -> Reservasjon:
        """Metode for å generere en gyldig bilreservasjon"""
        while True:
            try:
                info = {
                    "ReservasjonsID": self.reservasjonsID,
                    "Bruker": self.bruker,
                    "Registreringsnummer": input(
                        "Hvilken bil vil du reservere? "
                    ).upper(),
                    "Start tid": start_tid,
                    "Slutt tid": slutt_tid,
                }
                print()
                assert info["Registreringsnummer"] in ureserverte_biler
                reservasjon = Reservasjon(**info)
                return reservasjon
            except AssertionError:
                print("Ugyldig referansenummer, prøv igjen")
                print()
                continue

    def hent_reservasjoner(self) -> bool:
        """Metode for å hente reservasjoner i reservasjonssystemet"""
        reservasjoner = [
            (reservasjonsID, refereansenummer)
            for reservasjonsID, refereansenummer in self.reservasjonssystem.id_til_r_nummer_dict.items()
        ]
        if len(reservasjoner) == 0:
            print("Det fins ingen reservasjoner for øyeblikket!")
            print()
            return False
        print(reservasjoner)
        print()
        return True

    def bekreft_gyldig_id(self) -> int:
        """Metode for å sikre gyldig reservasjonsID"""
        while True:
            try:
                id = int(input("Hvilken reservasjon gjelder det? "))
                print()
                print(
                    self.reservasjonssystem.reservasjoner_registreringsnummer[
                        self.reservasjonssystem.id_til_r_nummer_dict[id]
                    ][id]
                )
                assert input("Er dette riktig reservasjon (y/n)? ").lower() == "y"
                print()
                return id
            except KeyError:
                print("Ikke en gyldig id")
                continue
            except ValueError:
                print("Ikke en gyldig id")
                continue
            except AssertionError:
                print("Velg id på nytt")
                continue

    def beregn_innleverings_kvittering(self, id: int) -> None:
        """Metode for å sikre gyldige bil-innleveringer"""
        while True:
            try:
                km = int(input("Hvor mange km kjørte du tilsammen? "))
                print()
                self.reservasjonssystem.lever_bil(id, km)
                return
            except ValueError:
                print("Ikke et gyldig antall km")
                print()
                continue

    @staticmethod
    def sett_reservasjonsintervall() -> list[datetime, datetime]:
        """Hjelpemetode for å sikre gyldige datetime-datoer"""
        while True:
            try:
                print("Innenfor hvilke datoer vil du reservere bilen? ")
                print()
                year1, month1, day1 = map(
                    int, input("Startdato på formen yyyy-mm-dd: ").split("-")
                )
                year2, month2, day2 = map(
                    int, input("Sluttdato på formen yyyy-mm-dd: ").split("-")
                )
                start_tid = datetime(year1, month1, day1)
                slutt_tid = datetime(year2, month2, day2)
                assert start_tid < slutt_tid
                return [start_tid, slutt_tid]
            except ValueError:
                print("Ugyldig intervall")
                print()
                continue
            except AssertionError:
                print("Sluttdato kan ikke kommer før startdato")
                print()
                continue

    @staticmethod
    def brukergrensesnitt() -> None:
        """Metode for å vise mulige brukervalg"""
        print("1 Reservere en bil")
        print("2 Avbestille en reservering")
        print("3 Levere inn en bil")
        print("X Avslutt")
