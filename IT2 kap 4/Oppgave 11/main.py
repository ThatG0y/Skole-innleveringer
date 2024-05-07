from klasser.bilkollektiv import Bilkollektiv


def main() -> None:
    kollektiv = Bilkollektiv("Oslo", "Oslo Sentrum") #skulle hentet fra csv for startinfo
    kollektiv.run()


if __name__ == "__main__":
    main()
