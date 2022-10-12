from ex022_classes_composicao_classes import Cliente

c1 = Cliente('Marcos', 23)
c1.include_address('Lajeado', 'RS')

c2 = Cliente('Sandra', 45)
c2.include_address('Salvador', 'BA')

c3 = Cliente('Ptolomeu', 94)
c3.include_address('São Paulo', 'SP')

print(c1.name, c1.age)
c1.show_addresses()
