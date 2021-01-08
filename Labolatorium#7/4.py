tup = ("tutaj", "powinno", "być","6","elementów","elementuniów")
a = "6"
if a in tup:
    print(tup.index(a))

tup2 = ("Tutaj znajduje się bardzo długie zdanie z cyfrą 6")

if a in tup2:
    print(tup2.index(a))
    print(tup2.count(a))