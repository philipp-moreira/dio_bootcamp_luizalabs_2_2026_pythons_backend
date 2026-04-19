class Person:
    """A class abstracting the representation of a Person from the real world."""

    # Constructor
    def __init__(self, name, birth_date):
        """Person's name
        Private attribute, by convention. Don't changes out of the class
        """
        # Attributes
        self._name = name
        """Private attribute, do not access or modify outside the class.
        """
        self._birth_date = birth_date
        """Private attribute, do not access or modify outside the class.
        """

    # Methods or Functions
    def __str__(self) -> str:
        return f'{self.__class__.__name__} {{{", ".join([f"{k}: {v}" for k, v in self.__dict__.items()])}}}'


p1 = Person('John Doe', '1980-01-04')
print(p1)

# p1._name # This is wrong, because, make direct access to a private attribute. Violation tha Python's convention
