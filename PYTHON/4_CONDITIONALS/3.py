print("=== Restaurant Menu ===")

print("1 - Burger")
print("2 - Pizza")
print("3 - Pasta")
print("4 - Coffee")

choice = int(input("Enter item number: "))

match choice:
    case 1:
        print("Burger selected")
        print("Price: ₹120")
    case 2:
        print("Pizza selected")
        print("Price: ₹250")
    case 3:
        print("Pasta selected")
        print("Price: ₹180")
    case 4:
        print("Coffee selected")
        print("Price: ₹80")
    case _:
        print("Invalid item selected")

print("Order completed.")
