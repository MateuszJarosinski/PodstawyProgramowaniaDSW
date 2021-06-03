import time
class Animal:
    def __init__(self, name, skinType, stillAlive, isDangerous, species):
        self.name = name
        self.skinType = skinType
        self.stillAlive = stillAlive
        self.isDangerous = isDangerous
        self.species = species

    def IsDangerousInfo(self):
        answer = input(f"Czy zwierzę {self.name} {self.species} jest niebezpieczne? [TAK/NIE]")
        if answer.upper() == "TAK":
            print("Niebezpieczne zwierze, lepiej uważać!")
        if answer.upper() == "NIE":
            print("Milutkie zwierze")

    def ListOfAnimals(self):
        print("Łosie, jelenie, sarny, dziki, lisy, borsuki, kuny, jenoty, wilki i rysie")
        time.sleep(1)
        print("Z ptaków:")
        time.sleep(1)
        print("Kuropatwy, bażanty, dzikie kaczki, gęsi, whisky, begasy i cietrzewie")
        time.sleep(1)
        print("Mmay jendak poważne obawy o dalsze rozczeczewia")

    def IsStillAlive(self):
        if self.stillAlive.upper() == "TAK":
            print("Ten gatunek wciąż sitnieje na Ziemi!")
        else:
            print("Ten gatyunek nie występuje już na Ziemi :c")


class Cat(Animal):
    def __init__(self, name, skinType, stillAlive, isDangerous, species, isWild, favoriteFood):
        super().__init__(name, skinType, stillAlive, isDangerous, species)
        self.isWild = isWild
        self.favoriteFood = favoriteFood
        self.isSleppy = True
        self.isHungry = True

    def FeedCat(self):
        if self.isHungry == True:
            print("Nakarm kota!")
            print(f"Podaj mu {self.favoriteFood}")
            self.isHungry = False
            print("Kot nakarmiony")
        else:
            print("Kot jest już nakarmiony")
    def IsCatSleppy(self):
        if self.isHungry == True:
            print("Najpierw nakarm kota!")
        else:
            if self.isSleppy == True:
                print("Kot idzie spać")
                i = 0
                while i != 10:
                    print("zzz")
                    time.sleep(1)
                    i+=1
                self.isSleppy = False
            else:
                print("Kot jest wyspany!")
class Dog(Animal):
    def __init__(self, name, skinType, stillAlive, isDangerous, species, howBig):
        super().__init__(name, skinType, stillAlive, isDangerous, species)
        self.howBig = howBig
        self.isNajlepszyPrzyjacielCzłowieka = True
        self.wantsWalk = True

    def GoForWalk(self):
        if self.wantsWalk == True:
            print("Wyprowadź psa na spacer!")
            time.sleep(10)
            self.wantsWalk = False
        else:
            print("Pisunio jest zadowloony")

    def IsNajlepszyPrzyjacielCzłowieka(self):
        print("Pies to najlepszy przyjaciel człowieka !")

class Bird(Animal):
    def __init__(self, name, skinType, stillAlive, isDangerous, species, canFly):
        super().__init__(name, skinType, stillAlive, isDangerous, species)
        self.canFly = canFly

    def Fly(self):
        if self.canFly.upper()== "TAK":
            print("Ło skubany ale leci!")
        else:
            print(f"{self.name} nie potrafi latać, trochę dziwny ptak")
    def Papuguj(self):
        if self.species == "PAPUGA":
            answer = input("Powiedz coś: ")
            print(answer)
        else:
            print(f"{self.name} nie jest papugą :c")

class Fish(Animal):
    def __init__(self, name, skinType, stillAlive, isDangerous, species):
        super().__init__(name, skinType, stillAlive, isDangerous, species)

    def GulGul(self):
        print("Gul gul")

    def LowderGulGul(self):
        print("GUL GUL GUL!!!")


mruczek = Cat("Mruczek", "czarno - biała sierść", "Tak", "Nie", "dachowiec", "Nie", "Whiskas")
mruczek.IsStillAlive()
mruczek.IsCatSleppy()
mruczek.FeedCat()

benio = Dog("Benio", "brązowa sierść", "Tak", "Nie", "Owczarek Niemiecki", 1.5)
benio.GoForWalk()
benio.IsNajlepszyPrzyjacielCzłowieka()

dodo = Bird("Piotrek", "pióra", "Nie", "Nie", "Dodo", "Nie")
dodo.Fly()
dodo.Papuguj()
dodo.IsStillAlive()

rekin = Fish("Konrad", "rybna", "Tak", "Tak", "rekin")
rekin.LowderGulGul()
rekin.IsDangerousInfo()
rekin.ListOfAnimals()