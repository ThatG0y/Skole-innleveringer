def krypteringsverktøy(streng: str, krypteringsnøkkel: dict) -> str:
    """Bruker gitt krypteringsnøkkel på gitt streng

    Parameters
    ----------
    streng : str
        En streng
    krypteringsnøkkel : dict
        En ordbok med nøkler og verdier for enkrypsjonsbruk

    Returns
    -------
    str
        En (en)kryptert streng
    """
    return "".join(
        [
            krypteringsnøkkel[tegn] if tegn in krypteringsnøkkel.keys() else " "
            for tegn in streng.lower()
        ]
    )


def main() -> None:
    krypter = {
        "a": "c",
        "b": "d",
        "c": "e",
        "d": "f",
        "e": "g",
        "f": "h",
        "g": "i",
        "h": "j",
        "i": "k",
        "j": "l",
        "k": "m",
        "l": "n",
        "m": "o",
        "n": "p",
        "o": "q",
        "p": "r",
        "q": "s",
        "r": "t",
        "s": "u",
        "t": "v",
        "u": "w",
        "v": "x",
        "w": "y",
        "x": "z",
        "y": "ø",
        "z": "å",
        "ø": "a",
        "å": "b",
    }
    dekrypter = {v: k for k, v in krypter.items()}
    streng = "Hemmelig beskjed"
    enkryptert_streng = krypteringsverktøy(streng, krypter)
    print(
        f"{streng} blir til {krypteringsverktøy(streng, krypter)} når man krypterer den"
    )
    print(
        f"{enkryptert_streng} blir til {krypteringsverktøy(enkryptert_streng, dekrypter)} når man dekrypterer den"
    )


if __name__ == "__main__":
    main()
