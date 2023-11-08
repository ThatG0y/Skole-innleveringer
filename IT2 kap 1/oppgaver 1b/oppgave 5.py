temperatur = input("Skriv inn temperatur og enhet separert med mellomrom (20 C eller 24 F) ").split(" ")
if temperatur[1].lower() == "c":
    print(f"{temperatur[0]} {temperatur[1]} er lik {(float(temperatur[0])*1.8)+32} F")
elif temperatur[1].lower() == "f":
    print(f"{temperatur[0]} {temperatur[1]} er lik {(float(temperatur[0])-32)/1.8} C")