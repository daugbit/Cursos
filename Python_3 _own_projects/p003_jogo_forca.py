"""
Programa que simula um jogo da forca. A palavra a ser adivinhada
deve ser antecipadamente declarada na variável 'word'.
"""

from time import sleep
import os

word = 'PERFUME'
guesses = 6
right_letters = []
wrong_letters = []
temp_word = '-' * len(word)
color = {'white': '\033[m',
         'red': '\033[31m',
         'yellow': '\033[33m',
         'green': '\033[32m',
         'blue': '\033[34m',
         'alert': '\033[1:31:40m',
         'win': '\033[1:30:42m',
         'lose': '\033[1:30:41m',
         }


def printword():
    """
    Exibe o quadro com a palavra secreta, exibindo as letras já adivinhadas
    e ocultando aquelas que ainda não foram chutadas
    """
    print(color['green'], end='')
    print('~' * 40)
    print('Palavra secreta:', temp_word)
    print('~' * 40)
    print(color['white'], end='')


def guess():
    """
    Função que recebe o input e verifica se o mesmo é um caractere válido (a-z).
    """
    global color
    try:
        letter = str(input('Tente uma letra: ')).strip().upper()[0]
    except (ValueError, IndexError):
        print(color['alert'], 'Entrada inválida. Digite uma letra.', color['white'], sep='')
        sleep(1)
        return ''
    else:
        if not letter.isalpha():
            print(color['alert'], 'Entrada inválida. Digite uma letra.', color['white'], sep='')
            return None
        return letter


def verif():
    """
    Função que verifica se:
    1) a letra digitada já foi tentada anteriormente. Caso negativo:
    2) a letra digitada está na palavra
    Caso a letra esteja na palavra, adiciona a mesma em right_letters e executa
    a montagem parcial da palavra secreta.
    Caso a letra não esteja na palavra, adiciona a mesma em wrong_letters e
    desconta uma tentativa do total
    """
    global letter, word, wrong_letters, right_letters, temp_word, guesses
    if letter in right_letters or letter in wrong_letters:
        print(color['yellow'], 'Você já tentou esta letra! Escolha outra.', color['white'], sep='')
        sleep(1)
    elif letter in word:
        print(color['blue'], f'Demais! A palavra tem a letra {letter}!', color['white'], sep='')
        sleep(1)
        right_letters.append(letter)
        word_build()
    else:
        print(color['red'], f'Ah, não! A palavra não tem a letra {letter}!', color['white'], sep='')
        sleep(1)
        wrong_letters.append(letter)
        word_build()
        guesses -= 1


def word_build():
    """
    Função que faz a montagem parcial da palavra secreta com base nas letras certas informadas pelo usuário.
    """
    global temp_word
    temp_word = ''
    for ind, caract in enumerate(word):
        if caract in right_letters:
            temp_word += caract
        else:
            temp_word += '-'


# PROGRAMA PRINCIPAL

while guesses > 0:
    os.system("clear")
    print('\n', ' JOGO DA FORCA '.center(40, '*'), sep='')
    printword()
    print(f'Letras erradas: {wrong_letters}')
    print(f'Tentativas restantes: {guesses}')
    letter = guess()
    if letter:
        verif()

    if temp_word == word:
        os.system("clear")
        printword()
        print(color['win'], f'VITÓRIA!!!'.center(40), color['white'], sep='')
        break

else:
    print(color['lose'], 'FORCA!!!'.center(40), color['white'], sep='')
