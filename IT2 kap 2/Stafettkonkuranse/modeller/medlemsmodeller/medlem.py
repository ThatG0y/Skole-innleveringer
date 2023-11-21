class Medlem:
    """En klasse som representerer et lagmedlem.

    Attributes
    ----------
    navn : str
        Lagmedlemets navn
    """

    def __init__(self, navn: str) -> None:
        """Konstruerer tilstanden til lagmedlem-objektet.

        Parameters
        ----------
        navn : str
            Lagmedlemets navn
        """
        self.navn = navn
