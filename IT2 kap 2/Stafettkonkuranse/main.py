from modeller.lagmodeller.idrettsklubb import Idrettsklubb


def main() -> None:
    klubb = Idrettsklubb()
    klubb.finnRaskestLag()
    klubb.visKlubbInfo()


if __name__ == "__main__":
    main()
