def main() -> None:
    land_med_høyest_befolkning = {
        "Kina": 1448471404,
        "India": 1406631781,
        "USA": 339665118,
        "Indonesia": 279134505,
        "Pakistan": 242923845,
    }

    print("De fem landene med høyest befolkning er:")
    for land in land_med_høyest_befolkning.keys():
        print(land)

    print("")

    print("Landenes innbyggertall er: ")
    for befolkning in land_med_høyest_befolkning.values():
        print(befolkning)

    print("")

    print("Med andre ord:")
    for land, befolkning in land_med_høyest_befolkning.items():
        print(f"{land} har {befolkning} innbyggere")

    print("")

    print("De fem landene med høyest befolkning i alfabetisk rekkefølge er:")
    for land in sorted(land_med_høyest_befolkning.keys()):
        print(land)

    print("")

    print(
        f"{max(land_med_høyest_befolkning, key=land_med_høyest_befolkning.get)} har høyest befolkning"
    )
    print(
        f"{min(land_med_høyest_befolkning, key=land_med_høyest_befolkning.get)} har lavest befolkning"
    )


if __name__ == "__main__":
    main()
