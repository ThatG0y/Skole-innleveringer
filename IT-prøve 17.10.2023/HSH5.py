def tellForekomsterAvSifferITall(tall: int) -> dict[str, int]:
    """Teller forekomster av siffrene 1-9 i et tall

    Parameters
    ----------
    tall : int
        Et gitt tall

    Returns
    -------
    dict[str, int]
        En oversikt over siffer og forekomster hvor nøklene er sifferene 1-9 og korresponderende verdi er antall forekomster
    """
    tall_counter = [int(str(tall).count(str(i))) for i in range(1, 10)]
    tall_dictionary = {str(navn + 1): verdi for navn, verdi in enumerate(tall_counter)}
    return tall_dictionary


def main() -> None:
    tall = 123456789067237834121234569111111111
    siffer_oversikt = tellForekomsterAvSifferITall(tall)
    for siffer, antall in siffer_oversikt.items():
        print(f"Det er {antall:2} forekomster av {siffer}")


if __name__ == "__main__":
    main()
