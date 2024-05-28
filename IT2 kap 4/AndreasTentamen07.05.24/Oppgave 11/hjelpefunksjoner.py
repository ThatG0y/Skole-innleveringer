import os

MAPPE_STI = os.path.dirname(os.path.abspath(__file__))


def hent_absolutt_sti(relativ_sti: str) -> str:
    """Metode for å hente absolutte stier av relative stier"""
    return os.path.join(MAPPE_STI, relativ_sti)
