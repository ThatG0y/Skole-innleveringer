tall = 0
alle_tall = []
while True:
    tall = input("Positivt heltall: ")
    try:
        tall = int(tall)
    except ValueError:
        print("Du må oppgi et positivt heltall.")
        tall = 0
        continue

    if tall > 10:
        break
    elif tall > 0 and tall <= 10:
        alle_tall.append(tall)
    else:
        print("Du må oppgi et positivt heltall.")

alle_tall.sort()

print(f"Det største tallet er lik {alle_tall[-1]}")
print(f"Det minste tallet er lik {alle_tall[0]}")
print(f"Summen av alle tallene er lik {sum(alle_tall)}")
print(f"Gjennomsnittet av alle tallene er lik {sum(alle_tall)/len(alle_tall)}")