def konverterTallTilBinær(tall: int) -> str:
    binært_tall = ""
    while tall != 0:
        binært_tall += str(
            tall % 2
        )  # setter inn 1 på riktig plass i tallet (1-plass, 2-plass, 4-plass, osv)
        tall = tall // 2  # går gjennom tallet for hver loop
    return binært_tall[::-1]  # returnerer tallet riktig vei


def validInput() -> int:
    while True:
        tall = input("Skriv et tall mellom 1 og 64: ")
        try:
            tall = int(tall)
            return tall
        except ValueError:
            print("Ikke riktig input, prøv igjen")
            continue


def main() -> None:
    tall = validInput()
    binært_tall = konverterTallTilBinær(tall)
    print(f"Tallet {tall} kan skrives som {binært_tall} på binær form")


if __name__ == "__main__":
    main()
