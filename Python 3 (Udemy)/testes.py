import sys

lista1 = [x for x in range(1000)]
lista2 = (x for x in range(10))
print(sys.getsizeof(lista1))
print(sys.getsizeof(lista2))
