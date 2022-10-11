from ex020_classes_associacao_classes import *

car1 = Car('Tesla', 'Model S')
car2 = Car('Porshe', 'Cayenne')

fuel1 = Fuel('gasolina')
fuel2 = Fuel('eletricidade')

wheel1 = Wheel('18"')
wheel2 = Wheel('15"')

car1.fuel = fuel2
car1.wheel = wheel2
car2.fuel = fuel1
car2.wheel = wheel1

car1.descricao()
car2.descricao()
