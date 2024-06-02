import os


def absolutt_bane(relativ_bane: str) -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), relativ_bane)
