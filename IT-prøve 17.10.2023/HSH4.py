import random as rd


def main() -> None:
    tilfeldig_tall_liste = [rd.randint(1, 10) for _ in range(1, 20)]
    tall_sum = sum(tilfeldig_tall_liste)
    print(f"Summen av lista {tilfeldig_tall_liste} er {tall_sum}")


if __name__ == "__main__":
    main()
