class Hotel:
    def __init__(self, nazwa, ile_gwiazdkowy, ilosc_pieter, ilosc_pokoi):
        self.nazwa = nazwa
        self.ile_gwiazdkowy = ile_gwiazdkowy
        self.ilosc_piekter = ilosc_pieter
        self.ilosc_pokoi = ilosc_pokoi

    def Info(self):
        print(f"Jestem {self.ile_gwiazdkowy} gwiazdkowym hotelem")

class LepszyHotel:
    def __init__(self, nazwa, ile_gwiazdkowy, ilosc_pieter, ilosc_pokoi):
        self.nazwa = nazwa
        self.ile_gwiazdkowy = ile_gwiazdkowy
        self.ilosc_piekter = ilosc_pieter
        self.ilosc_pokoi = ilosc_pokoi

Barak = Hotel("Barak chłopaków", "0", "0", "2")
ZempamaLapepeWCentrumWarszawy = Hotel("ZempamaLapepe", "5", "20", "500")

for hotele in (ZempamaLapepeWCentrumWarszawy, Barak):
    print(hotele.Info())
