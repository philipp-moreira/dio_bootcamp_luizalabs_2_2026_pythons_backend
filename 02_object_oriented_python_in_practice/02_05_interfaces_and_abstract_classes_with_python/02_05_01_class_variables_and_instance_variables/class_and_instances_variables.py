class LogMixin:
    def log(*objs):
        for obj in objs:
            print(obj)


class Student(LogMixin):
    school = 'DIO'

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {{{", ".join([f"'{k}':'{v}'" for k, v in self.__dict__.items()]) + ", " + ", ".join([f"'{k}': '{v}'" for k, v in Student.__dict__.items() if "__" not in k])}}}'


s1 = Student('Doe, John', 1)
s2 = Student('Doe, Mary', 2)
Student.log(s1, s2)
print('-' * 200)

s2.id = 4
Student.log(s1, s2)
print('-' * 200)

# s1.school = 'Python'  # Creates a new variable ofr the object
# s1.__class__.school = 'Python'  # It works, but it's verbose and requires a broader understanding of the logic to identify the class of s1.
Student.school = 'Python'
Student.log(s1, s2)
print('-' * 200)

s3 = Student('Doe, Paul', 3)
Student.log(s1, s2, s3)
print('-' * 200)
