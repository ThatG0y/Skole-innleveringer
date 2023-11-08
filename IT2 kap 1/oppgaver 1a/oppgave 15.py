import math as m


def finn_hypotenus(katet, vinkel):
    return katet/(m.cos(m.radians(vinkel)))


print(f"{finn_hypotenus(7, 60):.2f}")  # :.2f runder av svaret til 2 desimaler
