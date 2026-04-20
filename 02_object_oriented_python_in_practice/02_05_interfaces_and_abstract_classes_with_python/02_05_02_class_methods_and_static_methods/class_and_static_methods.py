from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_a_person_from_their_date_of_birth_and_name(cls, year, month, day, name):
        age = date.today().year - int(year)
        return cls(name, age)

    @staticmethod
    def is_of_legal_age(age):
        LEGAL_AGE_OF_MAJORITY = 18
        return age >= LEGAL_AGE_OF_MAJORITY

    def __str__(self):
        return f'{self.__class__.__name__} {{{", ".join([f"{k}: {v}" for k, v in self.__dict__.items()])}}}'


p1 = Person('Doe, John', 20)
print(p1)
print(f'Person.is_of_legal_age(p1.age) ==> {Person.is_of_legal_age(p1.age)}')

p2 = Person.create_a_person_from_their_date_of_birth_and_name(2018, 12, 2, 'Doe, Mary')
print(p2)
print(f'Person.is_of_legal_age(p2.age) ==> {Person.is_of_legal_age(p2.age)}')
