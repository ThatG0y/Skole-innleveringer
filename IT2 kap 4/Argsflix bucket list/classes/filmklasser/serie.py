from classes.filmklasser.visuell_media import VisuellMedia


class Serie(VisuellMedia):
    def __init__(
        self, title: str, år: int, imdb_id: str, poster: str, antall_sesonger: int
    ) -> None:
        super().__init__(title, år, imdb_id, poster)
        self.antall_sesonger = antall_sesonger
