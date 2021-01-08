num = int(input("Podaj liczbę:"))
i = 1
tab = []
while i <= num:
    if num%i==0:
        tab.append(i)
    i += 1
print(tab)
