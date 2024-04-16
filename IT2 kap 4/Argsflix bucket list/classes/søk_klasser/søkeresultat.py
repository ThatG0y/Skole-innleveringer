class Søkeresultat:
    def __init__(
        self, tittel: str, år: str, imdb_id: str, poster: str, type: str
    ) -> None:
        self.tittel = tittel
        self.år = år
        self.imdb_id = imdb_id
        self.poster = poster
        self.type = type

    def __str__(self) -> str:
        return f"""
        Tittel:     {self.tittel}
        År:         {self.år}
        IMDB-id:    {self.imdb_id}
        Type:       {self.type.title()}"""
