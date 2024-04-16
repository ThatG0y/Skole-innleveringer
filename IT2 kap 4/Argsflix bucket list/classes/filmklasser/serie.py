from classes.filmklasser.visuell_media import VisuellMedia


class Serie(VisuellMedia):
    """Klasse for å presentere OMDB-objekter med type "serie" på"""

    def __init__(
        self,
        title: str,
        år: int,
        imdb_id: str,
        poster: str,
        plot: str,
        antall_sesonger: int,
        sett: bool,
    ) -> None:
        super().__init__(title, år, imdb_id, poster, plot, sett)
        self.antall_sesonger = antall_sesonger

    def __str__(self) -> str:
        return f"""
        Type:       Serie
        Sesonger:   {self.antall_sesonger}    
        {super().__str__()}"""

    @classmethod
    def fra_dict(cls, objekt: dict):
        tittel = objekt["Title"]
        år = objekt["Year"]
        imdb_id = objekt["imdbID"]
        poster = objekt["Poster"]
        plot = objekt["Plot"]
        antall_sesonger = objekt["totalSeasons"]
        sett = objekt["Sett"]
        return cls(tittel, år, imdb_id, poster, plot, antall_sesonger, sett)
