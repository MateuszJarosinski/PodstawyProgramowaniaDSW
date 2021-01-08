import math

print("Równanie kwadratowe ma postać: Ax^2 + Bx + C")
A = float(input("Podaj A: "))
B = float(input("Podaj B: "))
C = float(input("Podaj C: "))

delta = B**2 - 4*(A*C)



if delta==0:
    x = (-B)/2*A
    print("x = ",x)

if delta > 0:
    sqrt_delta = math.sqrt(delta)
    x1 = (-B) + sqrt_delta / 2 * A
    x2 = (-B) - sqrt_delta / 2 * A

    print("x1 = ",x1)
    print("x2 = ",x2)

if delta<0:
    print("Równanie kwadratowe nie ma rozwiązań")




