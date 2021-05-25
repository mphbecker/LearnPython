from enum import Enum


class Sex(Enum):
    MALE = "male"
    FEMALE = "female"


class Human:
    def __init__(self, age: int, sex: Sex, name: str):
        self.age = age
        self.sex = sex
        self.name = name
        # _varName == private varName

    # this is get
    @property
    def age(self):
        return self._age

    @property
    def sex(self):
        return self._sex

    @property
    def name(self):
        return self._name

    # this is set
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("U stupid? age always not negative, u no?")
        self._age = age

    @sex.setter
    def sex(self, sex):
        self._sex = sex

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Please name!")
        if name == "":
            raise ValueError("Please name a name :)")
        self._name = name
