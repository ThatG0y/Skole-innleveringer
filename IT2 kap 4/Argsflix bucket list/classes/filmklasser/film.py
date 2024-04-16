from classes.filmklasser.visuell_media import VisuellMedia


class Film(VisuellMedia):
    def __init__(
        self,
        title: str,
        år: int,
        imdb_id: str,
        poster: str,
        lengde: int,
        dvd: str,
        sett: bool,
    ) -> None:
        super().__init__(title, år, imdb_id, poster, sett)
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
        lengde = objekt["Runtime"]
        dvd = objekt["DVD"]
        sett = objekt["Sett"]
        return cls(tittel, år, imdb_id, poster, lengde, dvd, sett)
