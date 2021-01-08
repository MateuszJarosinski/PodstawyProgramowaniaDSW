import random
teams = ["Beyern Munchen", "Liverpool FC", "Paris Saint-Germain", "Menchester City", "Atletico Madrid", "Barcelona", "Chelsea FC", "Real Madrid", "Inter Milan", "AC Milan", "Borussia Dortmund", "Juventus", "Bayer Leverkusen", "Menchester United", "Sevilla", "Roma", "RasenBallsport", "Tottenham", "Ajax Amsterdam"]
A = set()
B = set()
C = set()
D = set()

i=0
while i != 20:
   A.add(random.choice(teams))
   i += 1
print(A)

j=0
while j != 20:
   B.add(random.choice(teams))
   j += 1
print(B)

k=0
while k != 20:
   C.add(random.choice(teams))
   k += 1
print(C)

n=0
while n != 20:
   D.add(random.choice(teams))
   n += 1
print(D)

print("Wspólne A i B: ", A.intersection(B))

print("Różnica B i C: ", B.difference(C))

print("Suma C i D: ", C.union(D))

print("Czy D jest podzbiorem A: ", D.issubset(A))

print("Czy B jest podzbiorem A: ", A.issuperset(B))

print("Ilość wspólnych elementów B i C: ",len(B.intersection(C)))

LigaCD = C - D
print("Elementy nie powtarzające się w C i D: ",LigaCD)

listaCodD = list(LigaCD)
print("Konwersja na listę C od D", listaCodD)