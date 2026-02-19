print("=== ATM Machine ===")

balance = 10000

print("1. Withdraw 1000")
print("2. Withdraw 2000")
print("3. Withdraw 5000")
print("4. Check Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    balance -= 1000
    print("Please collect ₹1000")
elif choice == 2:
    balance -= 2000
    print("Please collect ₹2000")
elif choice == 3:
    balance -= 5000
    print("Please collect ₹5000")
elif choice == 4:
    print("Your current balance is ₹", balance)
else:
    print("Invalid selection")

print("Thank you for using ATM.")
