"""
Programa para simples manipulação de strings através de list comprehension
"""
string = '012345678901234567890123456789'

new_string = [string[index:index + 10] for index in range(0, len(string), 10)]
print(new_string)
print()

newer_string = '.'.join([string[index:index + 10] for index in range(0, len(string), 10)])
print(newer_string)
