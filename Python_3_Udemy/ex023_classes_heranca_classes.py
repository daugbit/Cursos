class Membro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Membro):
    def estudar(self):
        print(f'O aluno {self.nome} está estudando.')


class Professor(Membro):
    def dar_aula(self):
        print(f'O professor {self.nome} está dando aula.')


class Diretor(Membro):
    def dar_bronca(self):
        print(f'O diretor {self.nome} está dando bronca.')
