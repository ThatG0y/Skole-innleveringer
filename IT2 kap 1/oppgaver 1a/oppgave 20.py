def removeAllNonNumberCharacters(streng):
    streng = streng.replace(",", ".")
    if streng.count(".") > 1:
        print("too many dots")
        return ""
    else:
        # ord() returnerer unicode-koden til et gitt tegn,
        # som lar oss filtrere ut alle tegn i en streng som ikke er tall, punktum eller komma.
        # jeg bruker en kombinasjon av .join() og list-comprehension for å bygge opp strengen på nytt.
        ny_streng = ''.join([i if 47 < ord(i) < 58 or ord(
            i) == 44 or ord(i) == 46 else '' for i in streng])
        return float(ny_streng)


print(removeAllNonNumberCharacters("100 m"))
print(removeAllNonNumberCharacters("300 000 km/s"))
print(removeAllNonNumberCharacters("2,718 281 828 459 045"))
