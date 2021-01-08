kontakty = {}
i=0
while i != 10:
   klucz=input("Podaj nazwe: ")
   wartosc=input("Podaj numer: ")
   kontakty[klucz]=wartosc
   i+=1

print(kontakty)

pierwszy_numer = list(kontakty.values())[0]
ostatni_numer = list(kontakty.values())[len(kontakty)-1]

del kontakty[list(kontakty)[0]]
del kontakty[list(kontakty)[len(kontakty)-1]]

kontakty["nowy_pierwszy_numer"] = pierwszy_numer
kontakty["nowy_ostatni_numer"] = ostatni_numer

del kontakty[list(kontakty)[4]]
del kontakty[list(kontakty)[5]]

print(kontakty)
