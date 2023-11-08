Tall = int | float


def oppskrift_fra_mengder(sukker: Tall, mel: Tall, smør: Tall) -> dict[str, int]:
    return {"sukker": sukker, "mel": mel, "smør": smør}


def oppskrift_fra_sukker(mengde: Tall) -> dict[str, int]:
    return oppskrift_fra_mengder(mengde, 2 * mengde, 3 * mengde)


def oppskrift_fra_mel(mengde: Tall) -> dict[str, int]:
    return oppskrift_fra_mengder(mengde / 2, mengde, (3 / 2) * mengde)


def oppskrift_fra_smoer(mengde: Tall) -> dict[str, int]:
    return oppskrift_fra_mengder(mengde / 3, (2 / 3) * mengde, mengde)


def skriv_oppskrift(sukker: Tall, mel: Tall, smør: Tall) -> None:
    print("Du trenger: ")
    print(f"{sukker} dl sukker")
    print(f"{mel} dl mel")
    print(f"{smør} dl smør")


def bak_kaker() -> None:
    while True:
        try:
            ingrediens = input(
                "Hvilken ingrediens vil du basere oppskriften på? "
            ).lower()
            mengde = float(input(f"Hvor mye {ingrediens} har du? "))
        except ValueError:
            print("Feil input. Skriv en kakeingrediens og en tallmengde.")
            continue
        match ingrediens:
            case "sukker":
                oppskrift = oppskrift_fra_sukker(mengde)
            case "mel":
                oppskrift = oppskrift_fra_mel(mengde)
            case "smør":
                oppskrift = oppskrift_fra_smoer(mengde)
            case _:
                print("Noe gikk galt, prøv igjen")
                continue
        skriv_oppskrift(*oppskrift.values())
        break


def main() -> None:
    bak_kaker()


if __name__ == "__main__":
    main()
