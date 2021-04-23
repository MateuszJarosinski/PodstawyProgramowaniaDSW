print("PROGRAM DO PRZELICZANIA JEDNOSTEK:")

answer = input("stopa - wciśnij S   cale - wciśnij C:   ")
choice = input("metry - m, centymetry - cm milimetry - mm, kilometry - km:   ")
value = float(input("Podaj ilość:   "))
if answer == "S":
    mm = 304.8
    cm = 30.48
    m = 0.3048
    km = 0.0003048
    if choice == "mm":
        print(value*mm)
    if choice == "cm":
        print(value*cm)
    if choice == "m":
        print(value*m)
    if choice == "km":
        print(value*km)
if answer == "C":
    mm = 25.4
    cm = 2.54
    m = 0.0254
    km = 2.54*10**(-5)
    if choice == "mm":
        print(value*mm)
    if choice == "cm":
        print(value*cm)
    if choice == "m":
        print(value*m)
    if choice == "km":
        print(value*km)