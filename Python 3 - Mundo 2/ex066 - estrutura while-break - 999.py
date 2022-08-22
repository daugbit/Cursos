cont = sum = num = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        sum += num
        cont += 1
    else:
        break
print(f'Ao final, foram digitados {cont} números e a soma entre eles foi igual a {sum}.')
