import sqlite3

connection = sqlite3.connect('pracownicy')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS pracownicy;
CREATE TABLE IF NOT EXISTS pracownicy (
id INTEGER PRIMARY KEY ASC,
imie VARCHAR(250) NOT NULL,
nazwisko VARCHAR(250) NOT NULL,
miejscowosc VARCHAR(250) NOT NULL,
zarobki INTEGER NOT NULL
)""")

cursor.execute('INSERT INTO pracownicy VALUES(NULL, "Mateusz", "Kapelusz", "Gdzieś na Podlasiu", 5000);')
cursor.execute('INSERT INTO pracownicy VALUES(NULL, "Bob", "Budowniczy", "Sosnowiec", 3000);')
cursor.execute('INSERT INTO pracownicy VALUES(NULL, "John", "Kowalsky", "UESEJ", 10000);')

def ShowEmployeesAlphabetically():
    with connection:
        cursor.execute('SELECT imie, nazwisko, miejscowosc, zarobki FROM pracownicy ORDER BY imie;')
        employees = cursor.fetchall()
        print("Lista pracowników posortowan alfabetycznie według imienia: ")
        for employee in employees:
            print(employee['imie'], employee['nazwisko'], employee['miejscowosc'], employee['zarobki'])

def AddEmployee():
    with connection:
        print("Dodaj pracownika: ")
        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")
        town = input("Podaj miejscowość: ")
        earnings = input("Podaj zarobki: ")
        cursor.execute(f'INSERT INTO pracownicy VALUES (NULL,"{name}", "{surname}", "{town}", {earnings});')
        print("Dodano pracownika")

def DismissEmployee():
    with connection:
        print("Zwolnij pracownika: ")
        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")
        cursor.execute(f'DELETE FROM pracownicy WHERE imie = "{name}" AND nazwisko = "{surname}";')
        print("Usunięto pracownika")

def SalaryInscrease():
    with connection:
        print("Zmień wynagrodzenie pracownika: ")
        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")
        earnings = int(input("Podaj nowe wynagrodzenie: "))
        cursor.execute(f'UPDATE pracownicy SET zarobki = {earnings} WHERE imie = "{name}" AND nazwisko = "{surname}";')
        print("Zaktualizowano wynagrodzenie pracownika")

def ShowEarningsDescending():
    with connection:
        print("Lista zarobków pracowników od największych do najmiejszych: ")
        cursor.execute('SELECT imie, nazwisko, miejscowosc, zarobki FROM pracownicy ORDER BY zarobki DESC;')
        earnigs = cursor.fetchall()
        for person in earnigs:
            print(person['zarobki'], person['imie'], person['nazwisko'])

def ShowEarningsAnscending():
    with connection:
        print("Lista zarobków pracowników od najmiejszych do największych: ")
        cursor.execute('SELECT imie, nazwisko, miejscowosc, zarobki FROM pracownicy ORDER BY zarobki ASC;')
        earnigs = cursor.fetchall()
        for person in earnigs:
            print(person['zarobki'], person['imie'], person['nazwisko'])
