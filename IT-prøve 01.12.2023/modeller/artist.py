class Artist:
    def __init__(self, fornavn: str, etternavn: str) -> None:
        self.navn = fornavn.title() + " " + etternavn.title()

    def __str__(self) -> str:
        return f"""Artist:
        Navn:                   {self.navn}
"""

    def vis_info(self):
        print(self)
