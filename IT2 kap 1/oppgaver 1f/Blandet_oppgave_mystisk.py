def hokuspokus(tekst: str, n: int) -> str:
    """Øker alle tegnene sine Unicode-verdier i en streng.

    Parameters
    ----------
    tekst : str
        En streng
    n : int
        Hvor mye tegnene i strengen sine Unicode-verdier øker med

    Returns
    -------
    str
        En ny streng med økt Unicode-verdi
    """
    nytekst = ""
    for bokstav in tekst:
        tallkode = ord(bokstav)
        tallkode += n
        nytekst += chr(tallkode)
    return nytekst


def simsalabim(tekst: str, n: int) -> str:
    """Minker alle tegnene sine Unicode-verdier i en streng.

    Parameters
    ----------
    tekst : str
        En streng
    n : int
        Hvor mye tegnene i strengen sine Unicode-verdier minker med

    Returns
    -------
    str
        En ny streng med minket Unicode-verdi
    """
    nytekst = ""

    for bokstav in tekst:
        tallkode = ord(bokstav)
        tallkode -= n
        nytekst += chr(tallkode)

    return nytekst
