import osmnx as ox
import folium as fol

# Byenes koordinater
punkter = [
    [59.9139, 10.7522],  # Oslo
    [55.6761, 12.5683],  # København
    [59.3293, 18.0686],  # Stockholm
]

# Beregner snittet av breddegrader og lengdegrader for å finne
# et punkt midt mellom alle byene.
bredde_sum = 0
lengde_sum = 0

for punkt in punkter:
    bredde_sum += punkt[0]
    lengde_sum += punkt[1]

bredde_snitt = bredde_sum / len(punkter)
lengde_snitt = lengde_sum / len(punkter)

# Lager et kart
m = fol.Map([bredde_snitt, lengde_snitt], zoom_start=6)

# Legger til byene
for punkt in punkter:
    fol.CircleMarker(punkt).add_to(m)

# Lagrer kartet
m.save("skandinavia.html")
