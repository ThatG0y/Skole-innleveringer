import matplotlib.pyplot as plt
import numpy as np

delta_x = 1e-4


def f(x: float) -> float:
    return x**3


def derivert(f):
    def den_deriverte(x):
        return (f(x + delta_x) - f(x)) / delta_x

    return den_deriverte


# x-verdier

x_verdier = np.linspace(-2, 2, 50)

# Samme plot

plt.plot(x_verdier, f(x_verdier), label="f(x) = $x^3$")
plt.plot(x_verdier, derivert(f)(x_verdier), color="red", label="f'(x) = $3x^2$")
plt.plot(
    x_verdier, derivert(derivert(f))(x_verdier), color="green", label="f''(x) = 6x"
)

plt.axhline(y=0, color="black", linestyle="dotted")
plt.axvline(x=0, color="black", linestyle="dotted")

plt.legend()
plt.title("Grafene til f(x), f'(x), og f''(x)")

plt.savefig("samme_plot.png", dpi=300)
plt.show()


# Ulike plots
plt.subplots(constrained_layout=True)

plt.subplot(3, 1, 1)
plt.plot(x_verdier, f(x_verdier), label="f(x) = $x^3$")
plt.axhline(y=0, color="black", linestyle="dotted")
plt.axvline(x=0, color="black", linestyle="dotted")
plt.title("f(x)")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(x_verdier, derivert(f)(x_verdier), color="red", label="f'(x) = $3x^2$")
plt.axhline(y=0, color="black", linestyle="dotted")
plt.axvline(x=0, color="black", linestyle="dotted")
plt.title("f'(x)")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(
    x_verdier, derivert(derivert(f))(x_verdier), color="green", label="f''(x) = 6x"
)
plt.axhline(y=0, color="black", linestyle="dotted")
plt.axvline(x=0, color="black", linestyle="dotted")
plt.title("f''(x)")
plt.legend()

plt.savefig("ulike_plot.png", dpi=300)
plt.show()
