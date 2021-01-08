a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))
c = float(input("Podaj liczbę c: "))
d = float(input("Podaj liczbę d: "))

if a > b and a > c and a > d:
    print("Liczba ", a, "jest największa")
elif b > a and b > c and b > d:
    print("Liczba ", b, "jest największa")
elif c > a and c > b and c > d:
    print("Liczba ", c, "jest największa")
elif d > a and d > b and d > c:
    print("Liczba ", d, "jest największa")
elif a == b == c == d:
    print("Wszystkie liczby są takie same")