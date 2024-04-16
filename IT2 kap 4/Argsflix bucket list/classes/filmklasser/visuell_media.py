class VisuellMedia:
    """Klasse for å presentere OMDB-objekter på"""

    def __init__(
        self, tittel: str, år: str, imdb_id: str, poster: str, plot: str, sett: bool
    ) -> None:
        self.tittel = tittel
        self.år = år
        self.imdb_id = imdb_id
        self.poster = poster
        self.plot = plot
        self.sett = sett

    def __str__(self) -> str:
        return f"""Tittel:     {self.tittel}
        År:         {self.år}
        IMDB-id:    {self.imdb_id}
        Sett:       {self.sett}
        Plot:       {self.plot}"""
        # Poster:     {self.poster}
