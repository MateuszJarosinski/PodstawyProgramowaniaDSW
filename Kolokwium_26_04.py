class Druzyna:
    def __init__(self, nazwa_druzyny, ilosc_czlonkow,):
        self.nazwa_druzyny = nazwa_druzyny
        self.ilosc_czlonkow = ilosc_czlonkow
        self.druzyna = []

    def DruzynaInfo(self):
        return self.nazwa_druzyny ,self.ilosc_czlonkow

class Zawodnicy(Druzyna):

    def __init__(self, nazwa_druzyny, ilosc_czlonkow, imie, nazwisko, sport):
        super().__init__(nazwa_druzyny, ilosc_czlonkow)
        self.imie = imie
        self.nazwisko = nazwisko
        self.sport = sport
        self.sport = sport

    def DodajZawodnika(self, obiekt_zawodnika):
        self.ilosc_czlonkow += 1
        return "Dodano zawodnika"

FCB = Druzyna("FCB", 0)
Zawodnik1 = Zawodnicy("FCB", 0, "Marcin", "Kowalski", "Koszykówka")
print(Zawodnik1.DodajZawodnika(Zawodnik1))
print(Zawodnik1.DruzynaInfo())
