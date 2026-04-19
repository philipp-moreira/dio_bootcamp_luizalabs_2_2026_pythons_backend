# Defining a super class or parent class
class Animal:
    def __init__(self, birth_date, gender):
        self.birth_date = birth_date
        self.gender = gender

    def eat(self) -> str:
        return f'{self.__class__.__name__} eating. . .'

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {{{", ".join([f"{k}: {v}" for k, v in self.__dict__.items()])}}}'


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
print(a1)  # Uses parent class method/function
print(a1.eat())

a2 = Carnivore('1900-05-01', 'lion')
print(a2)  # Uses parent class method/function
print(a2.eat())

a3 = Animal('1900-05-01', 'animal john')
print(a3)  # Uses parent class method/function
print(a3.eat())
