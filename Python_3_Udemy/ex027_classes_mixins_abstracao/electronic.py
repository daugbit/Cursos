from log import LogFileMixin


class Electronic:
    def __init__(self, name):
        self._name = name
        self._on = False

    def power_on(self):
        if not self._on:
            self._on = True
            return True
        return False

    def power_off(self):
        if self._on:
            self._on = False
            return True
        return False


class Smartphone(Electronic, LogFileMixin):
    def power_on(self):
        command = super().power_on()
        if command:
            self.log_success(f'{self._name} está ligado')
        else:
            self.log_error(f'{self._name} já está ligado')

    def power_off(self):
        command = super().power_off()
        if command:
            self.log_success(f'{self._name} está desligado')
        else:
            self.log_error(f'{self._name} já está desligado')

