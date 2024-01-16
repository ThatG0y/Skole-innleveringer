import matplotlib.pyplot as plt

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
]  # labels

antall = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]  # values

utdanningsdict = {
    utdanningsprogram[i]: antall[i] for i in range(len(antall))
}  # labels: values
utdanningsdict = {
    k: v for k, v in sorted(utdanningsdict.items(), key=lambda item: item[1])
}  # labels: values (sortert)

oppdeling = [
    int(256 / len(antall) * i) for i in range(len(antall))
]  # gjør at cmap fordeler farger jevnt

cmap = plt.get_cmap("viridis_r")(oppdeling)  # plottets farger

fig, ax = plt.subplots(figsize=(9, 4))  # Angir dimensjoner for figure-objektet

ax.pie(
    utdanningsdict.values(),  # antall
    labels=utdanningsdict.values(),  # også antall, men displayed som label
    wedgeprops={"linewidth": 1, "edgecolor": "white"},  # pynt
    colors=cmap,  # mer pynt
)
fig.subplots_adjust(right=0.5)  # fikser proposjoner
fig.legend(  # legend på siden
    title="Antall søkere for ulike VGS-linjer:",
    labels=utdanningsdict.keys(),
    loc="center right",
)

plt.show()
