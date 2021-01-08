num = list(input("Podaj liczbę byczq, pokażę ci sztuczkę:  "))

num_odwrotny = num[::-1]

if num_odwrotny == num:
    print("Odwróciłem twoją liczbę ale tego nie widzisz bo to palindrom!")
    print(num_odwrotny)
else:
    print("Odwóciłem ci liczbę OMG")
    print(num_odwrotny)

