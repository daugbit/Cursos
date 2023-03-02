# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

hits = 0

for question in perguntas:
    print(question['Pergunta'])

    for i, option in enumerate(question['Opções']):
        print(f'{i}) {option}')
    answer = input('Opção: ')

    if question['Opções'][int(answer)] == question['Resposta']:
        hits += 1
        print('Você acertou!')
    else:
        print('Você errou!')
    print('-=' * 20)

print(f'Você acertou {hits} de 3 perguntas')