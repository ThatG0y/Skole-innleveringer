import json

Prisoversikt = dict[str, dict[str, int]]


def hent_json_fil(path: str) -> dict:
    with open(path) as d:
        return json.load(d)


def finnButikk(
    handleliste: list[str], butikkliste: list[str], prisoversikt: Prisoversikt
) -> str:
    butikkpriser = {
        butikknavn: sum(prisoversikt[butikknavn][vare] for vare in handleliste)
        for butikknavn in butikkliste
    }
    lavest_pris = min(butikkpriser.values())
    return [
        butikknavn
        for butikknavn in butikkpriser.keys()
        if butikkpriser[butikknavn] == lavest_pris
    ]


def unit_tests() -> None:
    assert finnButikk(
        ["salat", "melk", "fisk", "brod"],
        ["Rema1000", "Meny", "Kiwi", "Spar", "Joker"],
        hent_json_fil("prac\handletur_oppgave_json.json"),
    ) == ["Meny"]
    assert finnButikk(
        ["salat", "melk", "fisk"],
        ["Rema1000", "Meny", "Kiwi", "Spar", "Joker"],
        hent_json_fil("prac\handletur_oppgave_json.json"),
    ) == ["Spar"]
    assert finnButikk(
        ["salat", "melk"],
        ["Rema1000", "Meny", "Kiwi", "Spar", "Joker"],
        hent_json_fil("prac\handletur_oppgave_json.json"),
    ) == ["Kiwi"]
    assert finnButikk(
        ["salat"],
        ["Rema1000", "Meny", "Kiwi", "Spar", "Joker"],
        hent_json_fil("prac\handletur_oppgave_json.json"),
    ) == ["Kiwi"]


def main() -> None:
    prisliste = [
        {"salat": 12, "fisk": 99, "melk": 12, "brod": 12},
        {"salat": 22, "fisk": 60, "melk": 18, "brod": 21},
        {"salat": 8, "fisk": 120, "melk": 10, "brod": 19},
        {"salat": 18, "fisk": 40, "melk": 30, "brod": 59},
        {"salat": 15, "fisk": 200, "melk": 40, "brod": 9},
    ]

    # bedre lagringsalternativ til prisListe
    prisdict = {
        "Rema1000": {"salat": 12, "fisk": 99, "melk": 12, "brod": 12},
        "Meny": {"salat": 22, "fisk": 60, "melk": 18, "brod": 21},
        "Kiwi": {"salat": 8, "fisk": 120, "melk": 10, "brod": 19},
        "Spar": {"salat": 18, "fisk": 40, "melk": 30, "brod": 59},
        "Joker": {"salat": 15, "fisk": 200, "melk": 40, "brod": 9},
    }
    # det samme men fra json
    prisdict = hent_json_fil("prac\handletur_oppgave_json.json")

    butikker = ["Rema1000", "Meny", "Kiwi", "Spar", "Joker"]

    handleliste = ["salat", "fisk"]

    print(
        f"Det er billigst å handle på {finnButikk(handleliste, butikker, prisdict)} når man handler {handleliste}"
    )
    unit_tests()


if __name__ == "__main__":
    main()
