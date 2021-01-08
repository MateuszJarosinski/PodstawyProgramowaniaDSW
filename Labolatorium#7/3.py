import random

A = []
B = []
i = 0
k = 0
while i != 100:
    parzyste = random.randint(0, 10)
    if parzyste%2==0:
        A.append(parzyste)
        i += 1
tupA = tuple(A)
print(tupA)

while k != 100:
    NIEparzyste = random.randint(0, 10)
    if NIEparzyste%2!=0:
        B.append(NIEparzyste)
        k += 1
tupB = tuple(B)
print(tupB)

