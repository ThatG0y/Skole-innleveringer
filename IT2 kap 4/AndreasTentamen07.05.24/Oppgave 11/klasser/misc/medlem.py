class Medlem:
    def __init__(self, navn: str, e_post: str) -> None:
        self.navn = navn
        self.e_post = e_post

    def __str__(self) -> str:
        return f"""Navn:        {self.navn}
E-post:         {self.e_post}
"""
