import sqlite3

con = sqlite3.connect('baza')
con.row_factory = sqlite3.Row    #umożliwia dostęp do kolumn poprzez nazwy, nie tylko indeksy
cur = con.cursor() #tworzy kursor dający dostęp do bazy

cur.executescript("""
    DROP TABLE IF EXISTS szkolenia;
    CREATE TABLE IF NOT EXISTS szkolenia (
    id INTEGER PRIMARY KEY ASC,
    temat varchar(250) NOT NULL,
    kategorie varchar(250) NOT NULL)""")

cur.executescript("""
    DROP TABLE IF EXISTS prowadzacy;
    CREATE TABLE IF NOT EXISTS prowadzacy(
    id INTEGER PRIMARY KEY ASC,
    imie varchar(250) NOT NULL,
    nazwisko varchar(250) NOT NULL,
    szkolenia_id INTEGER NOT NULL,
    FOREIGN KEY(szkolenia_id) REFERENCES szkolenia(id))""")

cur.executescript("""
    DROP TABLE IF EXISTS kursanci;
    CREATE TABLE IF NOT EXISTS kursanci (
    id INTEGER PRIMARY KEY ASC,
    imie varchar(250) NOT NULL,
    nazwisko varchar(250) NOT NULL,
    szkolenia_id INTEGER NOT NULL,
    FOREIGN KEY(szkolenia_id) REFERENCES szkolenia(id))""")

cur.execute('INSERT INTO szkolenia VALUES(NULL,?,?);',('programowanie','informatyka'))
cur.execute('INSERT INTO szkolenia VALUES(NULL, ?, ?);', ('grafika komputerowa', 'informatyka'))

cur.execute('INSERT INTO prowadzacy VALUES(NULL, ?, ?, ?);', ('Bogdan', 'Nowak', '1'))
cur.execute('INSERT INTO prowadzacy VALUES(NULL, ?, ?, ?);', ('Mirek', 'Kowalski', '2'))

cur.execute('INSERT INTO kursanci VALUES(NULL, ?, ?, ?);', ('Jan', 'Szymański', '2'))
cur.execute('INSERT INTO kursanci VALUES(NULL, ?, ?, ?) ;', ('Michal', 'Woźniak' , '1'))

con.commit()

def czytaj_dane():
    with con:
        cur.execute('SELECT * FROM szkolenia')
        wynik_szkolenia = cur.fetchall()
        print("\nSzkolenia:")
        for x in wynik_szkolenia:
            print(x['id'], x['temat'], x['kategorie'])


