class Car:
    def __init__(self, maker, model):
        self.__maker = maker
        self.__model = model
        self.__fuel = None
        self.__wheel = None

    @property
    def maker(self):
        return self.__maker

    @property
    def model(self):
        return self.model

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        self.__fuel = fuel

    @property
    def wheel(self):
        return self.__wheel

    @wheel.setter
    def wheel(self, wheel):
        self.__wheel = wheel

    def descricao(self):
        print(f'O veículo {self.__maker} {self.__model} utiliza o combustível {self.fuel.fuel_type},', end=' ')
        print(f'e roda de diâmetro {self.wheel.wheel_diameter}.')


class Wheel:
    def __init__(self, wheel_diameter):
        self.__wheel_diameter = wheel_diameter

    @property
    def wheel_diameter(self):
        return self.__wheel_diameter


class Fuel:
    def __init__(self, fuel_type):
        self.__fuel_type = fuel_type

    @property
    def fuel_type(self):
        return self.__fuel_type
