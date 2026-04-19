# Classes definition

# A Mixin is a "small" class that wasn't designed to exist on its own.
# Its sole purpose is to provide additional methods to other classes
# through multiple inheritance.
class MROLoggerMixin:
    """This mixin class demonstrates its use in a multiple inheritance context and the addition of behavior to other class(es)."""

    def get_mro_info(self) -> str:
        return self.__class__.mro()


class Animal:
    """Class that abstracts the representation of an Animal"""

    def __init__(self, number_of_legs):
        self.number_of_legs = number_of_legs

    def __str__(self):
        return f'{self.__class__.__name__} {{{", ".join([f"{k}:{v}" for k, v in self.__dict__.items()])}}}'


# The use of K args (**kw) is necessary because, in the context of multiple
# inheritance, the mapping of class attributes is done dynamically,
# according to the sequence of parent classes defined in the child class.
class Mammal(Animal):
    """Class that abstracts the representation of a Mammal"""

    def __init__(self, fur_color, **kw):
        self.fur_color = fur_color
        super().__init__(**kw)


class Bird(Animal):
    """Class that abstracts the representation of a Bird"""

    def __init__(self, beak_color, **kw):
        self.beak_color = beak_color
        super().__init__(**kw)


class Dog(Mammal):
    """Class that abstracts the representation of a Dog"""

    pass


class Cat(Mammal):
    """Class that abstracts the representation of a Cat"""

    pass


class Lion(Mammal):
    """Class that abstracts the representation of a Lion"""

    pass


class Platypus(Mammal, Bird, MROLoggerMixin):
    """Class that abstracts the representation of a Platypus (i.e., a mammal and a bird), where the concept of multiple inheritance is applied"""

    pass


# Using classes

# Using classes with single inheritance
d1 = Dog(number_of_legs=4, fur_color='white')
print(d1)

c1 = Cat(number_of_legs=3, fur_color='white and black')
print(c1)

l1 = Lion(number_of_legs=4, fur_color='brown')
print(l1)

# Using classes with multiple inheritance
platypus = Platypus(number_of_legs=4, fur_color='red', beak_color='orange')
print(platypus)

# Since the __mro__() attribute is accessible in every class definition, and exists in the object class, it could have simply been used in this way.
# print(platypus.__class__.mro())

print(platypus.get_mro_info())
