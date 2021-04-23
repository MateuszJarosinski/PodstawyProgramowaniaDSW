class Superhero:
    def __init__(self,superheroName,realName,superpower,health,strenght,agility):
        self.superheroName = superheroName
        self.realName = realName
        self.superpower = superpower
        self.health = health
        self.strenght = strenght
        self.agility = agility

    def Attack(self):
        print(f"{self.superheroName}, strike with force equal {self.strenght}")

class Thor():
