stop = int(input("Podaj ile liczb chcesz wpisać do listy: "))
lista = []
for x in range(0, stop):
    num = int(input("Podaj liczbę: "))
    lista.append(num)
print(lista)

max_element= max(lista)
print(max_element)
count= lista.count(max_element)
print(count)