phrase = str(input('Digite uma frase: ')).strip().upper()
splitted = phrase.split()
joined = ''.join(splitted)
count = 0
for c in range(0, len(joined)):
    if joined[c] != joined[len(joined) - (c + 1)]:
        count += 1
if count == 0:
    print(f'A frase {phrase} é um palíndromo: {joined} ->', joined[::-1])
else:
    print(f'A frase {phrase} não é um palíndromo: {joined} ->', joined[::-1])
