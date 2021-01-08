a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    print("Liczba",a,"jest najmniejsza")
    if b < c:
        print(b,"większa a ",c,"największa")
    if c < b:
        print(c, "większa a ", b, "największa")

if b < a and b < c:
    print("Liczba",b,"jest najmniejsza")
    if a < c:
        print(a,"większa a ",c,"największa")
    if c < a:
        print(c, "większa a ", a, "największa")

if c < a and c < b:
    print("Liczba",c,"jest najmniejsza")
    if a < b:
        print(a,"większa a ",b,"największa")
    if b < a:
        print(b, "większa a ", a, "największa")

if a==b==c:
    print("Obie liczby są równe LOL!")