num = int(input("Podaj liczbę całkowitą: "))
suma = 0
if num >= 0:
    for x in range(0, num+1):
        num2=x**2
        suma = suma + num2
        print(suma)
