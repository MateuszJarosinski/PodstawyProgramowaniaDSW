users = {
    "Bożydar" : '123',
    "Mieczysław" : '123',
    "Ambroży" : '123',
    "Tadeusz" : '123',
    "Waldemar" : '123',
    "admin" : 'admin'
}

while True:
    login = input("Login: ")
    password = input("Hasło: ")
    if password == users.get(login):
        if 'admin' != users.get(login):
            print("Zalogowano jako użytkownik")
            break
        else:
            print("Zalogowao jako admin")
            break
    else:
        print("Niewłaściwe hasło lub login")