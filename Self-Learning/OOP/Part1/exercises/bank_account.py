# Definne a new class called BankAccount.
# Each BankAccount should have an owner, specied when a new BankAccount is created like  BankAccount("Charlie")
# Each BankAccount should have a balance attribute   that always starts out as 0.0
# Each instance should have a deposit method that accepts a number and adds it to the balance. It should return the new balance.
# Each instance should have a withdraw method that accepts a number and subtracts it from the balance. It should return the new
# balance.


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        return self.balance

    def withdraw(self, withdraw):
        self.balance -= withdraw
        return self.balance


acct = BankAccount('Darcy')
print(acct.owner)  # Darcy
print(acct.balance)  # 0.0
print(acct.deposit(10))  # 10.0
print(acct.withdraw(3))  # 7.0
print(acct.balance)  # 7.0
