import random
import matplotlib.pyplot as plt
import itertools
from overlapp_oppgave_del_1 import overlapp_intervall

# egendefinerte typer
Tall = int | float
Firkant = tuple[Tall, Tall, Tall, Tall]


# ekstra
def overlapp_firkant(
    x1: Tall, y1: Tall, x2: Tall, y2: Tall, x3: Tall, y3: Tall, x4: Tall, y4: Tall
) -> (
    bool
):  # punktene (x1,y1) og (x2,y2) markerer punktene A og C i firkanten ABCD, punktene (x3,y3) og (x4,y4) markerer punktene E og G i firkanten EFGH
    """Sjekker om to firkanter overlapper,
    returnerer True dersom firkantene overlapper, ellers False

    Parameters
    ----------
    x1 : Tall
        x-koordinatet til hjørnet nede til venstre på den første firkanten
    y1 : Tall
        y-koordinatet til hjørnet nede til venstre på den første firkanten
    x2 : Tall
        x-koordinatet til hjørnet oppe til høyre på den første firkanten
    y2 : Tall
        y-koordinatet til hjørnet oppe til høyre på den første firkanten
    x3 : Tall
        x-koordinatet til hjørnet nede til venstre på den andre firkanten
    y3 : Tall
        y-koordinatet til hjørnet nede til venstre på den andre firkanten
    x4 : Tall
        x-koordinatet til hjørnet oppe til høyre på den andre firkanten
    y4 : Tall
        y-koordinatet til hjørnet oppe til høyre på den andre firkanten

    Returns
    -------
    bool
        Sier om firkantene overlapper
    """
    if overlapp_intervall(x1, x2, x3, x4) and overlapp_intervall(y1, y2, y3, y4):
        return True
    else:
        return False


def sjekk_overlapp_firkanter(firkanter: list[tuple[str, Firkant]]) -> None:
    """Sjekker alle gitte firkanter for om de overlapper med hverandre

    Parameters
    ----------
    firkanter : list[tuple[str, Firkant]]
        en liste med tuples med navn og verdi for hver firkant
    """
    for firkant1, firkant2 in itertools.combinations(firkanter, 2):
        if overlapp_firkant(*firkant1[1], *firkant2[1]):
            print(f"{firkant1[0]} og {firkant2[0]} overlapper")


def lag_tilfeldig_firkant() -> Firkant:
    """Lager en tilfeldig firkant

    Returns
    -------
    Firkant
        Den tilfeldige firkanten som blir generert
    """
    return sorted(
        random.sample(range(1, 51), 4)
    )  # sorted sørger for at firkantenes punktkoordinater blir korrekte


def visualisering_av_overlapping(
    firkanter: list[tuple[str, Firkant]]
) -> None:  # tar inn "firkant" lister på formen [x1,y1,x2,x2]
    """Lager en visuell framstilling av overlappende firkanter ved hjelp av matplotlib

    Parameters
    ----------
    firkanter : list[tuple[str, Firkant]]
        en liste med tuples med navn og verdi for hver firkant
    """
    plt.axes()
    cmap = plt.get_cmap("PiYG", len(firkanter))  # lager farger
    for index, firkant in enumerate(firkanter):
        x1, y1, x2, y2 = firkant[1]
        color = list(cmap(index))
        color[-1] -= 0.7  # gir alfakanal lik 0.3
        firkant = plt.Polygon(
            [[x1, y1], [x2, y1], [x2, y2], [x1, y2]],
            fc=color,  # fillcolor
            ec=(0, 0, 0),  # edgecolor
            label=firkant[0],
        )
        plt.gca().add_patch(firkant)
    plt.axis("scaled")
    plt.legend()
    plt.show()


def main():
    # testverdier
    firkanter_org = [
        ("firkant1", [1, 1, 5, 5]),
        ("firkant2", [5, 1, 6, 3]),
        ("firkant3", [2, 2, 6, 6]),
        ("firkant4", [1, 1, 2, 2]),
    ]
    firkanter_tilfeldig = [
        (f"firkant{len(firkanter_org)+(i+1)}", lag_tilfeldig_firkant())
        for i in range(len(firkanter_org))  # tilfeldige firkanter
    ]

    sjekk_overlapp_firkanter(firkanter_org)
    visualisering_av_overlapping(firkanter_org)

    print("")

    sjekk_overlapp_firkanter(firkanter_tilfeldig)
    visualisering_av_overlapping(firkanter_tilfeldig)


if __name__ == "__main__":
    main()
