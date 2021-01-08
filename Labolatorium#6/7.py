import random
strike = 0
tab = []
for i in range(0,6):
    answer = int(input("Podaj liczbę:"))
    tab.append(answer)
for z in range(0,6):
    num = random.randint(0,49)
    if num in tab:
        strike = strike+1
print("Trafiles",strike,"liczb")

if strike == 3:
    print("Wygrałeś: 50 zł")
if strike == 4:
    print("Wygrałeś: 200 zł")
if strike == 5:
    print("Wygrałeś: 5 000zł")
if strike == 6:
    print("Wygrałeś: 1 000 000zł")
