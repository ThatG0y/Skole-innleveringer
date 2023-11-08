import numpy as np

# from nptyping import NDArray, Int

Array = np.ndarray[np.integer | np.floating]


def doble_tall_i_talliste(talliste: Array) -> Array:
    """Dobler alle tall i en array

    Parameters
    ----------
    talliste : Array
        Array med tall

    Returns
    -------
    Array
        Array med tall
    """
    return np.multiply(talliste, 2)


def main() -> None:
    talliste = np.array([1, 5, 23, 88, 3, 777])
    print(
        f"{list(talliste)} blir til {list(doble_tall_i_talliste(talliste))} når doblet"
    )


if __name__ == "__main__":
    main()
