class Cliente:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.enderecos = []

    def include_address(self, city, state):
        self.enderecos.append(Endereco(city, state))

    def show_addresses(self):
        for endereco in self.enderecos:
            print(f'{endereco.city}/{endereco.state}')


class Endereco:
    def __init__(self, city, state):
        self.city = city
        self.state = state
