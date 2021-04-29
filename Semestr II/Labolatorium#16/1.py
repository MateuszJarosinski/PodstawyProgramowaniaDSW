import  sqlite3

connection = sqlite3.connect('kontakty')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS kontakty;
CREATE TABLE IF NOT EXISTS kontakty (
id INTEGER PRIMARY KEY ASC,
imie Varchar(250) NOT NULL,
nazwisko Varchar(250) NOT NULL,
numer INTEGER NOT NULL
)""")

cursor.execute('INSERT INTO kontakty VALUES (NULL, "Jan", "Kowalski", 123456789);')
cursor.execute('INSERT INTO kontakty VALUES (NULL, "Mateusz", "Kapelusz", 696420666)')

def ShowContacts():
    with connection:
        cursor.execute('SELECT * FROM kontakty')
        contacts = cursor.fetchall()
        print("Lista kontaktów w tabeli kontakty: ")
        for contact in contacts:
            print(contact['id'], contact['imie'], contact['nazwisko'], contact['numer'])

def FindContact():
    with connection:
        num = int(input("Podaj szukany numer telefonu:"))
        cursor.execute(f'SELECT * FROM kontakty WHERE numer = {num}')
        findNum = cursor.fetchall()
        for contact in findNum:
            print(f"Szukany numer należy do: {contact['imie']} {contact['nazwisko']}")

def AddContact():
    with connection:
        print("Dodaj kontakt: ")
        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")
        num = int(input("Podaj numer telefonu: "))
        cursor.execute(f'INSERT INTO kontakty VALUES(NULL , "{name}", "{surname}", "{num}" )')
        print("Kontakt został dodany")

def DeleteContact():
    with connection:
        print("Usuń kontakt: ")
        num = int(input("Podaj numert telefonu który chcesz usunąć: "))
        cursor.execute(f'DELETE FROM kontakty WHERE numer = {num}')
        print("Kontakt został usunięty")


print(DeleteContact())
print(ShowContacts())