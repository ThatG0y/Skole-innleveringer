from classes.filmklasser.visuell_media import VisuellMedia


class Film(VisuellMedia):
    def __init__(
        self, title: str, år: int, imdb_id: str, poster: str, lengde: int
    ) -> None:
        super().__init__(title, år, imdb_id, poster)
        self.lengde = lengde
