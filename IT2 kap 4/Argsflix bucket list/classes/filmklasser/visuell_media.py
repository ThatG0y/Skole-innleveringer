class VisuellMedia:
    def __init__(self, title: str, år: int, imdb_id: str, poster: str) -> None:
        self.title = title
        self.år = år
        self.imdb_id = imdb_id
        self.poster = poster
        self.sett = False
