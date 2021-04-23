tab = []
i=0

num = int(input("Podaj ilość liczb: "))
while i < num:
    a = int(input("Podaj te liczby: "))
    if a < 0:
        continue
    else:
        tab.append(a)
        i += 1
print(tab)
srednia = (sum(tab)) / num
print(srednia)