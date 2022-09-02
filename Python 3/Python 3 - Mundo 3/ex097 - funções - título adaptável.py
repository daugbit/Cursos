def escreva(msg):
    length = len(msg) + 4
    print('~' * length)
    print(f'{msg:^{length}}')
    print('~' * length)


escreva('Olá, Mundo!')
escreva('Curso em Vídeo')
escreva('Douglas Augusto Ullmann')
