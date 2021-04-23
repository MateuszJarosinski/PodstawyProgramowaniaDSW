i=0
list=[]
for i in range(0,101):
   num = i**3
   list.append(num)
   if sum(list) > 10000000:
      print("Aby uzyskać liczbę większą od 10000000 należy zsumować", len(list), "liczb")
      break
   else:
      i += 1
print("Suma wszystkich liczb:")
print(sum(list))
