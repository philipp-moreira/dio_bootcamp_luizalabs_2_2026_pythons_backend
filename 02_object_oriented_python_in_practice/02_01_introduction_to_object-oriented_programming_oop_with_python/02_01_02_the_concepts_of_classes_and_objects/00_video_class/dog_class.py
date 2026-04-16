# Defining class --> Concept | Pillar of OOP: Abstraction
class Dog:
    """Dog Class
    Defined attributes and behaviors for a dog. It's abstraction.
    """

    # Class constructor
    def __init__(self, name, color, awake=True):
        # Properties/Attributes -> Initialization by constructor
        # However, the properties/attributes remain accessible through direct external changes, violating the encapsulation principle of object-oriented programming.
        self.name = name
        self.color = color
        self.awake = awake

    # Methods or Behaviors
    #  Concept | Pillar of OOP: Encapsulation

    # Self implemented
    def bark(self) -> None:
        print('Woof woof...')

    def sleep(self):
        self.awake = False
        print('Zzzzzzz')

    # Overriding
    # Specializing behavior of the built-in function method to text data type (text/string/str) in the cast action (object to text)
    #  Concept | Pillar of OOP: Polymorphism
    def __str__(self) -> str:
        return '{.....'


# Outside the scope of the class - Using classes as objects
# Or instantiating the class
dog_1 = Dog('Dog 1', 'brown')

print(dog_1)
dog_1.color = 'green'
print(dog_1)
dog_1.bark()
dog_1.sleep()
print(dog_1)
print('dog_1.__doc__ ==> ', dog_1.__doc__)
print(dog_1.__module__)
print('dog_1.__format__', dog_1.__format__)
