def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls


def my_planet(method):
    def iner(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if 'Terra' in result:
            return 'Você está em casa'
        return result

    return iner


@add_repr
class Team:
    def __init__(self, name):
        self.nome = name


@add_repr
class Planet:
    def __init__(self, name):
        self.name = name

    @my_planet
    def say_name(self):
        return f'O planeta é {self.name}'


brasil = Team('Brasil')
portugal = Team('Portugal')

terra = Planet('Terra')
marte = Planet('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

print(terra.say_name())
print(marte.say_name())
