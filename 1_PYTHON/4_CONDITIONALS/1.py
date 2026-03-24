#if statement

print("=== Positive & Divisible by 5 Checker ===")

num = 10
if num > 0:
    print("The number is positive.")
    if num % 5 == 0:
        print("It is also divisible by 5.")
    print("Check completed.")

print("Program finished.")

#if-else

print("=== Eligibility Checker ===")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
    print("You can apply for a driving license.")
else:
    print("You are not eligible to vote.")
    years_left = 18 - age
    print("You need to wait", years_left, "more years.")







