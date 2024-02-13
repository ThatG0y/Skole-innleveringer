import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os


def hent_data(adresse: str) -> pd.DataFrame:
    data = pd.read_csv(adresse, sep=",", na_values=np.nan, encoding="unicode-escape")
    return data


def oppgave_1(data: pd.DataFrame) -> None:
    top_ti = data["Country"].value_counts()[:10]
    print("De ti landene med flest YT-kanaler er:")
    for navn, antall in top_ti.items():
        print(f"{navn} med {antall} subscribers")


def oppgave_2(data: pd.DataFrame) -> None:
    top_ti = data["Country"].value_counts()[:10]
    print(top_ti.index)


def main() -> None:
    adresse = os.path.join(
        os.path.abspath(os.path.dirname("")), r"Global YouTube Statistics.csv"
    )
    data = hent_data(adresse)
    # oppgave_1(data)
    oppgave_2(data)


if __name__ == "__main__":
    main()
