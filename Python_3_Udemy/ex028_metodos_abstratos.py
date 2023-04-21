from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = name

    @property
    # @abstractmethod
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)

    # @property
    # def name(self):
    #     return self._name

    @AbstractFoo.name.setter        # Ao não declarar a @property na classe atual,
    def name(self, name):           # deve-se especificar o nome classe abstrata no @setter.
        self._name = name


foo = Foo('Bar')
print(foo.name)
foo.name = 'Arroz'
print(foo.name)
