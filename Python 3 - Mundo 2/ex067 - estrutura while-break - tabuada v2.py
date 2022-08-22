while True:
    print('=-=' * 15)
    num = int(input('Você quer a tabuada de qual número? '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
