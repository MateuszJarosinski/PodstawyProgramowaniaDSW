tab = []
i = 0
while i != 10:
   a = int(input("Podaj liczbę z przedziału od 0 do 59:"))
   if a >= 0 and a <=59:
      tab.append(a)
      i += 1
   else:
      print("Podałeś liczbę z poza przedziłu!!!")
      i += 0
print(tab)

k = 0                                                 #dla append
while k != 3:
   num = int(input("Podaj liczbę parzystą"))
   if num%2==0:
      tab.append(num)
      k+=1
   else:
      print("Parzystą!")
      k+=0
print(tab)

j = 0                                                 #dla insert
while j != 3:
   num = int(input("Podaj liczbę i index którą chcesz dodać:"))
   if num%2==0:
      tab.insert(num)
      j+=1
   else:
      print("Parzystą!")
      j+=0
print(tab)

n = 0                                                 #dla pop
while n != 3:
   index = int(input("Podaj indeks liczby nieparzystej, którą chcesz usunąć:"))
   if index%2!=0:
      tab.pop(index)
      n+=1
   else:
      print("Nieparzystą!")
      n+=0
print(tab)

m = 0                                                 #dla remove
while m != 3:
   num = int(input("Podja liczbę nieparzystą, którą chcesz usunąć:"))
   if num%2!=0:
      tab.remove(num)
      m+=1
   else:
      print("Nieparzystą!")
      m+=0
print(tab)

tab.insert(5,3)
tab.insert(10,33)
