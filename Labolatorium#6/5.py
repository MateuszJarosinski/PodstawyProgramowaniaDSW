start = int(input("Podaj pierwszą liczbę z przedizału:")) # pierwsza tabelka
end = int(input("Podaj ostatnią liczbę z przedziału:"))

tab=[]
powt = 0

for i in range(start, end+1):
   tab.append(start)
   start += 1

print(tab)

print(tab[-3]) #szuka 3 od końca

k = int(input("Podaj który element od końca mam usunąć:"))   #losowy od końca do usunięcia
tab.pop(-k)

print(tab)

start_2 = int(input("Podaj pierwszą liczbę z przedizału dla drugiel listy:"))   # 2 tablica
end_2 = int(input("Podaj ostatnią liczbę z przedziału dla drugiej listy:"))

tab_2=[]

for i in range(start_2, end_2+1):
   tab_2.append(start_2)
   start += 1

print(tab_2)

tab_3 = tab + tab_2

print(tab_3)

for i in range(len(tab_3) + 1):
    if tab_3.count(i) > 1:
        powt += 1
    i += 1
print(len(tab_3))
print(powt)
