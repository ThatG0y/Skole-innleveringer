from klasser.bilkollektiv.bilkollektiv import BilKollektiv
from klasser.bilkollektiv.bilklasser.elbil import Elbil
from klasser.bilkollektiv.bilklasser.fossilbil import Fossilbil
from klasser.reservasjonssystem.reservasjon import Reservasjon
from klasser.reservasjonssystem.bruker import Bruker
from datetime import datetime


class Reservasjonssystem:
    """Klasse som representerer et reservasjonssystem rettet mot reservering av biler i et bilkollektiv."""

    def __init__(self) -> None:
        self.bilkollektiv = BilKollektiv()
        # Lagrer registreringsnummer for en gitt id
        self.id_til_r_nummer_dict = {}

        # Lagrer alle reservasjoner etter registreringsnummer
        self.reservasjoner_registreringsnummer = {}

    def legg_til_reservasjon(self, ny_reservasjon: Reservasjon) -> None:
        """Metode for å registrere en bilreservasjon"""
        # Sjekker om bilen fins
        if ny_reservasjon.registreringsnummer not in self.bilkollektiv.biler:
            print("Den bilen er ikke registrert i bilkollektivet")
            print()
            return

        # Sjekker om bilen er reservert fra før
        if ny_reservasjon.registreringsnummer in self.reservasjoner_registreringsnummer:
            for dokumentert_reservasjon in self.reservasjoner_registreringsnummer[
                ny_reservasjon.registreringsnummer
            ].values():  # Henter alle reservasjoner knyttet til bilen
                if self.sjekk_reservasjon_overlapp(
                    dokumentert_reservasjon, ny_reservasjon
                ):
                    print("Bilen er desverre opptatt innenfor dette tidsintervallet")
                    print()
                    return

        self.id_til_r_nummer_dict[ny_reservasjon.reservasjon_ID] = (
            ny_reservasjon.registreringsnummer
        )
        self.reservasjoner_registreringsnummer[ny_reservasjon.registreringsnummer] = {}
        self.reservasjoner_registreringsnummer[ny_reservasjon.registreringsnummer][
            ny_reservasjon.reservasjon_ID
        ] = ny_reservasjon

    def fjern_reservasjon(self, reservasjon_ID: int) -> None:
        """Metode for å avbestille en registrert bilreservasjon"""
        self.reservasjoner_registreringsnummer[
            self.id_til_r_nummer_dict[reservasjon_ID]
        ].pop(reservasjon_ID)
        self.id_til_r_nummer_dict.pop(reservasjon_ID)

    def lever_bil(self, reservasjon_ID: int, km_kjørt: float) -> None:
        """Metode for å levere tilbake en utlånt bil"""
        valgt_bil = self.bilkollektiv.biler[self.id_til_r_nummer_dict[reservasjon_ID]]

        print(f"Pris for {km_kjørt} km: {valgt_bil.pris_per_km * km_kjørt} kr")

        # Antar at brukeren fullader/fyller tanken helt opp hvis den noen gang ble brukt opp
        match valgt_bil:
            case Elbil():
                wh = valgt_bil.wattimer_per_km * km_kjørt
                print(f"Du har brukt {wh} watt-timer under kjøringen")

                if valgt_bil.energinivå < wh:
                    print(
                        f"Du fulladet bilen {((wh-valgt_bil.energinivå)//valgt_bil.batteri)+1} under kjøringen"
                    )
                    valgt_bil.energinivå += valgt_bil.batteri * (
                        ((wh - valgt_bil.energinivå) // valgt_bil.batteri) + 1
                    )

                valgt_bil.energinivå -= wh

                print(f"Bilen har {valgt_bil.energinivå} watt-timer til overs")
            case Fossilbil():
                bensin_forbruk = valgt_bil.bensin_per_km * km_kjørt
                print(f"Du har brukt {bensin_forbruk} liter under kjøringen")

                if valgt_bil.drivstoffmengde < bensin_forbruk:
                    print(
                        f"Du fylte bilens tank {((bensin_forbruk-valgt_bil.drivstoffmengde)//valgt_bil.tank)+1} ganger under kjøringen"
                    )
                    valgt_bil.drivstoffmengde += valgt_bil.tank * (
                        ((bensin_forbruk - valgt_bil.drivstoffmengde) // valgt_bil.tank)
                        + 1
                    )

                valgt_bil.drivstoffmengde -= bensin_forbruk

                print(
                    f"Bilen har {valgt_bil.drivstoffmengde} liter bensin igjen i tanken"
                )

        # Oppdater lagret reservasjon-/bil-info
        print()
        self.fjern_reservasjon(reservasjon_ID)
        # self.bilkollektiv.lagre_info()

    def vis_ureserverte_biler(
        self, bruker: Bruker, start_tid: datetime, slutt_tid: datetime
    ) -> list[str]:
        """Metode for hente ledige biler for et gitt tidsintervall"""
        ureserverte_biler = [
            registreringsnummer for registreringsnummer in self.bilkollektiv.biler
        ]
        for bil in ureserverte_biler:
            if bil in self.reservasjoner_registreringsnummer:
                for reservasjon in self.reservasjoner_registreringsnummer[bil].values():
                    simulert_reservasjon = Reservasjon(
                        **{
                            "ReservasjonsID": 0,
                            "Bruker": bruker,
                            "Registreringsnummer": bil,
                            "Start tid": start_tid,
                            "Slutt tid": slutt_tid,
                        }
                    )
                    if self.sjekk_reservasjon_overlapp(
                        reservasjon, simulert_reservasjon
                    ):
                        ureserverte_biler.remove(bil)
        return ureserverte_biler

    @staticmethod
    def sjekk_reservasjon_overlapp(
        reservasjon_1: Reservasjon, reservasjon_2: Reservasjon
    ) -> bool:
        """Hjelpemetode for å sjekke reservasjoner for overlappende tidsintervallet"""
        if (
            reservasjon_2.slutt_tid < reservasjon_1.start_tid
            or reservasjon_1.slutt_tid < reservasjon_2.start_tid
        ):
            return False
        else:
            return True
