def hent_valid_personinformasjon() -> list[str, int]:
    while True:
        try:
            navn, alder = input("Vennligst skriv et navn og en alder: ").split(" ")
        except ValueError:
            print("For mange verdier, prøv igjen")
            continue
        try:
            alder = int(alder)
            assert type(navn) == str
            assert navn.lower()[0] in "abcdefghijklmnopqrstuvwxyzæøå"
        except ValueError:
            print("Alder burde være et heltall, vennligst prøv igjen")
            continue
        except AssertionError:
            print("Navn burde være en streng, vennligst prøv igjen")
            continue
        return navn, alder


def hent_valid_forbokstav() -> str:
    while True:
        forbokstav = input("Skriv en bokstav: ")
        try:
            assert type(forbokstav) == str
            assert len(forbokstav) == 1
        except AssertionError:
            print("Vennligst skriv en bokstav")
            continue
        return forbokstav


def finn_person(personer: dict[str, int]) -> None:
    forbokstav = hent_valid_forbokstav()
    for navn in personer.keys():
        if navn[0].lower() == forbokstav.lower():
            print(f"{navn}      {personer[navn]}")


def legg_til_person(personer: dict[str, int]) -> dict[str, int]:
    test = "j"
    while test == "j":
        navn, alder = hent_valid_personinformasjon()
        personer[navn.title()] = alder
        test = input("Hvis du ønsker å legge til flere navn, tast 'j': ")
    return personer


def main() -> None:
    personer = {}
    personer = legg_til_person(personer)
    finn_person(personer)


if __name__ == "__main__":
    main()
