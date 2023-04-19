from log import LogFileMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            return True
        return False

    def desligar(self):
        if self._ligado:
            self._ligado = False
            return True
        return False


class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        command = super().ligar()
        if command:
            self.log_success(f'{self._nome} está ligado')
        else:
            self.log_error(f'{self._nome} já está ligado')

    def desligar(self):
        command = super().desligar()
        if command:
            self.log_success(f'{self._nome} está desligado')
        else:
            self.log_error(f'{self._nome} já está desligado')

