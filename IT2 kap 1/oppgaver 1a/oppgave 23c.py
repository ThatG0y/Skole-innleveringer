def finn_timer(minutter):
    org_minutter = minutter
    timer = minutter // 60
    minutter = minutter % 60
    print(f"{org_minutter} minutter er lik {timer} timer og {minutter} minutter")

if __name__ == "__main__":
    finn_timer(input("Konverter minutter til timer: "))