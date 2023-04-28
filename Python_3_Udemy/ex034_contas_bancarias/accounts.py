from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, branch: int, account_num: int, balance: float =0):
        self.branch = branch
        self.account_num = account_num
        self.balance = balance

    @abstractmethod
    def withdrawal(self, value: float): ...

    def deposit(self, value: float):
        self.balance += value
        self.details(f'DEPÓSITO: R${value}')

    def details(self, msg=''):
        print(f'O seu saldo é de R${self.balance:.2f} - {msg}')


class CheckingAccount(Account):
    def __init__(self, branch: int, account_num: int, balance: float = 0, limit: float = 0):
        super().__init__(branch, account_num, balance)
        self.limit = limit

    def withdrawal(self, value: float):
        if value > (self.balance + self.limit):
            print(f'Limite insuficiente (R${self.limit})')
            self.details(f'Valor requisitado: R${value}')
            return None

        self.balance -= value
        self.details(f'SAQUE: R${value}')


class SavingsAccount(Account):
    def withdrawal(self, value: float):
        if value > self.balance:
            print('Saldo insuficiente!')
            self.details(f'Valor requisitado: R${value}')
            return None

        self.balance -= value
        self.details(f'SAQUE: R${value}')

    def __repr__(self):

