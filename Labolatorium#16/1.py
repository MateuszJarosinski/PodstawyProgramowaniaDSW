import sqlite3

connection = sqlite3.connect('Kontakty')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.executescript("""
    DROP TABLE IF EXISTS Kontakty;
    CREATE TABLE IF NOT EXISTS Kontakty (
    id INTEGER PRIMARY KEY ASC,
    imie varchar(250) NOT NULL,
    nazwisko varchar(250) NOT NULL,
    numerTelefonu INTEGER NOT NULL,)""")

cursor.execute('INSERT INTO Kontakty VALUES(imie,nazwisko,numerTelefonu);',('Jan', 'Kowalski', '666666666'))

connection.commit()