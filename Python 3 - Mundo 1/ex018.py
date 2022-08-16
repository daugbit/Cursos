from math import sin, cos, tan, radians
angle = float(input('Digite o valor de um ângulo qualquer, em graus (º): '))
print(f'Para o ângulo informado ({angle}º),', end=" ")
print('o SENO é de ', sin(radians(angle)), end=" ")
print('o COSSENO é de ', cos(radians(angle)), end=" ")
print('e a TANGENTE é de ', tan(radians(angle)))
