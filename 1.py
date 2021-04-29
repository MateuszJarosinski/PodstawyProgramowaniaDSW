class Czlowiek:
    def __init__(self, kolor_skory, pochodzenie):
        self.kolor_skory = kolor_skory
        self.pochodzenie = pochodzenie

    def zmienPochodzenie(self, nowePochodznie):
        self.pochodzenie = nowePochodznie
        return self.pochodzenie


class Osoba(Czlowiek):
    def __init__(self, imie, nazwisko, PESEL, kolor_skory, pochodzenie):
        super().__init__(kolor_skory, pochodzenie)
        self.imie = imie
        self.nazwisko = nazwisko
        self.PESEL = PESEL

    def Info(self):
        print(self.imie, self.nazwisko, self. kolor_skory)

JanKowalski = Osoba("Jan", "Kowalski", 123123123, "bialy", "Polska")
JanKowalski.zmienPochodzenie("Hiszpania")