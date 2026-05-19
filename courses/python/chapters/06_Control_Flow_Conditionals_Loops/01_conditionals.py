"""
Conditionals — if, elif, else, ternary, match-case
=====================================================
Run: python3 01_conditionals.py

Covers:
- if, elif, else statements
- Nested conditionals
- Ternary operator (conditional expression)
- match-case (Python 3.10+ structural pattern matching)
- Truthy and falsy values
"""


# =============================================================================
# IF, ELIF, ELSE
# =============================================================================

print("=" * 55)
print("  IF / ELIF / ELSE")
print("=" * 55)

# Basic if
age = 18
print(f"\n  age = {age}")
if age >= 18:
    print(f"  -> You are an adult.")

# if-else: two-way decision
temperature = 35
print(f"\n  temperature = {temperature}")
if temperature > 30:
    print(f"  -> It's hot outside!")
else:
    print(f"  -> The weather is pleasant.")

# if-elif-else: multi-way decision
score = 85
print(f"\n  score = {score}")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"  -> Grade: {grade}")

# Multiple conditions with logical operators
print(f"\n  --- Multiple Conditions ---")
age = 25
has_license = True
print(f"  age = {age}, has_license = {has_license}")
if age >= 18 and has_license:
    print(f"  -> You can drive!")

day = "Saturday"
print(f"\n  day = '{day}'")
if day == "Saturday" or day == "Sunday":
    print(f"  -> It's the weekend!")


# =============================================================================
# NESTED CONDITIONALS
# =============================================================================

print(f"\n{'=' * 55}")
print("  NESTED CONDITIONALS")
print("=" * 55)

age = 25
has_id = True
is_vip = False

print(f"\n  age={age}, has_id={has_id}, is_vip={is_vip}")

if age >= 18:
    if has_id:
        if is_vip:
            print(f"  -> VIP entry! Welcome!")
        else:
            print(f"  -> Regular entry. Welcome!")
    else:
        print(f"  -> Entry denied: No ID")
else:
    print(f"  -> Entry denied: Under 18")

# Better: flatten with 'and' when possible
print(f"\n  Tip: Flatten nested ifs when possible:")
if age >= 18 and has_id and is_vip:
    print(f"  -> VIP entry!")
elif age >= 18 and has_id:
    print(f"  -> Regular entry!")


# =============================================================================
# TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# =============================================================================

print(f"\n{'=' * 55}")
print("  TERNARY OPERATOR")
print("=" * 55)

# Syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(f"\n  age = {age}")
print(f"  status = 'adult' if age >= 18 else 'minor'")
print(f"  -> status = '{status}'")

# Practical examples
x = 10
abs_x = x if x >= 0 else -x
print(f"\n  x = {x}")
print(f"  abs_x = x if x >= 0 else -x -> {abs_x}")

num = 7
parity = "even" if num % 2 == 0 else "odd"
print(f"\n  num = {num}")
print(f"  parity = '{parity}'")

# In f-strings
score = 85
print(f"\n  Result: {'PASS' if score >= 60 else 'FAIL'}")


# =============================================================================
# MATCH-CASE (Python 3.10+)
# =============================================================================

print(f"\n{'=' * 55}")
print("  MATCH-CASE (Python 3.10+)")
print("=" * 55)

# Basic pattern matching
command = "start"
print(f"\n  command = '{command}'")

match command:
    case "start":
        print(f"  -> Starting the application...")
    case "stop":
        print(f"  -> Stopping the application...")
    case "restart":
        print(f"  -> Restarting...")
    case _:
        print(f"  -> Unknown command!")

# With values
http_status = 404
print(f"\n  http_status = {http_status}")

match http_status:
    case 200:
        print(f"  -> OK")
    case 301:
        print(f"  -> Moved Permanently")
    case 404:
        print(f"  -> Not Found")
    case 500:
        print(f"  -> Internal Server Error")
    case _:
        print(f"  -> Unknown status code")

# OR patterns with |
day = "Saturday"
print(f"\n  day = '{day}'")

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"  -> Weekday")
    case "Saturday" | "Sunday":
        print(f"  -> Weekend!")


# =============================================================================
# TRUTHY AND FALSY VALUES
# =============================================================================

print(f"\n{'=' * 55}")
print("  TRUTHY AND FALSY VALUES")
print("=" * 55)

print(f"\n  Falsy values (evaluate to False):")
falsy_values = [False, None, 0, 0.0, "", [], {}, set()]
for val in falsy_values:
    print(f"    {str(val):<10} -> bool = {bool(val)}")

print(f"\n  Truthy (everything else evaluates to True):")
truthy_values = [True, 1, -1, 3.14, "hello", [1, 2], {"a": 1}]
for val in truthy_values:
    print(f"    {str(val):<12} -> bool = {bool(val)}")

# Practical use
print(f"\n  --- Practical ---")
name = ""
if name:
    print(f"  Hello, {name}!")
else:
    print(f"  name is empty -> treated as False")

items = [1, 2, 3]
if items:
    print(f"  items has {len(items)} elements -> treated as True")

print(f"\n{'=' * 55}")
