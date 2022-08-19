height = float(input('Qual a sua altura (m)? '))
weight = float(input('Qual o seu peso (kg)? '))
IMC = weight / height ** 2
if IMC <= 18.5:
    status = 'abaixo do seu peso ideal'
elif IMC <= 25:
    status = 'no seu peso ideal'
elif IMC <= 30:
    status = 'com sobrepeso'
elif IMC <= 35:
    status = 'com obesidade nível I'
elif IMC <= 40:
    status = 'com obesidade nível II'
else:
    status = 'com obesidade mórbida'
print(f'O seu IMC é igual a {IMC:.1f} e você está {status}.')