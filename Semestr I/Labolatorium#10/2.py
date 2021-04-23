name = input("Jak masz na imię: ")
surname = input("Jak masz na nazwisko: ")
phone_number = input("Podaj numer telefonu: ")
shoe_number = input("Jaki masz numer buta xD: ")

print(name.isalpha())
print(surname.isalpha())
print(phone_number.isdigit())
print(shoe_number.isdigit())

if name.isupper() != True:
    print(name.capitalize())

if surname.isupper() != True:
    print(surname.capitalize())

if phone_number.isdigit != True:
    new_phone_number = phone_number.replace("-", "")
    print(new_phone_number)

if shoe_number.isdigit != True:
    new_shoe_number=shoe_number.replace("-",'')
    print(shoe_number)

if name.endswith("a") == True or name == "Nel" :
    if name != "Barnaba":
        print("Jesteś kobietą")
    else:
        print("Masz na imię Barnaba OMG !")
else:
    print("Jesteś mężczyzną")
