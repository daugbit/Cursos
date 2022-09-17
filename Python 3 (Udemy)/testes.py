matriz = [
    (x, y)
    if y != 2 else (x, y * 100)
    for x in range(1, 4)
    for y in range(1, 5)
    if x != 3
]
print(matriz)
