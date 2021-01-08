i = int(input("Podaj liczbęnaturalną:"))
while i % 12 != 0:
    i = int(input("Podaj następną liczbę:"))
    if i % 12 == 0:
        print("Podałeś liczbę podzielną przez 12, kończę działanie programu!")
    else:
        continue
