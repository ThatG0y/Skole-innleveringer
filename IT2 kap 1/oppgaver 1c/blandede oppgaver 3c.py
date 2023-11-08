import random
alle_terningkast = []
while True:
    antall_terninger = input("Antall terninger: ")
    try:
        antall_terninger = int(antall_terninger)
    except ValueError:
        print("Du må oppgi et positivt heltall.")
        continue
    for i in range(antall_terninger+1):
        alle_terningkast.append(random.randint(1,6))

    print(f"Summen av alle tallene er lik {sum(alle_terningkast)}")
    print(f"Gjennomsnittet av alle tallene er lik {sum(alle_terningkast)/len(alle_terningkast)}")
    break