import sqlite3

conn = sqlite3.connect('test.db')

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES (1, ’Adam', 32, 'Wroclaw', 2000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES (2, ’Marcin’, 50, 'Wroclaw, 2000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES (3, ’Jan’, 19, 'Berlin', 6000.00 )")

conn.close()