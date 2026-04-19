# Defining a super class or parent class
class Animal:
    def __init__(self, birth_date, gender):
        self.birth_date = birth_date
        self.gender = gender

    def eat(self) -> str:
        return f'{self.__class__.__name__} eating. . .'


# Defining a derived  class or child class
class Mammal(Animal):  # Mammal extends Animal
    def __init__(self, birth_date, gender):
        super().__init__(birth_date, gender)

    def eat(self) -> str:
        return f'{self.__class__.__name__} is sucking (milk). . .'


# Defining a derived  class or child class
class Carnivore(Animal):  # Carnivore extends Animal
    def __init__(self, birth_date, gender):
        super().__init__(birth_date, gender)

    def eat(self) -> str:
        return f'{self.__class__.__name__} is eating (devouring meat)...'


# Instantiating classes
a1 = Mammal('1900-01-01', 'cow')
print(a1.eat())

a2 = Carnivore('1900-05-01', 'lion')
print(a2.eat())

a3 = Animal('1900-05-01', 'animal jhonn')
print(a3.eat())
