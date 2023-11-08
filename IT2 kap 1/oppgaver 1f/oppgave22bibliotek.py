def summer_liste(liste: list[int | float]) -> float:
    """Summerer tallene i en liste

    Parameters
    ----------
    liste : list[int  |  float]
        Liste med tall

    Returns
    -------
    float
        Summen av tallene i listen
    """
    return sum(liste)


def gjennomsnittlig_verdi_i_liste(liste: list[int | float]) -> float:
    """Finner gjennomsnittlig verdi i listen

    Parameters
    ----------
    liste : list[int  |  float]
        Liste med tall

    Returns
    -------
    float
        Gjennomsnittlig verdi i listen
    """
    return sum(liste) / len(liste)


def størst_tall_i_liste(liste: list[int | float]) -> float:
    """Finner største tall i en liste

    Parameters
    ----------
    liste : list[int  |  float]
        Liste med tall

    Returns
    -------
    float
        Største tall i listen
    """
    return max(liste)


def minst_tall_i_liste(liste: list[int | float]) -> float:
    """Finner minste tall i en liste

    Parameters
    ----------
    liste : list[int  |  float]
        Liste med tall

    Returns
    -------
    float
        Minste tall i listen
    """
    return min(liste)
