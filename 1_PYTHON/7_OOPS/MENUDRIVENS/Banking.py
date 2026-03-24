class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0 #protected / encapsulation
    
    def check_balance(self):
        print("Balance:",self._balance)
        
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposit Successful. Updated Balance:{self._balance}")
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdrawal Successful. Updated Balance:{self._balance}")
        else:
            print("Insufficient Balance!")

class SavingsAccount(Account): #inheritance
    def calculate_interest(self):
        INTEREST_RATE = 0.05 #5%
        interest = self._balance * INTEREST_RATE
        print("Interest:",interest)

class CurrentAccount(Account):
    def withdraw(self, amount): #override / polymorphism
        OVERDRAFT_LIMIT = 1000
        if self._balance + OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            print(f"Withdrawal Successful. Updated Balance:{self._balance}")
        else:
            print("Ask is Over limit")

class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__accounts = {} #private / encapsulation

    def create_account(self, id, holder_name, account_type):
        if account_type == "Savings":
            new_account = SavingsAccount(id, holder_name)
        elif account_type == "Current":
            new_account = CurrentAccount(id, holder_name)
        
        self.__accounts[id] = new_account
        print("Account Created Successfully")
        return new_account
            
    def get_account(self, id):
        if id not in self.__accounts:
            print("Acconut not found")
        else:
            account = self.__accounts[id]
        print(f"\nID:{account.id}\n Holder Name {account.holder_name}")
        return account
    
#creating objects

NBK = Bank("Nandan Bank of Karnataka", "Hosadurga")

S1 = NBK.create_account("1", "Anvik", "Savings")
C1 = NBK.create_account("2", "Virat kohli", "Current")

S1.deposit(1000)
C1.deposit(20) 

S1.withdraw(2000)
C1.withdraw(20)

S1.check_balance()
C1.check_balance()

S1.calculate_interest()

#errors i did

# The problems in the existing code are:
# 1. In create_account, 'type' is used instead of the parameter 'account_type'.
# 2. In create_account, the SavingsAccount was not being added to the self.__accounts dictionary.
# 3. In create_account, the indentation for adding to the dictionary and returning was only inside the 'elif' block.
# 4. In deposit and withdraw methods, f-strings are missing the 'f' prefix, so {self._balance} prints as literal text.
# 5. In get_account, if the ID is not found, the code still tries to access 'account', which will cause an UnboundLocalError.

