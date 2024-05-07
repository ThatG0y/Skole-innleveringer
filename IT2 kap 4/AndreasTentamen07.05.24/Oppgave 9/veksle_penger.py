def veksle_penger(seddel: int):
    if seddel >= 500:
        print("Over 500. Ikke gyldig.")
        return (0, 0, 0, 0)
    mynter = []
    kr = 20
    for i in range(3):  # sjekker 20, 10, og 5
        mynt = seddel // (kr)
        seddel = seddel % (kr)
        mynter.append(int(mynt))
        kr = kr / 2
    mynter.append(int(seddel))
    return tuple(mynter)
