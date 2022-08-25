nums = [[], []]
for n in range(1, 8):
    num = int(input(f'Digite o {n}º número: '))
    if num % 2 != 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
print(f'Os valores pares digitados foram: {sorted(nums[1])}.')
print(f'Os valores ímpares digitados foram: {sorted(nums[0])}.')
