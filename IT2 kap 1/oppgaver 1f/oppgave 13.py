def antall_forekomster_i_streng(
    tegn: str, streng: str, case_sensitive: bool = True
) -> int:
    """Sjekker antall forekomster av et tegn i en streng

    Parameters
    ----------
    tegn : str
        Et tegn
    streng : str
        En streng
    case_sensitive : bool, optional
        Om strengen skal sjekkes med case-sensitivity, by default True

    Returns
    -------
    int
        Antall forekomster
    """
    if not case_sensitive:
        streng, tegn = streng.lower(), tegn.lower()

    return streng.count(tegn)


def main():
    streng = "Rundt 9000 fvt. var mesteparten av Norge fremdeles dekket av is. Tidligere hadde det vært 30-40 istider, men fra 13 000 fvt. smeltet fastlandsisen raskt. En kuldeperiode mellom 9000 og 8000 fvt. gjorde at isen vokste for siste gang, og skapte det store raet - en morenerygg som går gjennom Østfold og deretter følger norskekysten."
    print(
        f'Antall forekomster av tegnet "-" i strengen er {antall_forekomster_i_streng("-", streng)}'
    )
    print(
        f'Antall forekomster av tegnet "E" i strengen er {antall_forekomster_i_streng("E", streng)}'
    )
    print(
        f'Antall forekomster av tegnet "E" og "e i strengen er {antall_forekomster_i_streng("E", streng, case_sensitive=False)}'
    )


if __name__ == "__main__":
    main()
