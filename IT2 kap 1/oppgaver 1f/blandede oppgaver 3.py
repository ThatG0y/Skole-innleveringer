def lengde_på_streng(streng: str) -> int:
    """Sjekker lengden av en streng

    Parameters
    ----------
    streng : str
        En streng

    Returns
    -------
    int
        Lengden av strengen
    """
    return sum([1 for _ in streng])


def midterste_tegn_i_streng(streng: str) -> str:
    """Finner de midterste bokstavene i en streng.

    Parameters
    ----------
    streng : str
        En streng

    Returns
    -------
    str
        De midterste bokstavene i strengen
    """
    # Returnerer alltid bokstaven som er på indeksen til halve lengden av strengen.
    # Hvis strengen er et partall, returnerer også bokstaven som er på indeksen under.
    # eks. "streng" -> 6 / 2 = 3 -> "e" -> partall -> 3 - 1 = 2 -> "re"
    # eks. "steng" -> 5 / 2 = 2.5 = 2 -> "e" -> oddetall -> "e"
    return "".join(
        (streng[(len(streng) - 1) // 2]) * ((len(streng) + 1) % 2)
        + streng[(len(streng)) // 2]
    )


def streng_er_palindrom(streng: str) -> bool:
    """Sjekker om en gitt streng er et palindrom

    Parameters
    ----------
    streng : str
        En streng

    Returns
    -------
    bool
        Hvis strengen er et palindrom: True. Hvis strengen ikke er det: False
    """
    streng = streng.lower()
    return streng == streng[::-1]


def main() -> None:
    streng = "Hello World"
    print(f"lengden på strengen '{streng}' er {lengde_på_streng(streng)}")

    print(
        f"Bokstaven{'e' * ((len(streng)+1) % 2)} i midten av strengen '{streng}' er '{midterste_tegn_i_streng(streng)}'"
    )

    palindromtest1 = "palindrom"
    palindromtest2 = "reker"

    # print(f"Strengen '{palindromtest1}' er et palindrom: {streng_er_palindrom(palindromtest1)}")

    print(
        f"Strengen '{palindromtest1}' er{' ikke' * (not streng_er_palindrom(palindromtest1))} et palindrom"
    )
    print(
        f"Strengen '{palindromtest2}' er{' ikke' * (not streng_er_palindrom(palindromtest2))} et palindrom"
    )


if __name__ == "__main__":
    main()
