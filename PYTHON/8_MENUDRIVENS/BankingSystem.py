def Menu():
    print("----BANKING SYSTEM----")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

balance = 0

while (True):
    Menu()
    choice = int(input("Enter your choice:"))

    if choice == 1:
        print("Balance:",balance)
    elif choice == 2:
        amount = int(input("Enter amount to deposit:"))
        balance += amount
    elif choice == 3:
        amount = int(input("Enter amount to withdraw:"))
        balance -= amount
    elif choice == 4:
        print("Quitting....") 
        break
    else:
        print("Invalid choice! Try Again")
                    
        

