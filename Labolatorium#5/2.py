import statistics
print("Podaj zakres licb:")

first_num=int(input(""))
last_num=int(input(""))
stop = first_num + 6
tab = []
if first_num and last_num !=0:
    for first_num in range(first_num, last_num+1):
        if first_num != stop:
            tab.append(first_num)
            first_num += 1
        else:
            break
else:
    print("Nie możesz podać liczby 0 w sumie nie wiem dlaczego ale NIE!")
print(tab)
print(min(tab))
print(max(tab))

srednia = sum(tab)/len(tab)
print(srednia)

print(statistics.median(tab))
