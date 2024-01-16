import matplotlib.pyplot as plt
import numpy as np

årstall = [  # årstall
    2021,
    2017,
    2013,
    2009,
    2005,
    2001,
    1997,
    1993,
    1989,
    1985,
]

høyre = [  # verdier
    36,
    45,
    48,
    41,
    38,
    38,
    23,
    28,
    37,
    50,
]
ap = [  # verdier
    48,
    49,
    55,
    64,
    61,
    43,
    65,
    67,
    63,
    71,
]

fig, ax = plt.subplots(figsize=(8, 5))  # Angir dimensjoner for figure-objektet

y = np.arange(10)

ax.barh(
    y - 0.2, ap, height=0.4, label="Arbeiderpartet", color="red"
)  # Lager stolpediagram ap
ax.barh(
    y + 0.2, høyre, height=0.4, label="Høyre", color="blue"
)  # Lager stolpediagram høyre
ax.set_yticks(y, årstall)  # Legger til akseverdier
ax.legend()  # Legger til beskrivelse
plt.title("Antall årlige stortingsrepresentanter: H og AP", fontsize="15")

# fig.subplots_adjust(left=0.4)  # Øker plassen på venstre side av diagrammet

ax.grid(axis="x", linestyle="--")  # Legger til rutenett (bare vertikale linjer)
plt.show()  # Viser diagrammet
