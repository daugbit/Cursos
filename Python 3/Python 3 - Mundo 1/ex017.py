import math
cat_op = float(input('Informe o comprimento do cateto oposto: '))
cat_ad = float(input('Informe o comprimento do cateto adjacente: '))
hyp = math.hypot(cat_op, cat_ad)
print(f'A hipotenusa deste triângulo mede {hyp:.2f}')
