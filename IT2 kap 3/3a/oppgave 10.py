import matplotlib.pyplot as plt
import numpy as np

utdanningsprogram = [
    "Bygg- og anleggsteknikk",
    "Elektro og datateknologi",
    "Helse- og oppvekstfag",
    "Naturbruk",
    "Restaurant- og matfag",
    "Teknologi- og industrifag",
    "Håndverk, design og produktutvikling",
    "Frisør, blomster, interiør og eksponeringsdesign",
    "Informasjonsteknologi og medieproduksjon",
    "Salg, service og reiseliv",
]

antall = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]

fig, ax = plt.subplots(
    figsize=(10, 5),
)


oppdeling = [int(256 / len(antall) * i) for i in range(len(antall))]

cmap = plt.get_cmap("viridis")(oppdeling)

bars = ax.barh(
    utdanningsprogram,
    antall,
    color=cmap,
    height=0.9,
    edgecolor="white",
    linewidth=0.1,
)  # Lager stolpediagrammet
# ax.set_facecolor("0.9")
fig.subplots_adjust(
    left=0.4,
)  # Øker plassen på venstre side av diagrammet
plt.title("Antall søkere for ulike VGS-linjer", fontsize="15")
plt.grid(
    axis="x",
    linestyle="--",
)  # Legger til rutenett (bare vertikale linjer)
plt.show()  # Viser diagrammet
