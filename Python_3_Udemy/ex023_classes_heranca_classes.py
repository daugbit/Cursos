class MembroEscola:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'Membro {self.nome} está falando.')


class Aluno(MembroEscola):
    def falar(self):
        print(f'Aluno {self.nome} está falando.')

    def estudar(self):
        print(f'O aluno {self.nome} está estudando.')


class AlunoPrimario(Aluno):
    def __init__(self, nome, sobrenome, idade):
        MembroEscola.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        MembroEscola.falar(self)
        Aluno.falar(self)
        print(f'Agora o aluno primário {self.nome} está falando.')


class Professor(MembroEscola):
    def dar_aula(self):
        print(f'O professor {self.nome} está dando aula.')


class Diretor(MembroEscola):
    def dar_bronca(self):
        print(f'O diretor {self.nome} está dando bronca.')
