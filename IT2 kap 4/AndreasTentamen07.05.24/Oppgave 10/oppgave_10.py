import pandas as pd
import matplotlib.pyplot as plt


def hent_data():
    url = r"Oppgave 10\utgifter.csv"
    return pd.read_csv(url, sep=";", skiprows=1).fillna(0)


def fiks(dato: str):
    dag, måned, år = dato.split(".")
    return int(måned)


def deloppgave_a():
    data = hent_data()
    print("Totale utgifter: ")
    mat = data[data["Type"] == "mat"]
    klær = data[data["Type"] == "klær"]
    strøm = data[data["Type"] == "strøm"]
    print(f"Penger brukt på mat: {mat['Beløp'].sum()}")
    print(f"Penger brukt på klær: {klær['Beløp'].sum()}")
    print(f"Penger brukt på strøm: {strøm['Beløp'].sum()}")
    print()


def deloppgave_b():
    data = hent_data()
    måneder = {1: "Januar", 2: "Februar", 3: "Mars"}
    for i in range(3):
        print(f"{måneder[i + 1]}:")
        mån_data = data[data["Dato"].map(fiks) == i + 1]
        print(
            f"Penger brukt på mat: {int(sum(mån_data[mån_data['Type']=='mat']['Beløp']))}"
        )
        print(
            f"Penger brukt på klær: {int(sum(mån_data[mån_data['Type']=='klær']['Beløp']))}"
        )
        print(
            f"Penger brukt på strøm: {int(sum(mån_data[mån_data['Type']=='strøm']['Beløp']))}"
        )
        print()


def deloppgave_b_org():
    måneder = {1: "Januar", 2: "Februar", 3: "Mars"}
    data = hent_data()
    for i in range(3):
        print(f"{måneder[i+1].title()}: ")
        avgifter = {"mat": 0, "klær": 0, "strøm": 0}
        for element in data.iterrows():
            if int(element[1]["Dato"].split(".")[1]) == i + 1:
                avgifter[element[1]["Type"]] = element[1]["Beløp"]
        print(f"Penger brukt på mat: {avgifter['mat']}")
        print(f"Penger brukt på klær: {avgifter['klær']}")
        print(f"Penger brukt på strøm: {avgifter['strøm']}")
        print()


def deloppgave_c():
    data = hent_data()
    plt.bar(
        ["Januar", "Februar", "Mars"],
        [
            sum(data[data["Dato"].map(fiks) == i + 1][data["Type"] != "strøm"]["Beløp"])
            for i in range(3)
        ],
        color=["red", "blue", "green"],
    )
    plt.title("Sum hverdagsavgifter")
    plt.xlabel("Måned")
    plt.ylabel("Antall kr")
    plt.show()


def deloppgave_c_org():
    måneder = {1: "januar", 2: "februar", 3: "mars"}
    data = hent_data()
    y_verdier = []
    for i in range(3):
        avgifter = {"mat": 0, "klær": 0}
        for element in data.iterrows():
            if (
                int(element[1]["Dato"].split(".")[1]) == i + 1
                and element[1]["Type"] != "strøm"
            ):
                avgifter[element[1]["Type"]] = element[1]["Beløp"]
        y_verdier.append(int(sum(avgifter.values())))
    plt.bar(måneder.values(), y_verdier, color=["red", "blue", "green"])
    plt.title("Sum hverdagsavgifter")
    plt.xlabel("Måned")
    plt.ylabel("Antall kr")
    plt.show()


def deloppgave_d():
    data = hent_data()
    fast_utgift = data[data["Type"] == "strøm"]
    hverdagsutgift = data[data["Type"] != "strøm"]
    plt.pie(
        [
            fast_utgift["Beløp"].sum(),
            hverdagsutgift["Beløp"].sum(),
        ],
        labels=["Fast utgift", "Hverdagsutgift"],
        autopct="%1.0f%%",
    )
    plt.title("Totale utgifter Januar-Mars")
    plt.show()


def main() -> None:
    deloppgave_a()
    deloppgave_b()
    deloppgave_c()
    deloppgave_d()


if __name__ == "__main__":
    main()
