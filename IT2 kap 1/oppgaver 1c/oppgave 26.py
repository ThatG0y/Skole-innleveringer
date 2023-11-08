karaktersnitt = 0
while karaktersnitt <1 or karaktersnitt > 6:
    
    karaktersnitt = input("Oppgi karaktersnittet ditt. Desimaltall skrives med punktum: ")
    try:
        karaktersnitt = float(karaktersnitt)
    except ValueError:
        print("Du må oppgi et tall mellom 1 og 6, pass på ett punktum i desimaltall!")
        karaktersnitt = 0
        continue
    
    if karaktersnitt >= 1 and karaktersnitt <= 6:
        print(f"Ditt karaktersnitt er {karaktersnitt}.")
    else:
        print("Du må oppgi et tall mellom 1 og 6.")