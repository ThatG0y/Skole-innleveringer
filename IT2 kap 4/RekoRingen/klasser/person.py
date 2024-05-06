class Person:
    def __init__(self, navn: str, mobil: int) -> None:
        self.mobil = mobil
        self.navn = navn

    def __str__(self) -> str:
        return f"""Navn     {self.navn}
Telefonnummer:  {self.mobil}"""
