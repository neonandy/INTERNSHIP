#create a program where users can:
#add items
#Remove items
#view the total price
#Exit


def grocery_store():
    cart = []
    def menu():
        print("\n--- Grocery Store Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Total Price")
        print("4. Exit")
    
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item name: ")
            price = float(input("Enter price: "))
            cart.append((item, price))
            print(f"{item} added to cart.")

        elif choice == '2':
            item = input("Enter item name to remove: ")
            found = False
            for i in cart:
                if i[0] == item:
                    cart.remove(i)
                    print(f"{item} removed.")
                    found = True
                    break
            if not found:
                print("Item not found.")

        elif choice == '3':
            total = sum(price for _, price in cart)
            print(f"Total Price: ₹{total}")

        elif choice == '4':
            print("Exiting Grocery Store...")
            break

        else:
            print("Invalid choice!")

grocery_store()