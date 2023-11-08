maanednr = 0
while maanednr <1 or maanednr > 12:
    
    maanednr = input("Oppgi nummeret til måneden vi er i ")
    try:
        maanednr = int(maanednr)
    except ValueError:
        print("Du må oppgi et heltall mellom 1 og 12")
        maanednr = 0
        continue
    
    if maanednr >= 1 and maanednr <= 12:
        print(f"Du skrev inn {maanednr}.")
    else:
        print("Du må oppgi et tall mellom 1 og 12.")