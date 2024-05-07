import pandas as pd
import matplotlib.pyplot as plt


def hent_data():
    url = r"utgifter.csv"
    return pd.read_csv(url, sep=";", skiprows=1)


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


def deloppgave_b_2():
    data = hent_data()


def deloppgave_b():
    måneder = {1: "januar", 2: "februar", 3: "mars"}
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
    hverdagsutgift_1 = data[data["Type"] == "klær"]
    hverdagsutgift_2 = data[data["Type"] == "mat"]
    plt.pie(
        [
            fast_utgift["Beløp"].sum(),
            hverdagsutgift_1["Beløp"].sum() + hverdagsutgift_2["Beløp"].sum(),
        ],
        labels=["Fast utgift", "Hverdagsutgift"],
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
