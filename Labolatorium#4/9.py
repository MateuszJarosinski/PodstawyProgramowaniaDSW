import math

first_num = int(input("Podaj pierwszą liczbę: "))
next_num = int(input("Podaj następną liczbę:"))
modul = math.fabs(first_num - next_num)

while modul < 5:
    next_num = int(input("Podaj następną liczbę:"))
    modul = math.fabs(first_num - next_num)
    print(modul)
    first_num = next_num