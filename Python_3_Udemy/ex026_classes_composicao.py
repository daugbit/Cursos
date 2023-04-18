class Car:
    def __init__(self, name):
        self.name = name
        self.__engine = None
        self.__manufacturer = None

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer


class Manufacturer:
    def __init__(self, name):
        self.name = name


class Engine:
    def __init__(self, name):
        self.name = name


v8 = Engine('V8')
v10 = Engine('V10')
v12 = Engine('V12')

m1 = Manufacturer('Volksvagen')
m2 = Manufacturer('Toyota')
m3 = Manufacturer('Chevrolet')
m4 = Manufacturer('Ford')

c1 = Car('Corolla')
c2 = Car('Camaro')
c3 = Car('Hilux')
c4 = Car('RAV4')
c5 = Car('Fusca')
c6 = Car('Jetta')

c1.engine = v10
c1.manufacturer = m2
c2.engine = v12
c2.manufacturer = m3
c3.engine = v12
c3.manufacturer = m4
c4.engine = v10
c4.manufacturer = m2
c5.engine = v8
c5.manufacturer = m4
c6.engine = v10
c6.manufacturer = m1

print(f'O veículo {c1.name}, fabricado pela {c1.manufacturer.name}, utiliza o motor {c1.engine.name}.')
print(f'O veículo {c2.name}, fabricado pela {c2.manufacturer.name}, utiliza o motor {c2.engine.name}.')
print(f'O veículo {c3.name}, fabricado pela {c3.manufacturer.name}, utiliza o motor {c3.engine.name}.')
print(f'O veículo {c4.name}, fabricado pela {c4.manufacturer.name}, utiliza o motor {c4.engine.name}.')
print(f'O veículo {c5.name}, fabricado pela {c5.manufacturer.name}, utiliza o motor {c5.engine.name}.')
print(f'O veículo {c6.name}, fabricado pela {c6.manufacturer.name}, utiliza o motor {c6.engine.name}.')