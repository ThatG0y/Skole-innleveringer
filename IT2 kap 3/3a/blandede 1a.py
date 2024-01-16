import matplotlib.pyplot as plt
import numpy as np

karakterer = [
    5,
    3,
    6,
    3,
    5,
    1,
    2,
    2,
    2,
    4,
    2,
    2,
    5,
    5,
    6,
    3,
    5,
    3,
    5,
    4,
    2,
    6,
    1,
    4,
    2,
    3,
    3,
    3,
    5,
    5,
]
karakterer_label = set(karakterer)
fig, ax = plt.subplots(figsize=(5, 5))  # Angir dimensjoner for figure-objektet

oppdeling = [int(256 / len(karakterer_label) * i) for i in range(len(karakterer_label))]

cmap = plt.get_cmap("viridis")(oppdeling)

ax.bar(
    list(karakterer_label),
    [karakterer.count(i) for i in karakterer_label],
    color=cmap,
    edgecolor="white",
)
plt.xlabel("Karakter")
plt.ylabel("Antall elever")


plt.title("Klassens karakterer", fontsize="15")

# fig.subplots_adjust(left=0.4)  # Øker plassen på venstre side av diagrammet

plt.show()  # Viser diagrammet
