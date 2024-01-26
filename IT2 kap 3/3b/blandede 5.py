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
    flest_poeng = bruker_score[max(bruker_score, key=bruker_score.get)]
    flest_poeng_bruker = []
    for bruker in bruker_score.items():
        if bruker[1] == flest_poeng:
            flest_poeng_bruker.append(bruker[0])
    print(
        f"Brukeren(e) med mest score er 'bruker(e) {flest_poeng_bruker}' med {flest_poeng} poeng"
    )

    # subtask e
    minst_poeng = bruker_score[min(bruker_score, key=bruker_score.get)]
    minst_poeng_bruker = []
    for bruker in bruker_score.items():
        if bruker[1] == minst_poeng:
            minst_poeng_bruker.append(bruker[0])
    print(
        f"Brukeren(e) med mest score er 'bruker(e) {minst_poeng_bruker}' med {minst_poeng} poeng"
    )


if __name__ == "__main__":
    main()
