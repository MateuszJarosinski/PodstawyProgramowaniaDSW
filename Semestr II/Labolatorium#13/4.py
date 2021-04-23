class Student:
    def __init__(self, name, surname, age, energy, percentOfAlcochol,):
        self.name = name
        self.surname = surname
        self.age = age
        self.energy = energy
        self.percentOfAlcochol = percentOfAlcochol

    def drinkCoffe(self):
        if self.energy < 30:
            print(f"{self.name} ma niewystarczającą ilośc kawy w organiźmie, wypij kawę!")
            while self.energy <= 100:
                print("Wypito kawę")
                self.energy += 25
            print(f"{self.name} jest pełęn sił!")
        elif self.energy < 80:
            print("Nie wygląda to dobrze, czas na kawę")
            while self.energy <= 100:
                print("Wypito kawę")
                self.energy += 25
            print(f"{self.name} jest pełen sił!")
        else:
            print(f"{self.name} jest gotowy do pracy, czas na majcę")

MateuszKapelusz = Student("Mateusz", "Kapelusz", "20", 70, 0.0)
MateuszKapelusz.drinkCoffe()
