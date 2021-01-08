menu = {
   "MARINARA" : 15,
   "MARGHERITA" : 16,
   "SALAME" : 20,
   "CALABRESE" : 20,
   "POLLO" : 20,
   "COTTO" : 20,
   "BOLOGNA" : 20,
   "BARI" : 21,
   "DIAVOLA" : 21,
   "PATATINA" : 21,
}

for klucz in menu.keys():
   print(klucz)

for wartosc in menu.values():
   print(wartosc)

for klucz, wartosc in menu.items():
   print (klucz, wartosc)


del menu[max(menu, key=menu.get)]
print(menu)
del menu[min(menu, key=menu.get)]
print(menu)

menu['HAWAI'] = 19
print(menu)
