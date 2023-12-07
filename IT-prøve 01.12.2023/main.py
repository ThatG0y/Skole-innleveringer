from modeller.artist import Artist
from modeller.platealbum.platealbum import Platealbum
from modeller.platesamling import Platesamling

# alle modell-dokument trenger dokumentasjon


def main() -> (
    None
):  # Det gjenstår å legge til brukerstyrt opplevelse med bla. input, inntil videre er alt "hardcoded"
    # Definerer noen objekter
    artist = Artist("Katy", "Perry")
    album = Platealbum("Noe", artist, "ENda mer", 1984)
    samling = Platesamling("adnreas", plater=album)

    # Tester noen funksjoner, rakk ikke lage unit_tests men ville gjort det istedet
    samling.registrer_artist(Artist("michael", "jackson"))
    samling.registrer_platealbum(
        Platealbum("All i want for christmas", Artist("Mariah", "Carrey"), "Noko", 1900)
    )
    samling.registrer_platealbum(
        Platealbum("Last Christmas", Artist("Mariah", "Carrey"), "Noko", 1910)
    )

    # Gir diverse utskrifter, ville sannsynligvis utbrodert utskrifter mer slik at bruker ikke trenger å lese koden for å forstå hva som skrives ut
    samling.vis_alle_artistens_plater(Artist("Mariah", "Carrey"))
    samling.vis_alle_artister()
    samling.vis_alle_plater()
    print(samling)


if __name__ == "__main__":
    main()
