import random

lista = []

for x in range(10):
    element = random.randint(0, 10)
    lista.append(element)
print(lista)                   #pierwotna lista

random.shuffle(lista)
print(lista)                   #to jest lista pomieszana

lista.sort()
print(lista)                   #tutaj sortuje min - max

