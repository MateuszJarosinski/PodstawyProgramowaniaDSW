a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

pijtagoraza = (a**2 == b**2 + c**2)
pijtagorazb = (b**2 == a**2 + c**2)
pijtagorazc = (c**2 == a**2 + b**2)

if pijtagoraza or pijtagorazb or pijtagorazc == True:
    print("Trójkąt jest prostokątny")
else:
    print("Trójkąt nie jest prostokątny")
