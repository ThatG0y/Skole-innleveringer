import os
import json
from collections import defaultdict


def main() -> None:
    adresse = os.path.join(os.path.abspath(os.path.dirname("")), r"3b\todos.json")

    with open(adresse, encoding="utf-8-sig") as data:
        json_objekt = json.load(data)

    # undersøker...
    # print(json_objekt) viser at vi har et objekt med objekter, hvor hvert objekt har en bruker-id, oppgave-id, oppgave-tittel, og en completed-boolean

    oppgave_oversikt = json_objekt
    # subtask b (jeg tolker oppgaven som at de vil ha alle oppgave-titler)

    for oppgave in oppgave_oversikt:
        print(f"Oppgave {oppgave['id']:0>3}: {oppgave['title']}")

    # subtask c (tolker oppgaven som at jeg skal lage to lister over fullførte og ikke fullførte oppgaver, som alle har tilhørende id'er)
    fullførte_oppgaver = []
    ikke_fullførte_oppgaver = []
    for oppgave in oppgave_oversikt:
        if oppgave["completed"]:
            fullførte_oppgaver.append(oppgave["id"])
        else:
            ikke_fullførte_oppgaver.append(oppgave["id"])

    print("\nOppgaver som er fullførte:", end="\n\n")
    print(fullførte_oppgaver)
    print("\nOppgaver som ikke er fullførte:", end="\n\n")
    print(ikke_fullførte_oppgaver, end="\n\n")

    # subtask d

    bruker_score = defaultdict(lambda: 0)
    for oppgave in oppgave_oversikt:
        if oppgave["completed"]:
            bruker_score[oppgave["userId"]] += 1
    flest_poeng_bruker = max(bruker_score, key=bruker_score.get)
    print(
        f"Brukeren med mest score er 'bruker {flest_poeng_bruker}' med {bruker_score[flest_poeng_bruker]} poeng"
    )

    # subtask e

    minst_poeng_bruker = min(bruker_score, key=bruker_score.get)
    print(
        f"Brukeren med mest score er 'bruker {minst_poeng_bruker}' med {bruker_score[minst_poeng_bruker]} poeng"
    )


if __name__ == "__main__":
    main()
