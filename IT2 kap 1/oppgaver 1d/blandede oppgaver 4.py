import random


def finn_median(liste=list):
    liste.sort()
    if len(liste) % 2:
        return liste[round(len(liste) / 2)]
    else:
        return (liste[int(len(liste) / 2) - 1] + liste[int(len(liste) / 2)]) / 2


liste1 = [random.randint(1, 100) for i in range(50)]
liste2 = [random.randint(1, 100) for i in range(25)]

print(finn_median(liste1))
print(finn_median(liste2))
