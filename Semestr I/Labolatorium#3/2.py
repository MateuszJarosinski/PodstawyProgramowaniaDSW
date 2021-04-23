end = int(input("Podaj ostatnią liczbę z predziału:"))

for x in range(end+1, 0, -1):
   if x%6==0 and x%9==0:
      print(x)
