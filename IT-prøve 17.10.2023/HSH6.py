import random as rd


def alternativ1(tall_liste: list[int]) -> None:
    maks_verdi = max(tall_liste)
    min_verdi = min(tall_liste)
    print(f"Den minste verdien i lista {tall_liste} er {min_verdi:2}")
    print(f"Den største verdien i lista {tall_liste} er {maks_verdi:2}")


def alternativ2(tall_liste: list[int]) -> None:
    min_verdi = tall_liste[0]
    maks_verdi = tall_liste[0]
    for tall in tall_liste:
        if tall > maks_verdi:
            maks_verdi = tall
        if tall < min_verdi:
            min_verdi = tall
    print(f"Den minste verdien i lista {tall_liste} er {min_verdi:2}")
    print(f"Den største verdien i lista {tall_liste} er {maks_verdi:2}")


def main() -> None:
    tilfeldig_tall_liste = [rd.randint(1, 100) for _ in range(10)]
    alternativ1(tilfeldig_tall_liste)
    alternativ2(tilfeldig_tall_liste)


if __name__ == "__main__":
    main()
