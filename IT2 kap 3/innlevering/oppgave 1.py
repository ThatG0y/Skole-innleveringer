import pandas
import matplotlib.pyplot as plt

def read_data() -> pandas.DataFrame:
    with open("todos.json", encoding="utf-8-sig") as f:
        data = pandas.read_json(f)
        return data

def oppgave3(data: pandas.DataFrame) -> None:
    completed_tasks_count = data.value_counts()


    # Printer antall elementer totalt. Antar at hvert element er en separat task.
    print(f"Det finnes {len(data)} tasks")
    
    # Printer antall completed tasks
    completed = data["completed"] == True
    print(f"Det finnes {len(data[completed])} tasks som allerede er fulført")
    
    # Antall brukere
    print(f"Det finnes {len(data['userId'].unique())} ulike brukere som jobber i prosjektet")

def oppgave4(data: pandas.DataFrame) -> None:

    #Spesielle variabel pandas kan bruke
    completed = data["completed"] == True
    not_completed = data["completed"] == False


    print("\nDette er de taskene som er fullført\n")

    #Sorterer ut de som er completed og ikke completed
    for i, oppgave in enumerate(data[completed]["title"]):
        print(f"{i+1}. {oppgave}")
    
    print("\nDette er de taskene som ikke er fullført\n")
    for i, oppgave in enumerate(data[not_completed]["title"]):
        print(f"{i+1}. {oppgave}")

def oppgave5(data: pandas.DataFrame) -> None:
    completed = data["completed"] == True

    #Finner unike instanser av "userId" og antall
    completed_tasks_count = data[completed]["userId"].value_counts()

    _, highest = completed_tasks_count.keys()[0], completed_tasks_count.iloc()[0]
    print(f"Den høyeste poeng summen er {highest}, personenen/e som fikk denne summen var:")
    count = 1

    #Finner alle brukere som har flest oppgaver løst.
    for i in range(len(completed_tasks_count)):
        value, new_highest = completed_tasks_count.keys()[i], completed_tasks_count.iloc()[i]
        if new_highest == highest:
            print(f"{count}. User_Id {value}")
            count += 1
        else:
            break
    
def oppgave6(data: pandas.DataFrame) -> None:
    completed = data["completed"] == True
    not_completed = data["completed"] == False

    #Pandas finner alle rows hvor completed er True/False
    completed_count = len(data[completed])
    not_completed_count = len(data[not_completed])


    values = [completed_count, not_completed_count]
    titles = ["Antall ferdig", "Antall ikke ferdig"]

    fig, ax = plt.subplots(figsize=(8,4))


    plt.title("Oppgaveoversikt")
    plt.ylabel("Antall")
    ax.bar(titles, values, color=["blue", "red"])
    plt.show()

def oppgave7(data: pandas.DataFrame) -> None:
    completed = data["completed"] == True

    completed_tasks_count = data[completed]["userId"].value_counts()
    usernames = []
    values = []

    # Finner alle brukere og deres antall løste oppgaver
    for user, value in zip(completed_tasks_count.keys(), completed_tasks_count.iloc()):
        usernames.append(f"Bruker {user}")
        values.append(value)
    fig, ax = plt.subplots(figsize=(8,4))
    plt.title("Prosentvis oppgaver utført av ansatte")
    ax.pie(values, labels=usernames, autopct='%1.0f%%')
    fig.legend(bbox_to_anchor=(0.75, 0.65))
    fig.subplots_adjust(right=0.5)
    plt.show()
    

def main():
    data = read_data()
    
    oppgave3(data)
    oppgave4(data)
    oppgave5(data)
    oppgave6(data)
    oppgave7(data)
if __name__ == '__main__':
    main()