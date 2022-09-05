num = int(input('Quantos termos da sequência Fibonacci você quer visualizar? '))
n1 = 0
n2 = 1
c = 3
print(n1)
print(n2)
while c < num:
    n3 = n2 + n1
    print(n3)
    n1 = n2
    n2 = n3
    c += 1
