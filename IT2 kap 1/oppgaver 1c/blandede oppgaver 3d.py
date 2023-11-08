import random
alle_terningkast = []
while True:
    antall_terningkast = input("Antall terningkast: ")
    try:
        antall_terningkast = int(antall_terningkast)
    except ValueError:
        print("Du må oppgi et positivt heltall.")
        continue
    for i in range(antall_terningkast+1):
        alle_terningkast.append((random.randint(1,6)+random.randint(1,6)))

    print(f"Summen av alle tallene er lik {sum(alle_terningkast)}")
    print(f"Gjennomsnittet av alle tallene er lik {sum(alle_terningkast)/len(alle_terningkast)}")
    break