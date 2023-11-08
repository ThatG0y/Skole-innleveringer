def main() -> None:
    tekst = "Det var en gang for kanskje 3 minutter siden da jeg gikk for å spise en sen middag, at jeg så en mørkerød flodhest knuse gjennom naboens grillutstyr på vei inn deres verandadør."
    tegn_forekomster = {}
    for tegn in tekst:
        try:
            tegn_forekomster[tegn] += 1
        except KeyError:
            tegn_forekomster[tegn] = 1

    for key, value in dict(
        sorted(tegn_forekomster.items(), key=lambda item: item[1], reverse=True)
    ).items():
        print(f"'{key}': {value}")


if __name__ == "__main__":
    main()
