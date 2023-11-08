alder = -1
while  alder<=0:
    
    alder = input("Oppgi alderen din: ")
    try:
        alder = int(alder)
    except ValueError:
        print("Du må oppgi et positivt heltall")
        alder = -1
        continue
    
    if alder > 0:
        print(f"Du er {alder} år.")
    else:
        print("Du må oppgi et positivt heltall")