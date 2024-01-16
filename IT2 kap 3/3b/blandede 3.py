import pandas as pd
import matplotlib.pyplot as plt

adresse = r"C:\Users\opdah\OneDrive - Akademiet Norge AS\2023-2024 Skolefag\IT\for git\IT2 kap 3\3b\fritidsboliger_moh_2019.csv"
data = pd.read_csv(adresse, sep=";", header=None, index_col=0)
titles = data.index

fig, ax = plt.subplots(figsize=(10, 5))  # Angir dimensjoner for figure-objektet

# x = data.loc[titles[0]].values
# y = list(map(int, data.loc[titles[1]].values))

x_mer = "Over 1000 m"
y_mer = sum(list(map(int, data.loc[titles[1]].values))[14:])

data = data.drop(
    [i for i in range(14, len(data.loc[titles[0]].values) + 1)], axis="columns"
)
data[14] = pd.Series(data=[x_mer, y_mer], index=titles)
lengde = len(data.loc[titles[0]].values)
# data = data.assign(lengde=[x_mer, y_mer])

oppdeling = [
    int(256 / (lengde) * i) for i in range((lengde))
]  # gjør at cmap fordeler farger jevnt

cmap = plt.get_cmap("viridis")(oppdeling)  # plottets farger

ax.barh(
    data.loc[titles[0]].values,
    list(map(int, data.loc[titles[1]].values)),
    color=cmap,
)  # Lager stolpediagram jenter

plt.xlabel(titles[1])
plt.ylabel(titles[0])


plt.title("Høyde over havet for norske fritidsboliger (hytter)", fontsize="15")

plt.grid(axis="x", linestyle="--")
plt.show()
