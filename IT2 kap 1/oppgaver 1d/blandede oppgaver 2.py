import random

liste = [random.randint(1, 100) for i in range(50)]
liste.sort()
print(f"{[partall for partall in liste if partall%2==0]}")
print(f"{[oddetall for oddetall in liste if oddetall%2]}")
print(f"{[liste[tall] for tall in range(0,len(liste),2)]}")
print(f"{liste[::-1]}")
