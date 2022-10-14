class LogCenter:
    def status_log(self, msg):
        self.write_log(f'STATUS: {msg}')

    def error_log(self, msg):
        self.write_log(f'ERROR: {msg}')

    @staticmethod
    def write_log(msg):
        with open('log.log', 'a+') as log:
            log.write(msg)
            log.write('\n')


class Electronic:
    def __init__(self, elec_type):
        self.elec_type = elec_type
        self.power = False

    def turn_on(self):
        if self.power:
            print(f'O {self.elec_type} já está ligado')
            return
        else:
            self.power = True
            print(f'{self.elec_type.title()} ligado com sucesso.')
            return

    def turn_off(self):
        if not self.power:
            print(f'O {self.elec_type} já está desligado.')
            return
        else:
            self.power = False
            print(f'{self.elec_type.title()} desligado com sucesso.')
            return


class Smartphone(Electronic, LogCenter):
    def __init__(self, elec_type, brand, model):
        super().__init__(elec_type)
        self.brand = brand
        self.model = model
        self.wifi = False

    def wifi_on(self):
        if not self.power:
            error = f'O {self.brand} {self.model} está desligado.'
            self.error_log(error)
            print(error)
            return
        elif self.wifi:
            error = f'O wifi do {self.brand} {self.model} já está ligado.'
            self.error_log(error)
            print(error)
            return
        else:
            self.wifi = True
            status = f'O wifi do {self.brand} {self.model} foi ligado com sucesso.'
            self.status_log(status)
            print(status)
            return

    def wifi_off(self):
        if not self.power:
            error = f'O {self.brand} {self.model} está desligado.'
            self.error_log(error)
            print(error)
            return
        elif not self.wifi:
            error = f'O wifi do {self.brand} {self.model} já está desligado.'
            self.error_log(error)
            print(error)
            return
        else:
            self.wifi = False
            status = f'O wifi do {self.brand} {self.model} foi desligado com sucesso.'
            self.status_log(status)
            print(status)
            return
