import matplotlib.pyplot as plt
import numpy as np
import random as rd

# Deloppgave a + b
x_verdier = np.linspace(1, 6, 6)
y_verdier = np.zeros(6)

while True:
    try:
        antall_kast = int(input("Velg antall terningkast: "))
        break
    except ValueError:
        print("Ikke valid input")
        continue


def terning_kast() -> int:
    return rd.randint(1, 6)


for _ in range(antall_kast):
    y_verdier[terning_kast() - 1] += 1

plt.plot(x_verdier, y_verdier)
plt.scatter(x_verdier, y_verdier)
plt.title("Hundre terningkast")
plt.savefig("hundre_kast.png", dpi=300)
plt.show()

# Deloppgave c

x_verdier = np.linspace(1, 6, 6)
y_verdier = np.zeros(6)

antall_kast = 100000

for i in range(antall_kast):
    y_verdier[terning_kast() - 1] += 1

plt.plot(x_verdier, y_verdier)
plt.scatter(x_verdier, y_verdier)
plt.title("Hundre tusen terningkast")
plt.savefig("hundre_tusen_kast.png", dpi=300)
plt.show()
