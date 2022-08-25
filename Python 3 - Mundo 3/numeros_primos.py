# Números primos
end = int(input('Até qual número você quer calcular os primos? '))
print(2)
for num in range(3, end + 1, 2):
    cont = 1
    for c in range(3, num // 2, 2):
        if num % c == 0:
            cont += 1
        if cont > 2:
            break
    if cont <= 2:
        print(num)
