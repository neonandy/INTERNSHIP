class BankAccount:

    def __init__(self, account_number, balance):
        self.__account_number = account_number #private variable
        self.__balance = balance #private variable

    #method to deposit, check balance, withdraw money
    #encpsulated methods to access private variables
    def CheckBalance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")

    def Deposit(self, amount):
        print(f'Amount deposited: {amount}')

    def Withdraw(self, amount):
        print(f'Amount withdrawn: {amount}')


#creating object
account_1 = BankAccount("123456789", 5000)


account_1.CheckBalance()
account_1.Deposit(2000)
account_1.CheckBalance()


#chagpt

class BankAccount:

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def check_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")


# Usage
account_1 = BankAccount("123456789", 5000)

account_1.check_balance()
account_1.deposit(2000)
account_1.check_balance()
account_1.withdraw(3000)
account_1.check_balance()