class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative!")

# Usage
acc = BankAccount(1000)
print(acc.get_balance())

acc.set_balance(500)
print(acc.get_balance())

acc.set_balance(-200)  # invalid