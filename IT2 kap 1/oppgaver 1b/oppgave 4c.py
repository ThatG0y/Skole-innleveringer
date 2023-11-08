tall = input("Skriv inn 3 tall separert med mellomrom (1 2 3): ").split(" ")
tall = [int(i) for i in tall]
tall.sort()
høyest_tall = tall[-1]

if tall[1] == tall[2]:
    if tall[0]== tall[1]:
        print(f"Alle tallene er like, og svaret er {høyest_tall}")
    else:
        print(f"De to høyeste tallene er like, og svaret er {høyest_tall}")
else:
    print(f"Det høyeste tallet er {høyest_tall}")    