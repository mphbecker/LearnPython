from humans.human import Human, Sex


class Child(Human):
    def __init__(self, age: int, sex: Sex, name: str):
        super.__init__(age, sex, name)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("U stupid? age always not negative, u no?")
        if age > 12:
            raise ValueError("too old")

        self._age = age
