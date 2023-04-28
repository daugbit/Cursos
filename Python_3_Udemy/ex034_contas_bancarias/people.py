import accounts


class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'


class Customer(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.account = accounts.Account | None

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r}, {self.account!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = Customer('Marcos', 44)
    c1.account = accounts.SavingsAccount(100, 200, 0)
    print(c1)
