maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes"
def finn_maaned(maanedtall):
    if not 0<maanedtall<12 or type(maanedtall) != int:
        print("misinput")
        return ""
    maaneindeks=0
    for indeks, letter in enumerate(maaneder):
        if letter.isupper():
            maaneindeks+=1
        if maaneindeks==maanedtall:
            return maaneder[indeks:indeks+3]

if __name__ == "__main__":
    print("Katt "[4])
    maanedtall = int(input("Hvilken måned vil du vite forkortelsen til? "))
    print(f"Den månedens forkortelse er {finn_maaned(maanedtall)}")
