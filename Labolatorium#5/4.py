amount = int(input("Podaj ilość liczb: "))
i = 0
tab = []
while i < amount:
    num = int(input("Podaj liczbę: "))
    tab.append(num)
    i += 1
print(tab)

for x in tab:
    if x > -6 and x < 6:
        print(x)
