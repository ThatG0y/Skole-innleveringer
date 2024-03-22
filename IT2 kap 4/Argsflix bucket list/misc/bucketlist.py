from classes.filmklasser.visuell_media import VisuellMedia


class Bucketlist:
    def __init__(self) -> None:
        self.favoritter = []

    def legg_til(self, film: VisuellMedia) -> None:
        self.favoritter.append(film)
