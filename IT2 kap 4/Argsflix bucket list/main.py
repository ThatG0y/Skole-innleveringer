from classes.app import App
from utils.settings import API_KEY


def main() -> None:
    app = App(API_KEY)
    app.lagre_film_info(app.hent_film("Avengers"), "test.json")


if __name__ == "__main__":
    main()
