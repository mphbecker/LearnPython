from humans.human import Human, Sex


class Teenager(Human):
    def __init__(self, age: int, sex: Sex, name: str):
        super().__init__(age, sex, name)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 12 > age > 20:
            raise ValueError("That's no teeny!")
        self._age = age
