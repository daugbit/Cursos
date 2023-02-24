phrase = input('Digite uma frase: ').upper()
letters = []
verif_letters = []
i = 0

while i < len(phrase):
    letter = []
    if phrase[i] not in verif_letters and phrase[i] != ' ':
        verif_letters.append(phrase[i])
        letter.append(phrase[i])
        letter.append(phrase.count(phrase[i]))
        letters.append(letter)
    i += 1

letters.sort(key=lambda j: j[1], reverse=True)

for k in letters:
    print(f'A letra "{k[0]}" apareceu {k[1]} vez(es)')
