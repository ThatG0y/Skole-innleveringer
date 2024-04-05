from classes.app import App
from utils.settings import API_KEY


def main() -> None:
    app = App()
    # app.lagre_film_info(app.hent_film("Avengers"), "test.json")
    app.søk.søk_tittel("Avengers")
    app.søk.søk_id("tt1517155")


if __name__ == "__main__":
    main()
