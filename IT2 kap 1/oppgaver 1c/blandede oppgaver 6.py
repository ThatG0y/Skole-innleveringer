import random

tall = random.randint(1,100)

for i in range(7):
    gjett = input("Gjett tallet mellom 1 og 100: ")
    try:
        gjett=int(gjett)
    except ValueError:
        print("Ikke riktig input")
        continue
    if gjett < tall:
        print("For lavt!")
    elif gjett > tall:
        print("For høyt!")
    elif gjett == tall:
        print("Du gjetta riktig!")
        exit()
    else:
        print("Error")

print(f"Du klarte ikke å gjette tallet :( (tallet var {tall}))")