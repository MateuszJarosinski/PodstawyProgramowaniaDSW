import random
num = random.randint(1,101)
i=0
while i != 3:
   answer=int(input("Zgadnij liczbę:"))
   if answer>num:
      print("Podałeś za dużą wartość!")
      i +=1
   elif answer<num:
      print("Podałeś za małą wartość!")
      i +=1
   else:
      print("Gratulacje!")
      break
else:
   print("Ha Ha przegrałęś !!!")
