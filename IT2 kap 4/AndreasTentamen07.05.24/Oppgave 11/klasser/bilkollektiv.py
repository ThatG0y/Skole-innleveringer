from klasser.bilklasser.elbil import Elbil
from klasser.bilklasser.fossilbil import Fossilbil
from klasser.misc.reservasjon import Reservasjon
from klasser.misc.medlem import Medlem
import datetime


class Bilkollektiv:
    def __init__(self, navn: str, lokasjon: str) -> None:
        self.navn = navn
        self.lokasjon = lokasjon
        self.bilpark = []
        self.reservasjonsliste = []

    def vis_biler(self) -> None:
        for bil in self.bilpark:
            print(bil)

    def vis_info(self) -> None:
        print(f"Bilkollektivet '{self.navn}' i '{self.lokasjon}' har følgende biler: ")
        self.vis_biler()

    def vis_reservasjoner(self) -> None:
        print("Følgende reservasjoner er lagt inn: ")
        for reservasjon in self.reservasjonsliste:
            print(reservasjon)

    def legg_til_bil(self, bil: Elbil | Fossilbil) -> None:
        self.bilpark.append(bil)

    def fjern_bil(self, registreringsnummer: str) -> None:
        for bil in self.bilpark:
            if bil.registreringsnummer == registreringsnummer:
                print(f"Fjernet '{registreringsnummer}'")
                self.bilpark.pop(bil)

    def reserver_bil(
        self, bil: Elbil | Fossilbil, medlem: Medlem, dato: datetime.datetime
    ) -> None:
        for reservasjon in self.reservasjonsliste:
            if bil.registreringsnummer == reservasjon.bil.registreringsnummer:
                if dato == reservasjon.dato:
                    print("Den bilen er desverre opptatt den dagen")
                    return None
        self.reservasjonsliste.append(Reservasjon(bil, medlem, dato))

    def lever_bil(self, registreringsnummer: str, dato: datetime.datetime) -> bool:
        if self.fjern_reservasjon(registreringsnummer, dato):
            print("Vi har registrert din innlevering av bil")
        else:
            print(
                f"Vi har ikke registrert et utlån av {registreringsnummer} for {dato}, vennligst sjekk for skrivefeil"
            )

    def fjern_reservasjon(self, registreringsnummer: str, dato: datetime.datetime):
        for reservasjon in self.reservasjonsliste:
            if registreringsnummer == reservasjon.bil.registreringsnummer:
                if dato == reservasjon.dato:
                    self.reservasjonsliste.pop(reservasjon)
                    return True
        return False

    def brukergrensesnitt(self) -> None:
        print("1 Vis bilpark")
        print("2 Vis reservasjoner")
        print("3 Legg til bil")
        print("4 Legg til reservasjon")
        print("5 Fjern bil")
        print("6 Fjern reservasjon")
        print("7 Lever bil")
        print("X Avslutt")

    def run(self) -> None:
        self.fortsett = True
        while self.fortsett:
            self.brukergrensesnitt()
            self.bruker_valg()

    def bruker_valg(self) -> None:  # skulle gjort ferdig her
        valg = input("Hva vil du gjøre?")

        if valg == "1":
            self.valg_1()
        elif valg == "2":
            self.valg_2
        elif valg == "3":
            self.valg_3
        elif valg == "4":
            pass
        elif valg == "5":
            pass
        elif valg == "6":
            pass
        elif valg == "7":
            pass
        elif valg.lower() == "x":
            self.fortsett = False

    def valg_1(self) -> None:
        self.vis_info()

    def valg_2(self) -> None:
        print("Følgende reservasjoner er registrert:")
        for reservasjon in self.reservasjonsliste:
            print(reservasjon)

    def valg_3(self) -> None:
        print("For å legge til en bil gi følgende informasjon: ")
        type = input("Er bilen en (E)lbil eller (F)ossilbil? ")
        if type.lower() == "e":
            modell = input("Modell: ")
            registreringsnummer = input("Registrasjonsnummer: ")
            pris = input("Pris: ")
            wh_per_km = int(input("Wh per km: "))
            batteri = int(input("Batteri: "))
            energinivå = int(input("Energinivå: "))
            self.legg_til_bil(
                Elbil(
                    modell,
                    registreringsnummer,
                    pris,
                    wh_per_km,
                    batteri,
                    energinivå,
                )
            )
        elif type.lower() == "f":
            modell = input("Modell: ")
            registreringsnummer = input("Registrasjonsnummer: ")
            pris = input("Pris: ")
            bensin_per_km = int(input("Bensin per km: "))
            tank = int(input("Tank: "))
            drivstoff_mengde = int(input("Drivstoff mengde: "))
            self.legg_til_bil(
                Fossilbil(
                    modell,
                    registreringsnummer,
                    pris,
                    bensin_per_km,
                    tank,
                    drivstoff_mengde,
                )
            )
        else:
            print("Noe gikk galt")

    def valg_4(self) -> None:
        pass
