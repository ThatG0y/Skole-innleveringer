class Rating:
    def __init__(self, navn: str, score: str) -> None:
        self.navn = navn
        self.score = score

    def __str__(self) -> str:
        return f"{self.navn}, {self.score}"

    def vis_score(self):
        print(self)
