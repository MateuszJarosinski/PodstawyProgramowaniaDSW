tekst = f"""Magia jest w opinii niektórych ucieleśnieniem Chaosu. Jest kluczem zdolnym otworzyć zakazane drzwi. Drzwi, za którymi czai się koszmar, 
zgroza i niewyobrażalna okropność, za którymi czyhają wrogie, destrukcyjne siły, moce czystego zła, mogące unicestwić nie tylko tego, kto drzwi 
te uchyli, ale i cały świat. A ponieważ nie brakuje takich, którzy przy owych drzwiach manipulują, kiedyś ktoś popełni błąd, a wówczas zagłada 
świata będzie przesądzona i nieuchronna. Magia jest zatem zemstą i orężem Chaosu. To, że po Koniunkcji Sfer ludzie nauczyli posługiwać się magią, 
jest przekleństwem i zgubą świata. Zgubą ludzkości. I tak jest. Ci, którzy uważają magię za Chaos, nie mylą się"""

print("Lower")

print(tekst.lower())

print("Swapcase")

print(tekst.swapcase())

print("Capitalize")

print(tekst.capitalize())

print("Replace")

print(tekst.replace("."," !@^%*&^% "))

print("Lstrip")

print(tekst.lstrip())

print("Rstrip")

print(tekst.rstrip())

print("Reversed")

print(tekst[::-1])

print("Count : y pojawia się tyle razy: ")

print(tekst.count("y",0,len(tekst)))

print("Find")

print(tekst.find("Zaraza",0,len(tekst)))

print("Isallnum")

print(tekst.isalnum())

print("Startswith")

print(tekst.startswith("Magia",0,len(tekst)))

print("Endswith")

print(tekst.endswith("Chaosu",0,len(tekst)))