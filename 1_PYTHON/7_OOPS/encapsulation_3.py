class BankAccount:

    def __init__(self, balance, pin):
        self.owner = "nandan"    # public   — accessible anywhere
        self._pin = pin             # protected — convention: don't touch from outside
        self.__balance = balance    # private  — name-mangled to _BankAccount__balance

    def get_balance(self):          # controlled access via method
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

acc = BankAccount(5000, 1234)
print(acc.get_balance())
   # 5000
#print(acc.__balance)     # AttributeError — blocked!

class BankAccount:
  def __init__(self, owner, balance, pin):
    self.owner = owner # public
    self._bank = "SBI" # protected
    self.__balance = balance # private (name-mangled)
    self.__pin = pin # private

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount

  def withdraw(self, amount):
    if amount > self.__balance:
      raise ValueError("Insufficient funds")
    self.__balance -= amount

  def get_balance(self): # controlled read
    return self.__balance

  def verify_pin(self, pin):
    return self.__pin == pin

acc = BankAccount("Nandan", 5000, 1234)
print(acc.get_balance()) # 5000