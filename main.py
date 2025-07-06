import os
import json

class calculator:
	"""Full Calculator program class"""
	def __init__(self):
		self.username = False
		self.history = False
		self.expression = ''
		self.explist = []
		self.test_case = 1
		self.operdict = {}
		self.history = {}

	def home(self):
		os.system('cls')
		self.starpat()
		print('\tCalculator Program')
		self.starpat()
		self.userfetch()
		print(f"\t\t\tWelcome {self.username}!\n")
		print("What do you wanna do?")
		print("1. Perform new operation")
		print("2. Check previous operation")
		print("3. Exit")
		self.option_choose_main_menu()

	def userfetch(self):
		try:
			with open('username.txt') as f:
				self.username = f.read()
		except FileNotFoundError:
			self.username = input('Please enter username of the Calculator : ')
			with open('username.txt','w') as f:
				f.write(self.username)
			self.home()

	def starpat(self):
		print(''.join(list('*' for i in range(1,40))))

	def option_choose_main_menu(self):
		while True:
			option = input('Enter the desired option : \t')
			match option:
				case '1':
					self.newOperation()
					break
				case '2':
					self.history_check()
					break
				case '3':
					exit()
				case _:
					print('Wrong Entered! Enter again!')

	def newOperation(self):
		os.system('cls')
		while self.test_case:
			self.expression = input('\nEnter full expression (No space needed) : \n\n')
			for i in range(0, len(self.expression)):
				if self.expression[i] not in list(str(x) for x in range(0, 10)) + ['+', '-', '*', '/', '%', ' ']:
					print("wrong entered! Enter again")
					self.test_case = 1
					break
				else:
					self.test_case = 0
		self.test_case = -1
		for i in range(0, len(self.expression)):
			if self.expression[i] in ['+', '-', '*', '/', '%', ' ']:
				if self.expression[i] != ' ':
					self.test_case += 1
					self.explist.append(self.expression[i]) 
			else:
				self.test_case += 1
				self.explist.append(int(self.expression[i]))
		self.operator_update()
		while self.operdict.keys():
			self.operator_perform()
		print(f"\nresult : {self.explist[0]}")
		self.history_update()
		self.after_operation()

	def operator_update(self):
		self.operdict = {}
		for i in range(0, len(self.explist)):
			if self.explist[i] in ['+', '-', '*', '/', '%']:
				self.operdict[self.explist[i]] = i

	def operator_perform(self):
		if '%' in self.operdict.keys():
			self.explist[self.operdict['%'] - 1] = self.explist[self.operdict['%'] - 1] % self.explist[self.operdict['%'] + 1]
			del self.explist[self.operdict['%']]
			del self.explist[self.operdict['%']]
			self.operator_update()
		elif '/' in self.operdict.keys():
			self.explist[self.operdict['/'] - 1] = self.explist[self.operdict['/'] - 1] / self.explist[self.operdict['/'] + 1]
			del self.explist[self.operdict['/']]
			del self.explist[self.operdict['/']]
			self.operator_update()
		elif '*' in self.operdict.keys():
			self.explist[self.operdict['*'] - 1] = self.explist[self.operdict['*'] - 1] * self.explist[self.operdict['*'] + 1]
			del self.explist[self.operdict['*']]
			del self.explist[self.operdict['*']]
			self.operator_update()
		elif '+' in self.operdict.keys():
			self.explist[self.operdict['+'] - 1] = self.explist[self.operdict['+'] - 1] + self.explist[self.operdict['+'] + 1]
			del self.explist[self.operdict['+']]
			del self.explist[self.operdict['+']]
			self.operator_update()
		elif '-' in self.operdict.keys():
			self.explist[self.operdict['-'] - 1] = self.explist[self.operdict['-'] - 1] - self.explist[self.operdict['-'] + 1]
			del self.explist[self.operdict['-']]
			del self.explist[self.operdict['-']]
			self.operator_update()

	def after_operation(self):
		self.set_default()
		option = True
		while option:
			option = input("\nPress 1. to go back 2. to exit :\t")
			match option:
				case '1':
					self.home()
				case '2':
					exit()
				case _:
					print('Wrong entered enter again!')

	def set_default(self):
		self.username = False
		self.history = False
		self.expression = ''
		self.explist = []
		self.test_case = 1
		self.operdict = {}

	def history_check(self):
		os.system('cls')
		try:
			with open('history.json') as f:
				self.starpat()
				print('Calculator History'.center(40))
				self.starpat()
				print('\n')

				self.history = json.load(f)
				if not self.history:
					print('No History Found!\n')
				else:
					# Header
					print(f"| {'No.':^5} | {'Expression':^20} | {'Result':^8} |")
					print('-' * 40)

					# Body
					for idx, (expr, result) in enumerate(self.history.items(), start=1):
						print(f"| {idx:^5} | {expr:^20} | {result:^8} |")
		except FileNotFoundError:
			print('No History Found!\n')

		while True:
			option = input('\nPress 1. to Back 2. to exit : \t')
			match option:
				case '1':
					self.home()
				case '2':
					exit()
				case _:
					print('Please Enter again !')

	def history_update(self):
		try:
			with open('history.json', 'r') as f:
				self.history = json.load(f)
		except (FileNotFoundError, json.decoder.JSONDecodeError):
			self.history = {}

		self.history[self.expression] = self.explist[0]

		with open('history.json', 'w') as f:
			json.dump(self.history, f, indent=4)

if __name__ == '__main__':
	program = calculator()
	program.home()