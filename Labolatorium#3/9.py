import random
tab = []
for i in range(0,6):
   wynik=random.randint(1,50)
   if wynik not in tab:
      tab.append(wynik)
   print(tab)
