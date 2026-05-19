"""
Arithmetic & Assignment Operators
==================================
Run: python3 01_arithmetic_and_assignment.py

Covers:
- Basic arithmetic: +, -, *, /, //, %, **
- Division always returns float
- Floor division truncates toward negative infinity
- Modulo for remainder, even/odd checks, clock math
- Exponentiation and large numbers
- Operator overloading with strings and lists
- Augmented assignment operators (+=, -=, *=, etc.)
"""


# =============================================================================
# ARITHMETIC OPERATORS
# =============================================================================

print("=" * 55)
print("  ARITHMETIC OPERATORS")
print("=" * 55)

# Basic operations
print(f"\n  10 + 3  = {10 + 3}")    # Addition
print(f"  10 - 3  = {10 - 3}")      # Subtraction
print(f"  10 * 3  = {10 * 3}")      # Multiplication
print(f"  10 / 3  = {10 / 3}")      # True division (always float)
print(f"  10 // 3 = {10 // 3}")     # Floor division (integer result)
print(f"  10 % 3  = {10 % 3}")      # Modulo (remainder)
print(f"  2 ** 10 = {2 ** 10}")     # Exponentiation

# Division always returns float
print(f"\n  --- Division Details ---")
print(f"  10 / 2 = {10 / 2}")       # 5.0 (not 5!)
print(f"  type(10 / 2) = {type(10 / 2)}")  # <class 'float'>

# Floor division truncates toward NEGATIVE infinity
print(f"\n  --- Floor Division ---")
print(f"   7 // 2  = {7 // 2}")     # 3
print(f"  -7 // 2  = {-7 // 2}")    # -4 (not -3! rounds toward negative infinity)
print(f"   7 // -2 = {7 // -2}")    # -4

# Modulo — incredibly useful
print(f"\n  --- Modulo Uses ---")
print(f"  15 % 4 = {15 % 4}")       # 3 (remainder)
print(f"  10 % 2 = {10 % 2}")       # 0 (even number: n % 2 == 0)
print(f"  11 % 2 = {11 % 2}")       # 1 (odd number: n % 2 != 0)

# Find even or odd number
num = 32 #int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# Clock arithmetic: what time is it 25 hours from 10?
current_hour = 10
hours_later = 25
new_hour = (current_hour + hours_later) % 24
print(f"  Clock: {current_hour}:00 + {hours_later}h = {new_hour}:00")

# Exponentiation
print(f"\n  --- Exponentiation ---")
print(f"  2 ** 0   = {2 ** 0}")      # 1 (anything to power 0)
print(f"  2 ** -1  = {2 ** -1}")     # 0.5 (negative = reciprocal)
print(f"  9 ** 0.5 = {9 ** 0.5}")    # 3.0 (square root!)
print(f"  2 ** 100 = {2 ** 100}")    # Python handles big integers


# =============================================================================
# OPERATOR OVERLOADING (+ and * with non-numeric types)
# =============================================================================

print(f"\n{'=' * 55}")
print("  OPERATOR OVERLOADING")
print("=" * 55)

# + with strings (concatenation)
greeting = "Hello" + " " + "World"
print(f"\n  'Hello' + ' ' + 'World' = '{greeting}'")

# * with strings (repetition)
line = "-" * 40
print(f"  '-' * 40 = '{line}'")

# + with lists (concatenation)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"  [1,2,3] + [4,5,6] = {combined}")

# * with lists (repetition)
zeros = [0] * 5
print(f"  [0] * 5 = {zeros}")


# =============================================================================
# AUGMENTED ASSIGNMENT OPERATORS
# =============================================================================
'''
Augmented assignment operators (often called compound assignment operators) are programming shortcuts that combine an arithmetic or bitwise operation with a variable assignment. 
Instead of writing a variable twice in a statement, you can perform the calculation and update the variable's value in a single step.

Long-form: x = x + 5
Augmented form: x += 5
'''

print(f"\n{'=' * 55}")
print("  AUGMENTED ASSIGNMENT OPERATORS")
print("=" * 55)

x = 10
print(f"\n  Starting with x = {x}")

x += 5
print(f"  x += 5   -> x = {x}")    # 15

x -= 3
print(f"  x -= 3   -> x = {x}")    # 12

x *= 2
print(f"  x *= 2   -> x = {x}")    # 24

x /= 4
print(f"  x /= 4   -> x = {x}")    # 6.0

x //= 2
print(f"  x //= 2  -> x = {x}")    # 3.0

x **= 3
print(f"  x **= 3  -> x = {x}")    # 27.0

x %= 10
print(f"  x %= 10  -> x = {x}")    # 7.0

# Works with strings too
message = "Hello"
message += " World"
print(f"\n  'Hello' += ' World' -> '{message}'")

# Works with lists too
my_list = [1, 2, 3]
my_list += [4, 5]
print(f"  [1,2,3] += [4,5]   -> {my_list}")

print(f"\n{'=' * 55}")
