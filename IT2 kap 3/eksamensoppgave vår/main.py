import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os
import re


def hent_data(adresse: str) -> pd.DataFrame:
    data = pd.read_csv(adresse, sep=",", na_values=np.nan, encoding="utf-8-sig")
    return data


def oppgave_1(data: pd.DataFrame) -> None:
    top_tre = data["Category"].value_counts()[:3]

    print("De tre kategoriene med flest apper er:")
    for navn, antall in top_tre.items():
        kategori_data = data[data["Category"] == navn].copy()
        kategori_data["Installs"] = kategori_data["Installs"].map(fiks_tall)
        avg_rating = round(kategori_data["Rating"].mean(), 2)
        avg_inst = int(kategori_data["Installs"].mean())

        print(f"\n{navn}:\n")
        print(f"Antall apper: {antall:5}")
        print(f"Gjennomsnittlig rating: {avg_rating:5}")
        print(f"Gjennomsnittlig antall instalasjoner: {avg_inst:5}")


def oppgave_2(data: pd.DataFrame) -> None:
    top_tre = data["Category"].value_counts()[:3]

    for kategori in top_tre.index.to_list():

        kategori_data = data[data["Category"] == kategori][["App", "Installs"]]
        kategori_data["Installs"] = kategori_data["Installs"].map(fiks_tall)
        print(f"\nDe tre største appene innenfor kategorien '{kategori}':\n")
        for index, row in kategori_data.nlargest(3, "Installs").iterrows():
            print(f"{row['App']:17} : {row['Installs']:10}+ nedlastninger")


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


def fiks_tall(element: str) -> int:
    return int("".join(re.findall("\d", element)))


def main() -> None:
    adresse = os.path.join(os.path.abspath(os.path.dirname("")), r"googleplaystore.csv")
    data = hent_data(adresse)
    oppgave_1(data)
    oppgave_2(data)


if __name__ == "__main__":
    main()
