from classes.filmklasser.visuell_media import VisuellMedia


class Film(VisuellMedia):
    """Klasse for å presentere OMDB-objekter med type "film" på"""

    def __init__(
        self,
        title: str,
        år: int,
        imdb_id: str,
        poster: str,
        plot: str,
        lengde: int,
        dvd: str,
        sett: bool,
    ) -> None:
        super().__init__(title, år, imdb_id, poster, plot, sett)
        self.lengde = lengde
        self.dvd = dvd

    def __str__(self) -> str:
        return f"""
        Type:       Film
        Lengde:     {self.lengde}    
        DVD:        {self.dvd}    
        {super().__str__()}"""

    @classmethod
    def fra_dict(cls, objekt: dict):
        tittel = objekt["Title"]
        år = objekt["Year"]
        imdb_id = objekt["imdbID"]
        poster = objekt["Poster"]
        plot = objekt["Plot"]
        lengde = objekt["Runtime"]
        dvd = objekt["DVD"]
        sett = objekt["Sett"]
        return cls(tittel, år, imdb_id, poster, plot, lengde, dvd, sett)
