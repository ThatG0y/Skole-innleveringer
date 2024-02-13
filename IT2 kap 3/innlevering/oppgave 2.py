import pandas
import os

def retrive_data(file: str) -> pandas.DataFrame: 
    with open(file, encoding="utf-8-sig") as f:
        data = pandas.read_json(f)
        return data
    
def fix_duplicates(data: pandas.DataFrame) -> None:
    #drop_duplicates fjerner duplikater ut ifra en kolonne i dataframe
    data.drop_duplicates(subset="id", inplace=True)

def fix_user_Id(data: pandas.DataFrame) -> None:
    #Astype omgjør typen til int (fra float)
    data["userId"] = data["userId"].astype(int)

def fix_blanks(data: pandas.DataFrame) -> None:
    #Bruker join() og split() til å fjerne unødvendige blanks fra innsiden av 'title'-strings
    data['title'] = data["title"].apply(lambda x: " ".join(x.split()))

def fix_estimat(data: pandas.DataFrame) -> None:
    #Hvis 'estimat' er tomt, endrer den til '3d'
    data['estimat'] = data['estimat'].apply(lambda x: "3d" if len(x) == 0 else x)

def test_data():
    data = retrive_data("TestData.json")
    print("\nURESNET DATA")
    print(f"{data}\n")
    fix_duplicates(data)
    fix_blanks(data)
    fix_estimat(data)
    print("RENSET DATA")
    print(data)

def main_data():
    data = retrive_data("todos_oppgave1.json")
    fix_duplicates(data)
    fix_blanks(data)
    fix_estimat(data)
    print(data)

def main():
    main_data()
    test_data()

if __name__ == '__main__':
    main() 