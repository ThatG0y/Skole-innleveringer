ord = "spiser"
lengde = len(ord)  # siden "spiser" inneholder 6 bokstaver blir "lengde" lik 6.
nyttOrd = ord[2] + ord[lengde - 3]
# ord[2] blir den tredje bokstaven i ordet (i) siden indexing i python begynner på 0.
# ord[lengde - 3] blir den fjerde bokstaven i ordet (s) siden ord[6-3] == ord[3].
print(nyttOrd)  # "i" + "s" = "is"
