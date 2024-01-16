import matplotlib.pyplot as plt

cmap = [
    "#4c2a85",
    "#6d435a",
    "#b1ede8",
    "#ff7700",
    "#6d435a",
    "#ff7700",
    "#b1ede8",
    "#8aea92",
    "#6d435a",
    "#8aea92",
    "#ff7700",
    "#8aea92",
    "#4c2a85",
]
klokkeslett = [
    "00:00-07:00",
    "07:00-08:00",
    "08:00-08:30",
    "08:30-11:50",
    "11:50-12:30",
    "12:30-15:50",
    "15:50-16:50",
    "16:50-17:40",
    "17:40-18:10",
    "18:10-18:30",
    "18:30-20:30",
    "20:30-23:00",
    "23:00-00:00",
]
døgnfordeling = [
    "Sove",
    "Frokost",
    "Buss til skole",
    "Skole",
    "Lunsj",
    "Skole",
    "Dra hjem",
    "Lager middag",
    "Spiser middag",
    "Andre gjøremål",
    "Lekser",
    "Fritid",
    "Sove",
]  # labels

timer = [
    7,
    1,
    1 / 2,
    3 + 1 / 3,
    2 / 3,
    3 + 1 / 3,
    1 + 1 / 2,
    5 / 6,
    1 / 2,
    1 / 3,
    2,
    2 + 1 / 2,
    1 / 2,
]  # values

fig, ax = plt.subplots(figsize=(9, 4))  # Angir dimensjoner for figure-objektet
label_l = [
    f"{døgnfordeling[i]}".ljust(15) + f"{klokkeslett[i]}".rjust(20)
    for i in range(len(timer))
]

ax.pie(
    timer,  # antall
    labels=døgnfordeling,  # også antall, men displayed som label
    wedgeprops={"linewidth": 1, "edgecolor": "white"},  # pynt
    colors=cmap,  # mer pynt
    startangle=90,
    counterclock=False,
)
fig.subplots_adjust(right=0.5)  # fikser proposjoner

fig.legend(  # legend på siden
    title="Klokkeslett for tidsfordeling av en skoledag: ",
    labels=label_l,
    loc="center right",
)
plt.title("En gjennomsnittlig skoledag", fontsize="15")
plt.show()
