tall = input("Skriv et positivt heltall: ")
try:
    tall = int(tall)
except ValueError:
    print("Du må oppgi et positivt heltall")

sum = 0
for i in range(tall+1):
    sum += i

print(f"Summen av tallene fra 0 til og med {tall} er {sum}, og gjennomsnittet er {sum/tall}")