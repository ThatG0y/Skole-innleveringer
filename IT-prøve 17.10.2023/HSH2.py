def summerTallListe(tall_liste: list[int]) -> int:
    tall_sum = 0
    for tall in tall_liste:
        if tall == 1:
            tall_sum += 1
    return tall_sum


def main() -> None:
    tall_liste = [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0]
    tall_sum = sum(tall_liste)  # alternativ 1
    tall_sum = summerTallListe(tall_liste)  # alternativ 2
    print(f"Summen av lista {tall_liste} er {tall_sum}")


if __name__ == "__main__":
    main()
