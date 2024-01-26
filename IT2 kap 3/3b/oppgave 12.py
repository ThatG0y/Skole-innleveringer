import os
import json


def main() -> None:
    adresse = os.path.join(os.path.abspath(os.path.dirname("")), r"3b\skandinavia.json")

    with open(adresse, encoding="utf-8-sig") as data:
        land_data = json.load(data)

    # subtask a

    land = [land["navn"] for land in land_data["land"]]

    print(f"Landene i JSON-objektet er {land}")

    # subtask b

    byer_danmark = []
    for land in land_data["land"]:
        if land["navn"] == "Danmark":
            byer_danmark = land["byer"]

    print(f"Byene i Danmark er {byer_danmark}")

    # subtask c (oppgaven sier print en list, derfor skriver jeg ikke bare print(dict.items()))

    land_og_byer = {
        land["navn"]: land["byer"] for land in land_data["land"]
    }  # lager en dict som har et lands navn og tilhørende byer

    print(
        f"Alle land med tilhørende byer er {[list(item) for item in land_og_byer.items()]}"
    )

    # subtask d

    byer_på_a_i_danmark = []
    for land in land_data["land"]:
        if land["navn"] == "Danmark":  # sjekker at landet er Danmark
            for by in land["byer"]:
                if by.lower()[0] == "a":  # sjekker at første bokstav er 'A'
                    byer_på_a_i_danmark.append(by)
            break

    print(f"Byene i Danmark som starter på 'A' er {byer_på_a_i_danmark}")


if __name__ == "__main__":
    main()
