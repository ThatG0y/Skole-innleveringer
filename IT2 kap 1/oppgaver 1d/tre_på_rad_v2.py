sidelengde = 16
brett = [
    ["*" for _ in range(sidelengde)] for _ in range(sidelengde)
]  # lager informasjons-brettn


def lag_blank_rad(brett):  # lager blanke rader for GUI
    lengde = len(brett)
    blank = "|-|"
    for _ in range(lengde - 1):
        blank += "---|-|"
    return blank


def vis_brett(brett):  # oppdaterer GUI
    blank = lag_blank_rad(brett)
    for index in range(len(brett)):
        rad = "".join(f"|{celle}|   " for celle in brett[index])
        print(rad)
        if index + 1 < len(brett):
            print(blank)


def sjekk_vinn(
    spiller_symbol, brett
):  # sjekker om spilleren har vunnet, og avslutter programmet hvis noen vinner
    kolonner = brett[:]
    rader = [list(rad) for rad in [*zip(*brett)]]
    diagonal_lr = [brett[i][i] for i in range(len(brett))]
    diagonal_rl = [brett[i][-(i + 1)] for i in range(len(brett))]
    if sjekk_full_rekke(spiller_symbol, *kolonner, *rader, diagonal_lr, diagonal_rl):
        print(f"Spiller '{spiller_symbol}' har vunnet")
        exit()


def sjekk_full_rekke(
    spiller_symbol, *args
):  # sjekker alle rekker i brettn etter en "vunnet" rekke
    for rekke in args:
        if rekke.count(spiller_symbol) == len(rekke):
            return True
    return False


def main():  # lets the player give input, and checks input for bugs. Uses other funsctions to run the actual game
    vis_brett(brett)
    for i in range(len(brett) ** 2):
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
            if x > len(brett) or y > len(brett) or x < 0 or y < 0:
                print(
                    f"Your input is out of range, matrix is a {len(brett)}x{len(brett)} grid"
                )
                continue

            if brett[-y][x - 1] != "*":
                print(f"The cell ({x}, {y}) is taken, try another: ")
                continue

            brett[-y][x - 1] = spiller
            vis_brett(brett)
            sjekk_vinn(spiller, brett)
            break
    print("Uavgjort")


if __name__ == "__main__":
    main()
