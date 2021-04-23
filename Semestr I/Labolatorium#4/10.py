numA = 0
numB = 0
suma = 0
i = 0

lista = []

while True:
    numB = float(input("Podaj liczbę:   "))
    lista.append(numB)
    if i == 0:
        num = lista[0]
        numA=numB
        suma=numB
        print(suma)
        i += 1
    else:
        num = lista[i]
        if numB != numA:
            numA = numB
            suma += numB
            print(suma)
            i += 1
        else:
            break

