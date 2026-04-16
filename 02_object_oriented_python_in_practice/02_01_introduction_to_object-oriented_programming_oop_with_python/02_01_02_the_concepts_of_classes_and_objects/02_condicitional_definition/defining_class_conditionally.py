obj = None
# build_a_physical_person = True
# build_a_legal_entity = False

build_a_physical_person = False
build_a_legal_entity = True


if build_a_physical_person:

    class Physical_Person:
        """A class that abstracts and represents a real-world person, containing a name and date of birth"""

        def __init__(self, name, birth_date):
            self.name = name
            self.birth_date = birth_date

        def __str__(self) -> str:
            return '{name: ' + self.name + ', birth_date: ' + self.birth_date + '}'

    obj = Physical_Person('Johnn Doe', '1900-01-01')
else:

    class Legal_Entity:
        """A class that abstracts and represents a legal entity (a company), containing a registered name and a commercial name that the company uses to interact with the public, do marketing and establish its brand"""

        def __init__(self, registered_name, doing_business_as):
            self.registered_name = registered_name
            self.doing_business_as = doing_business_as

        def __str__(self) -> str:
            return (
                '{registered_name: '
                + self.registered_name
                + ', doing_business_as: '
                + self.doing_business_as
                + '}'
            )

    obj = Legal_Entity('dream factory inc', 'Dreams INC')


print(obj)
