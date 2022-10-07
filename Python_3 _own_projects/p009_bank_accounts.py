Class Conta:
	def __init__(self, number, type, owner)
	  self.number = 
	  self.type = 
	  self.owner = 
	

	def open_account():
		self.status = True
		if self.type == 'corrente':
			self.balance = 50
		elif self.type == 'poupança':
			self.balance = 150


	def close_account():
		if self.balance != 0:
			print('Esta conta não pode ser encerrada, pois possui saldo diferente de R$0')
		else:
			self.status = False


	def deposit(value):
		if self.status == False:
			print('Conta desativada')
			return None
		
		self.balance += value
	

	def withdraw(value):
		if self.status == False:
			print('Conta desativada')
			return None
		
		if value > self.balance:
			print('O valor informado é maior que o saldo disponível')
		else:
			self.balance -= value


	def pay_fee():
		if self.status == False:
			print('Conta desativada')
			return None
		
		if self.type == 'corrente':
			self.balance -= 20
		elif self.type == 'poupança':
			self.balance -= 10



client1 = Conta(001, 'corrente', 'Douglas')

client1.open_account()

client1.deposit(100)

client1.withdraw(130)

client1.pay_fee(20)

client1.close_account()
