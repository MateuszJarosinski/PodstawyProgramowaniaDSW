print("Podaj liczby, żeby obliczyć z nich średnią. Podaj 0 żeby zakończyć działanie programu:")

i = 0
sum = 0.0
num = 1

while num !=0:
    num=float(input(""))
    sum = sum + num
    i += 1

if i == 0:
	print("Podaj kilka liczb")
else:
	print("Średnia podanych liczb wynosi:", sum / (i-1))