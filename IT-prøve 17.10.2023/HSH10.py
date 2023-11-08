def fizzBuzzSjekk(tall: int) -> str | int:
    """Fizzbuzz funksjonalitet

    Parameters
    ----------
    tall : int
        Et gitt tall

    Returns
    -------
    str | int
        Returnerer et tall hvis det gitte tallet ikke er delelig med 3 eller 5, returnerer en passende streng hvis tallet er delelig med 3 og/eller 5.
    """
    if not tall % (3 * 5):
        return "fizzbuzz"
    if not tall % 3:
        return "fizz"
    if not tall % 5:
        return "buzz"
    return tall


def fizzBuzzSpill(intervall_start: int, intervall_slutt: int) -> None:
    """Spiller fizzbuzz innenfor et gitt intervall.

    Parameters
    ----------
    intervall_start : int
        Startsverdien til intervallet. Er med i intervallet.
    intervall_slutt : int
        Sluttverdien til intervallet. Er ikke med i intervallet.
    """
    for tall in range(intervall_start, intervall_slutt):
        print(fizzBuzzSjekk(tall))


def main() -> None:
    fizzBuzzSpill(1, 30)


if __name__ == "__main__":
    main()
