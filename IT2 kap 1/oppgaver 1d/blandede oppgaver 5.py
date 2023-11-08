sidelengde = 3
matrise = [
    ["*" for _ in range(sidelengde)] for _ in range(sidelengde)
]  # lager informasjons-matrisen


def lag_blank_rad(matrise):  # lager blanke rader for GUI
    lengde = len(matrise)
    blank = "|-|"
    for _ in range(lengde - 1):
        blank += "---|-|"
    return blank


def vis_matrise(matrise):  # oppdaterer visuals
    blank = lag_blank_rad(matrise)
    for index in range(len(matrise)):
        rad = "".join(f"|{celle}|   " for celle in matrise[index])
        print(rad)
        if index + 1 < len(matrise):
            print(blank)


def sjekk_vinn(
    spiller_symbol, matrise
):  # sjekker om spilleren har vunnet, og avslutter programmet hvis noen vinner
    kolonner = matrise[:]
    rader = [list(rad) for rad in [*zip(*matrise)]]
    diagonal_lr = [matrise[i][i] for i in range(len(matrise))]
    diagonal_rl = [matrise[i][-(i + 1)] for i in range(len(matrise))]
    if sjekk_full_rekke(spiller_symbol, *kolonner, *rader, diagonal_lr, diagonal_rl):
        print(f"Spiller '{spiller_symbol}' har vunnet")
        exit()


def sjekk_full_rekke(
    spiller_symbol, *args
):  # sjekker alle rekker i matrisen etter en "vunnet" rekke
    for rekke in args:
        if rekke.count(spiller_symbol) == len(rekke):
            return True
    return False


def main():  # lets the player give input, and checks input for bugs. Uses other funsctions to run the actual game
    vis_matrise(matrise)
    for i in range(len(matrise) ** 2):
        spiller = "x" if i % 2 == 0 else "o"
        while True:
            koordinat = input("Velg celle (x,y): ")
            koordinat = koordinat.replace(".", ",")
            koordinat = "".join(
                [
                    i if 47 < ord(i) < 58 or ord(i) == 44 or ord(i) == 46 else ""
                    for i in koordinat
                ]
            )
            try:
                x, y = map(int, koordinat.split(","))
            except ValueError:
                print(
                    "Invalid input: Expected ',' as separator and two whole number inputs"
                )
                continue
            if x > len(matrise) or y > len(matrise) or x < 0 or y < 0:
                print(
                    f"Your input is out of range, matrix is a {len(matrise)}x{len(matrise)} grid"
                )
                continue

            if matrise[-y][x - 1] != "*":
                print(f"The cell ({x}, {y}) is taken, try another: ")
                continue

            matrise[-y][x - 1] = spiller
            vis_matrise(matrise)
            sjekk_vinn(spiller, matrise)
            break
    print("Uavgjort")


if __name__ == "__main__":
    main()
