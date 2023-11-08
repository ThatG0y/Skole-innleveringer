import oppgave22bibliotek as b


def main():
    talliste = [1, 4, 33, 38, 9]
    print(f"Summen av tallisten {talliste} er {b.summer_liste(talliste)}")
    print(
        f"Gjennomsnittlig verdi i tallisten {talliste} er {b.gjennomsnittlig_verdi_i_liste(talliste)}"
    )
    print(
        f"Det største tallet i tallisten {talliste} er {b.størst_tall_i_liste(talliste)}"
    )
    print(
        f"Det minste tallet i tallisten {talliste} er {b.minst_tall_i_liste(talliste)}"
    )


if __name__ == "__main__":
    main()
