from modeller.artist import Artist
from modeller.platealbum.platealbum import Platealbum
from modeller.platesamling import Platesamling


def main() -> None:
    artist = Artist("Katy", "Perry")
    album = Platealbum("Noe", artist, "ENda mer", 1984)
    samling = Platesamling("adnreas", plater=album)
    print(samling)


if __name__ == "__main__":
    main()
