def alternativ1() -> None:  # den mest time-effective løsning
    liste_tall = []

    reversert_liste_kvadrattall = []

    for tall in range(1, 10):
        liste_tall.append(tall)
        reversert_liste_kvadrattall.insert(0, tall**2)

    print(f"En liste med tall fra 1-10: {liste_tall}")
    print(
        f"En reversert liste med kvadrattallene fra 1-10: {reversert_liste_kvadrattall}"
    )


def alternativ2() -> None:
    liste_tall = [tall for tall in range(1, 10)]
    reversert_liste_kvadrattall = [tall**2 for tall in range(1, 10)][
        ::-1
    ]  # evt [tall**2 for tall in range(9, 0, -1)]

    print(f"En liste med tall fra 1-10: {liste_tall}")
    print(
        f"En reversert liste med kvadrattallene fra 1-10: {reversert_liste_kvadrattall}"
    )


def main() -> None:
    alternativ1()
    alternativ2()


if __name__ == "__main__":
    main()
