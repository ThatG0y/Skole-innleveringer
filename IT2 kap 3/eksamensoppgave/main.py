import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import os


def hent_data(adresse: str) -> pd.DataFrame:
    data = pd.read_csv(adresse, sep=",", na_values=np.nan, encoding="unicode-escape")
    return data


def oppgave_1(data: pd.DataFrame) -> None:
    top_ti = data["Country"].value_counts()[:10]
    print("De ti landene med flest YT-kanaler er:")
    for navn, antall in top_ti.items():
        print(f"{navn:14} : {antall:4} subscribers")


def oppgave_2(data: pd.DataFrame) -> None:
    top_ti = data["Country"].value_counts()[:10]

    land_liste = top_ti.index.to_list()
    avg_ab_liste = []
    avg_v_liste = []

    for land in land_liste:
        land_data = data[data["Country"] == land]

        avg_ab = int(land_data["subscribers"].mean())
        avg_ab_liste.append(avg_ab)
        avg_v = int(land_data["video views"].mean())
        avg_v_liste.append(avg_v)

        print(f"\nGjennomsnitt i {land}: \n")
        print(f"Abonnenter     : {avg_ab}")
        print(f"Videovisninger : {avg_v}")

    grafisk_fremstilling(land_liste, avg_ab_liste, avg_v_liste)


def grafisk_fremstilling(
    keys: list[str], abonnenter: list[int], views: list[int]
) -> None:
    fig, axis = plt.subplots(1, 2, figsize=(10, 6))

    fig.suptitle("Gjennomsnittlig statistikk for Top 10 land på YouTube")
    plot_barh(axis[0], keys, abonnenter, "Gjennomsnittlige abonnenter", "plasma")
    plot_barh(axis[1], keys, views, "Gjennomsnitlige seertall", "viridis")
    fig.tight_layout()
    plt.show()


def plot_barh(
    ax: matplotlib.axes.Axes,
    x_verdier: list[int | str],
    y_verdier: list[int],
    title: str,
    cmap: str,
) -> None:
    farger = plt.get_cmap(cmap)
    ax.barh(
        x_verdier,
        y_verdier,
        color=farger([int(i * 256 / len(x_verdier)) for i in range(len(x_verdier))]),
    )
    ax.set_title(title)


def main() -> None:
    adresse = os.path.join(
        os.path.abspath(os.path.dirname("")), r"Global YouTube Statistics.csv"
    )
    data = hent_data(adresse)
    oppgave_1(data)
    oppgave_2(data)


if __name__ == "__main__":
    main()
