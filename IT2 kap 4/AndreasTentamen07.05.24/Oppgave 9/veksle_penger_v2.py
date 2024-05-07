from veksle_penger import veksle_penger


def veksle_penger_v2(beløp):
    if beløp % 50 == 0 and beløp != 0:
        return veksle_penger(beløp)
    else:
        print("Ikke gyldig seddel-beløp")
        return (0, 0, 0, 0)
