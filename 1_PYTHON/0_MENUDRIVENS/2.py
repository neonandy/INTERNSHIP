students = {}

while True:
    print("\n--- Student Records ---")
    print("1. Add Student\n2. View All\n3. Search\n4. Delete\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Roll No: ")
        name = input("Name: ")
        marks = float(input("Marks: "))
        students[roll] = {"name": name, "marks": marks}
        print("Student added!")

    elif choice == "2":
        if not students:
            print("No records found.")
        for roll, info in students.items():
            print(f"Roll: {roll} | Name: {info['name']} | Marks: {info['marks']}")

    elif choice == "3":
        roll = input("Enter Roll No to search: ")
        if roll in students:
            info = students[roll]
            print(f"Name: {info['name']}, Marks: {info['marks']}")
        else:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter Roll No to delete: ")
        if roll in students:
            del students[roll]
            print("Deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")



        # I LOVE YOU ANU BANGARUUUUUU😘❤️