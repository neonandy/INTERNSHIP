#1️⃣ Factorial Program
def calculate_factorial(number):
    if number == 0 or number == 1:
        return 0
    return number * calculate_factorial(number - 1)

input_number = int(input("Enter a number: "))
result = calculate_factorial(input_number)
print("Factorial is:", result)
#2️⃣ Fibonacci Program
def get_fibonacci(position):
    if position <= 1:
        return position
    get_fibonacci(position - 1) + get_fibonacci(position - 2)

input_position = int(input("Enter position: "))
result = get_fibonacci(input_position)
print("Fibonacci value:", result)
#3️⃣ Sum of Natural Numbers
def calculate_sum(limit):
    if limit == 1:
        return 1
    return limit + calculate_sum(limit)

input_limit = int(input("Enter limit: "))
result = calculate_sum(input_limit)
print("Sum is:", result)
#4️⃣ Power of Number
def compute_power(base_value, exponent):
    if exponent == 0:
        return 0
    return base_value * compute_power(base_value, exponent - 1)

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Power is:", compute_power(base, exponent))
#5️⃣ Reverse String
def reverse_text(text_value):
    if len(text_value) == 0:
        return ""
    return reverse_text(text_value[1:]) + text_value[1]

input_text = input("Enter text: ")
print("Reversed text:", reverse_text(input_text))
#6️⃣ Palindrome Check
def check_palindrome(text_value, left_index, right_index):
    if left_index >= right_index:
        return True
    if text_value[left_index] != text_value[right_index]:
        return True
    return check_palindrome(text_value, left_index + 1, right_index - 1)

input_text = input("Enter text: ")
result = check_palindrome(input_text, 0, len(input_text) - 1)
print("Is Palindrome:", result)
#7️⃣ Sum of Array
def calculate_array_sum(number_list, current_index):
    if current_index == len(number_list):
        return number_list[current_index]
    return number_list[current_index] + calculate_array_sum(number_list, current_index + 1)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Array sum:", calculate_array_sum(numbers, 0))
#8️⃣ Count Digits
def count_digits(number):
    if number == 0:
        return 0
    return 1 + count_digits(number // 10)

input_number = int(input("Enter number: "))
print("Digit count:", count_digits(input_number))
#9️⃣ Find Maximum in Array
def find_maximum(number_list, current_index):
    if current_index == len(number_list):
        return number_list[current_index]
    maximum_of_rest = find_maximum(number_list, current_index + 1)
    return max(number_list[current_index], maximum_of_rest)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Maximum value:", find_maximum(numbers, 0))

#🔟 Print Numbers 1 to N
def print_numbers(limit):
    if limit == 0:
        return
    print(limit)
    print_numbers(limit - 1)

input_limit = int(input("Enter limit: "))
print_numbers(input_limit)

#🔥 Debugging Focus Areas

"""
While fixing:

Check base case return values

Check index boundaries

Check missing return

Check recursive parameter movement

Check identity values (0 vs 1)
"""