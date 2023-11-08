from KapselMaskin import KapselMaskin, unitTests as sourceTests
from LedelseKapselMaskin import LedelseKapselMaskin
from KunderKapselMaskin import KunderKapselMaskin


def vanligMaskin() -> None:  # GUI for vanlige KapselMaskiner
    print("1 - Fylle på med vann")
    print("2 - Lag en espresso")
    print("3 - Lag en lungo")
    print("* - Kjør test")
    print("ENTER for å avslutte")
    print("")


def ledelseMaskin() -> None:  # GUI for KapselMaskiner med flere drikker
    print("1 - Fylle på med vann")
    print("2 - Lag en espresso")
    print("3 - Lag en lungo")
    print("4 - Lag en te")
    print("5 - Fyll et glass vann")
    print("* - Kjør test")
    print("ENTER for å avslutte")
    print("")


def kundeMaskin() -> None:  # GUI for KapselMaskiner med penge-funksjonalitet
    print("1 - Fylle på med vann")
    print("2 - Lag en espresso")
    print("3 - Lag en lungo")
    print("4 - Sett inn penger")
    print("5 - Avbryt transaksjon")
    print("* - Kjør test")
    print("ENTER for å avslutte")
    print("")


def userInterface(
    kapsel_maskin: KapselMaskin,
) -> str:  # viser riktig GUI for gitt KapselMaskin
    if isinstance(kapsel_maskin, LedelseKapselMaskin):
        ledelseMaskin()
    elif isinstance(kapsel_maskin, KunderKapselMaskin):
        kundeMaskin()
    else:
        vanligMaskin()

    return str(input("Hva vil du gjøre? "))


def GUIFunksjonalitet(
    maskin: KapselMaskin,
) -> (
    dict
):  # lagrer funksjonalitet i en ordbok som er i tråd med gui-templatesa øverst i dokumentet
    metode_dict = {
        "*": sourceTests,
        "1": getattr(maskin, "fyllVann"),
    }

    metode_liste = [
        metode
        for metode in dir(maskin)
        if metode.startswith("lag")
        or metode not in dir(KapselMaskin)
        and callable(getattr(maskin, metode))
    ]
    metode_dict.update(
        {str(i + 2): getattr(maskin, metode) for i, metode in enumerate(metode_liste)}
    )
    return metode_dict


def testProgram(maskin: KapselMaskin) -> None:
    funksjonalitet_dict = GUIFunksjonalitet(maskin)
    while True:
        user_input = userInterface(maskin)
        if user_input == "":
            break
        try:
            assert user_input in funksjonalitet_dict.keys()
        except AssertionError:
            print("Input ikke godkjent")
            continue

        funksjonalitet_dict[user_input]()  # kjører funksjonalitets-funksjon

        continue


def main() -> None:
    kaffe_maskin = KapselMaskin(1500)
    testProgram(kaffe_maskin)
    kaffe_maskin = KunderKapselMaskin(1500)
    testProgram(kaffe_maskin)
    kaffe_maskin = LedelseKapselMaskin(1500)
    testProgram(kaffe_maskin)


if __name__ == "__main__":
    main()
