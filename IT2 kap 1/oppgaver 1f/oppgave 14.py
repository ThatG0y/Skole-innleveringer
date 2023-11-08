def tell_ord_i_rekke(tekst: str) -> int:
    """Teller antall forekomster av et ord i en tekst

    Parameters
    ----------
    tekst : str
        teksten man vil telle antall forekomster av ordet i
    Returns
    -------
    int
        antall forekomster
    """
    while True:
        ord = input("Søk etter ord i tekst: ")
        if len(ord.split(" ")) > 1:
            print("Input ikke godtatt. Kun ett ord av gangen")
            continue
        return tekst.lower().count(ord.lower())


def main() -> None:
    lang_tekst = "Det er fire offisielle spillmoduser: osu! (kalt osu! standard), osu!taiko, osu!catch og osu!mania. Med tillegg av osu!lazer kan spillere nå legge til egendefinerte spillmodi til osu! klient.[6][7] Den originale osu!standardmodusen er fortsatt den mest populære til dags dato, og fra januar 2023 har spillet over 19,3 millioner månedlige aktive brukere i henhold til spillets globale toppliste for land.[8] osu!standard henter direkte inspirasjon fra Osu! Tatakae! Ouendan-spill. I denne spillmodusen klikker spilleren sirkler i takt med en sang. Dette er flaggskipsspillmodusen på Osu! nettsted.[9] osu!mania er et vertikalt rullende rytmespill som stort sett henter inspirasjon fra Beatmania. Spillmodusen består av toner som faller vertikalt i forskjellige baner, med én tast som brukes til å trykke for hver bane.[10] osu!taiko simulerer å spille på taiko og er basert på Taiko no Tatsujin.[11] Den siste spillmodusen, osu!catch, er basert på EZ2CATCH, som var en del av EZ2DJ-kabinettet. I denne spillmodusen flytter spilleren en catcher til venstre eller høyre for å fange frukt som faller fra toppen av skjermen.[9][bedre kilde nødvendig] Hver modus tilbyr en rekke beatmaps, som er spillnivåer som spilles til sanger av forskjellige lengder, alt fra TV-størrelse anime-åpninger til maraton som overgår 7 minutter. I osu!standard består beatmaps av tre elementer: treffsirkler, skyveknapper og spinnere. Målet med spillet er at spilleren skal klikke på disse elementene i takt med musikken. Disse gjenstandene er samlet kjent som treffobjekter eller sirkler og er arrangert i forskjellige posisjoner på skjermen (bortsett fra spinneren) på forskjellige tidspunkt i løpet av en sang. Taiko beatmaps har trommeslag og spinnere. Catch beatmaps har frukt og spinnere (som er bananer), som er arrangert på en horisontalt fallende måte. Mania beatmaps består av taster (avbildet som en liten stolpe) og hold. Beatmapet spilles deretter med tilhørende musikk, og simulerer en følelse av rytme når spilleren samhandler med objektene i takt med musikken.[12][13] Hvert beatmap er akkompagnert av musikk og en bakgrunn (som kan deaktiveres). Spillet kan spilles ved hjelp av forskjellige eksterne enheter: det vanligste oppsettet er et grafikknettbrett eller en datamus for å kontrollere markørbevegelsen, sammenkoblet med et tastatur[14][5] eller et minitastatur med bare to taster, og bare tastaturet for osu !taiko, osu!catch og osu!mania beatmaps. Spillet tilbyr en kjøpbar utvidelsestjeneste kalt osu!supporter, som gir ekstra funksjoner til brukeren.[15] osu!supporter påvirker ikke rangeringssystemet eller gir noen fordeler i spillet. Mens osu!supporter i seg selv ikke er en gjentakende tjeneste (som betyr at det er en engangsbetaling), har den en begrenset gyldighetstid fra 1 måned til 2 år; Imidlertid kan flere kjøp av osu!supporter-tjenestetid gi rett til én bruker, noe som gir lengre uavbrutt tjeneste."
    print(f"Det er {tell_ord_i_rekke(lang_tekst)} tilfeller av det ordet i teksten")


if __name__ == "__main__":
    main()
