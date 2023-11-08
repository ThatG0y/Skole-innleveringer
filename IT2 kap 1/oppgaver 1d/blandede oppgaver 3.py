liste = []
while len(liste) < 10:
    heltall = input("Positivt heltall: ")
    try:
        heltall = int(heltall)
    except ValueError:
        print("Du må oppgi et positivt heltall.")
        continue
    if heltall in liste:
        print(f"{heltall} fins i listen fra før, prøv igjen :)")
    else:
        liste.append(heltall)
print(liste)
