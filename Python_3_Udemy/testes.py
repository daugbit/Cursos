def multiplicador(multiplo):
    def multiplicacao(num):
        return num * multiplo
    return multiplicacao


duplica = multiplicador(2)
triplica = multiplicador(3)
quadruplica = multiplicador(4)

print(duplica(10))
print(triplica(10))
print(quadruplica(10))
