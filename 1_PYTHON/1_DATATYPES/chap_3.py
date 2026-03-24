#1.Arithmetic Operators ~ Used for mathematical calculations.

"""
Operator	Meaning	Example
+	Addition	a + b
-	Subtraction	a - b
*	Multiplication	a * b
/	Division	a / b
//	Floor Division	a // b
%	Modulus	a % b
**	Exponent	a ** b
"""

#Example

from doctest import Example


a = 10
b = 3
print(a + b)   # 13
print(a // b)  # 3
print(a ** b)  # 1000

#2. Comparison ~ Used to compare two values. Result is True or False.

"""
Operator	Meaning	Example
==	Equal to	a == b
!=	Not equal to	a != b
>	Greater than	a > b
<	Less than	a < b
>=	Greater or equal	a >= b
<=	Less or equal	a <= b
"""

#Example

age = 20
print(age >= 18)  # True

# 3.Logical Operators ~ (Used to combine conditions)

"""
and -	Both conditions must be True
or	- Any one condition True
not	- Reverse the result

"""

#Example

age = 22
has_id = True

print(age >= 18 and has_id)   # True
print(not has_id)             # False

#4. Conditional (Ternary) Operator

"""
Used to write short if-else.

Syntax

result = value_if_true if condition else value_if_false
"""

#Example

age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)

#5. Operator Precedence (Quick Tip)

"""
Order of execution:

()

**

* / // %

+ -

Comparison

Logical
"""

#Example

result = 10 + 2 * 3
print(result)  # 16