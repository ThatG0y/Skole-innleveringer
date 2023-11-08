# egendefinerte typer
Tall = int | float


def overlapp_intervall(
    a: Tall, b: Tall, c: Tall, d: Tall
) -> bool:  # (a,b) og (c,d) er intervaller
    """Sjekker om to intervaller overlapper,
    returnerer True om intervallene overlapper, ellers False

    Parameters
    ----------
    a : Tall
        Startsverdi for første intervall
    b : Tall
        Sluttverdi for første intervall
    c : Tall
        Startsverdi for andre intervall
    d : Tall
        Sluttverdi for andre intervall

    Returns
    -------
    bool
        Sier om intervallene overlapper
    """
    if d <= a or b <= c:
        return False
    else:
        return True


def main():
    # testverdier
    print(
        f"intervallet (1, 10) overlapper med intervallet (3, 4): {overlapp_intervall(1, 10, 3, 4)}"
    )  # intervallet (3,4) overlapper med intervallet (1,10), derfor returnerer funksjonen "True"
    print(
        f"intervallet (1, 2) overlapper med intervallet (3, 4): {overlapp_intervall(1, 2, 3, 4)}"
    )  # intervallet (1,2) overlapper ikke med intervallet (3,4), derfor returnerer funksjonen "False"
    print(
        f"intervallet (1, 3) overlapper med intervallet (3, 4): {overlapp_intervall(1, 3, 3, 4)}"
    )  # intervallet (1,3) er inntil men overlapper ikke med intervallet (3,4), derfor returnerer funksjonen "False"
    print(
        f"intervallet (1, 10) overlapper med intervallet (3, 11): {overlapp_intervall(1, 10, 3, 11)}"
    )  # intervallet (1,10) overlapper med intervallet (3,11), derfor returnerer funksjonen "True"

    print("")


if __name__ == "__main__":
    main()
