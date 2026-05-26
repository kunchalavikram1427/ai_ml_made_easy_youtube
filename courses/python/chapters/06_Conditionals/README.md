# Conditionals

## Overview

Conditionals are the decision-making backbone of any program. They allow your code to choose different paths based on whether a condition is `True` or `False`. Without conditionals, programs would execute every line in sequence with no ability to respond to different inputs or situations.

Python provides clean, readable conditional structures — from the classic `if/elif/else` chain to the concise ternary operator and the powerful `match-case` pattern matching introduced in Python 3.10. By the end of this lesson, you'll be able to write programs that make intelligent decisions based on user input, data state, or any other condition.

## Learning Objectives

- Write conditional statements using if, elif, and else
- Understand how Python evaluates conditions top-to-bottom
- Use nested conditionals and know when to flatten them
- Use the ternary operator for concise conditional expressions
- Implement structural pattern matching with match-case (Python 3.10+)
- Understand truthy and falsy values in Python
- Combine conditions with logical operators (and, or, not)

## Prerequisites

- Variables & Data Types
- Keywords & Identifiers
- Operators (especially comparison and logical operators)
- Strings & Methods (for working with string data in conditions)

## How to Run the Examples

```bash
cd courses/python/chapters/06_Conditionals

python3 01_conditionals.py
python3 quiz_game.py
python3 countdown_timer.py
```

Each script is standalone and prints its output directly. The `quiz_game.py` and `countdown_timer.py` are interactive mini-projects.

---

## Detailed Explanation

### 1. if, elif, else Statements

The `if` statement is the most basic form of decision-making in Python. It evaluates a condition and executes a block of code only if the condition is `True`.

```python
# Basic if statement
age = 18
if age >= 18:
    print("You are an adult.")

# if-else: two-way decision
temperature = 35
if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant.")

# if-elif-else: multi-way decision
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is: {grade}")

# Multiple conditions with logical operators
age = 25
has_license = True
has_insurance = True

if age >= 18 and has_license and has_insurance:
    print("You can drive!")
elif age >= 18 and has_license:
    print("You need insurance first.")
elif age >= 18:
    print("You need a license first.")
else:
    print("You're too young to drive.")
```

**Important Rules:**
- Python uses **indentation** (4 spaces) to define code blocks, not braces `{}`
- The colon `:` at the end of the condition line is required
- `elif` can appear multiple times; `else` can appear at most once
- Conditions are evaluated top-to-bottom; the first `True` branch executes

### 2. Nested Conditionals

You can place if statements inside other if statements for more complex logic:

```python
# Nested conditionals
age = 25
employed = True
credit_score = 750

if age >= 18:
    print("Age requirement met.")
    if employed:
        print("Employment requirement met.")
        if credit_score >= 700:
            print("Congratulations! Loan approved.")
        else:
            print("Sorry, credit score too low.")
    else:
        print("You must be employed to apply.")
else:
    print("You must be at least 18 to apply.")

# Flattened version (often cleaner)
if age < 18:
    print("You must be at least 18 to apply.")
elif not employed:
    print("You must be employed to apply.")
elif credit_score < 700:
    print("Sorry, credit score too low.")
else:
    print("Congratulations! Loan approved.")
```

**Tip**: Avoid deeply nested conditionals when possible. Use early returns (in functions) or flatten with elif chains for better readability.

### 3. Ternary Operator (Conditional Expression)

Python's ternary operator provides a concise way to write simple if-else statements in a single line:

```python
# Syntax: value_if_true if condition else value_if_false

# Basic ternary
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # 'adult'

# Using in print statements
score = 85
print(f"Result: {'Pass' if score >= 60 else 'Fail'}")

# Assigning values
x = 10
y = 20
maximum = x if x > y else y
print(f"Maximum: {maximum}")  # 20

# Nested ternary (use sparingly - can reduce readability)
score = 75
grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'
print(f"Grade: {grade}")  # 'C'

# In list comprehensions
numbers = [1, -2, 3, -4, 5]
abs_values = [x if x >= 0 else -x for x in numbers]
print(abs_values)  # [1, 2, 3, 4, 5]
```

### 4. match-case (Python 3.10+ Structural Pattern Matching)

The `match-case` statement provides powerful pattern matching, similar to switch statements in other languages but far more capable:

```python
# Basic match-case (like switch)
def get_day_type(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Invalid day"

print(get_day_type("Monday"))   # 'Weekday'
print(get_day_type("Sunday"))   # 'Weekend'

# Match with value binding
def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"On X-axis at x={x}"
        case (0, y):
            return f"On Y-axis at y={y}"
        case (x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Not a valid point"

print(describe_point((0, 0)))    # 'Origin'
print(describe_point((5, 0)))    # 'On X-axis at x=5'
print(describe_point((3, 7)))    # 'Point at (3, 7)'

# Match with guards (if conditions)
def classify_number(n):
    match n:
        case x if x < 0:
            return "Negative"
        case 0:
            return "Zero"
        case x if x % 2 == 0:
            return "Positive even"
        case x:
            return "Positive odd"

print(classify_number(-5))   # 'Negative'
print(classify_number(0))    # 'Zero'
print(classify_number(4))    # 'Positive even'
print(classify_number(7))    # 'Positive odd'

# Match with dictionaries/mappings
def process_command(command):
    match command:
        case {"action": "move", "direction": direction}:
            return f"Moving {direction}"
        case {"action": "attack", "target": target}:
            return f"Attacking {target}"
        case {"action": "heal", "amount": amount}:
            return f"Healing for {amount} HP"
        case _:
            return "Unknown command"

print(process_command({"action": "move", "direction": "north"}))
print(process_command({"action": "attack", "target": "dragon"}))

# HTTP status codes example
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 301:
            return "Moved Permanently"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case code if 200 <= code < 300:
            return f"Success ({code})"
        case code if 400 <= code < 500:
            return f"Client Error ({code})"
        case code if 500 <= code < 600:
            return f"Server Error ({code})"
        case _:
            return f"Unknown status ({code})"
```

### 5. Truthy and Falsy Values

In Python, every value has a boolean interpretation. Understanding which values are "truthy" (evaluate to `True`) and "falsy" (evaluate to `False`) is essential for writing clean conditionals:

```python
# Falsy values (evaluate to False in boolean context)
falsy_values = [False, None, 0, 0.0, "", [], {}, set()]
for val in falsy_values:
    print(f"  {str(val):<10} -> bool = {bool(val)}")

# Truthy (everything else evaluates to True)
truthy_values = [True, 1, -1, 3.14, "hello", [1, 2], {"a": 1}]
for val in truthy_values:
    print(f"  {str(val):<12} -> bool = {bool(val)}")

# Practical use — checking for empty/None values
name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("Name is empty!")

items = [1, 2, 3]
if items:
    print(f"List has {len(items)} elements")

# Common pattern: default values
username = input("Enter name: ") or "Guest"
print(f"Welcome, {username}!")
```

**Key Rule:** Empty collections, zero, `None`, empty strings, and `False` are falsy. Everything else is truthy.

---

## Code Examples

### Example 1: FizzBuzz (Classic Interview Question)

```python
def fizzbuzz(n):
    """
    Print numbers from 1 to n with the following rules:
    - Divisible by 3: print "Fizz"
    - Divisible by 5: print "Buzz"
    - Divisible by both 3 and 5: print "FizzBuzz"
    - Otherwise: print the number
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()

fizzbuzz(30)
```

### Example 2: Simple ATM Simulator

```python
def atm_simulator():
    """Simulate a basic ATM with PIN verification and transactions."""
    correct_pin = "1234"
    balance = 5000.00
    max_attempts = 3
    
    print("=" * 40)
    print("      Welcome to Python Bank ATM")
    print("=" * 40)
    
    # PIN verification with limited attempts
    attempts = 0
    authenticated = False
    
    while attempts < max_attempts:
        pin = input(f"\nEnter your PIN ({max_attempts - attempts} attempts left): ")
        if pin == correct_pin:
            authenticated = True
            print("\nPIN accepted! Welcome, Customer.")
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print("Incorrect PIN. Try again.")
    
    if not authenticated:
        print("\nToo many incorrect attempts. Card blocked.")
        return
    
    # Main transaction loop
    while True:
        print(f"\n{'─' * 40}")
        print(f"  Current Balance: ${balance:,.2f}")
        print(f"{'─' * 40}")
        print("  1. Check Balance")
        print("  2. Deposit")
        print("  3. Withdraw")
        print("  4. Exit")
        
        choice = input("\n  Select option: ")
        
        match choice:
            case "1":
                print(f"\n  Your balance is: ${balance:,.2f}")
            case "2":
                amount = input("  Enter deposit amount: $")
                if amount.replace('.', '', 1).isdigit() and float(amount) > 0:
                    balance += float(amount)
                    print(f"  Deposited ${float(amount):,.2f}")
                else:
                    print("  Invalid amount.")
            case "3":
                amount = input("  Enter withdrawal amount: $")
                if amount.replace('.', '', 1).isdigit() and float(amount) > 0:
                    if float(amount) <= balance:
                        balance -= float(amount)
                        print(f"  Withdrawn ${float(amount):,.2f}")
                    else:
                        print("  Insufficient funds!")
                else:
                    print("  Invalid amount.")
            case "4":
                print("\n  Thank you for banking with us. Goodbye!")
                break
            case _:
                print("  Invalid option. Please try again.")

# Run the ATM (uncomment to execute)
# atm_simulator()
```

---

## Exercises

### Exercise 1: Grade Classifier (Beginner)

**Task**: Create a program that:

1. Asks the user for their percentage score (0-100)
2. Validates the input is a valid number in range
3. Assigns a letter grade using if/elif/else
4. Provides a personalized message based on the grade
5. Uses match-case to suggest next steps based on the grade

```python
def grade_classifier():
    """
    Grade classification system.
    
    Features:
    - Input validation
    - Letter grade assignment (A, B, C, D, F)
    - Personalized feedback using match-case
    - Pass/fail determination using ternary
    """
    # TODO: Get score from user
    # TODO: Validate input (0-100)
    # TODO: Assign letter grade with if/elif/else
    # TODO: Use match-case to give feedback per grade
    # TODO: Use ternary for pass/fail status
    
    # Hints:
    # - Use .isdigit() or try/except for validation
    # - A: 90+, B: 80+, C: 70+, D: 60+, F: below 60
    # - match grade: case 'A': ... case 'B': ...
    pass

# Test
grade_classifier()
```

**Expected Output:**
```
Enter your score (0-100): 85

Score: 85%
Grade: B
Status: Pass
Feedback: Great work! You're above average. Push for that A next time!
```

### Exercise 2: Python Quiz Game (Intermediate)

**Reference**: See `quiz_game.py` in this directory.

**Task**: Build an interactive quiz game that:

1. Presents multiple-choice questions
2. Uses if/elif/else to check answers
3. Tracks score with conditional logic
4. Provides different end messages based on performance (match-case)
5. Validates all user input

### Exercise 3: Menu-Driven Calculator (Advanced)

**Task**: Build an interactive calculator that:

1. Uses a main menu with match-case for operation selection
2. Handles edge cases with conditionals (division by zero, invalid input)
3. Supports chaining operations (use previous result)
4. Provides different precision modes
5. Implements proper input validation throughout

```python
def calculator():
    """
    Interactive calculator using match-case and conditionals.
    
    Features:
    - Basic operations (+, -, *, /, //, %, **)
    - Input validation with helpful error messages
    - Result chaining (use previous answer)
    - Precision modes (integer, 2 decimal, full)
    - Operation history
    
    Uses: match-case, if/elif/else, ternary, nested conditionals
    """
    # TODO: Implement menu loop
    # TODO: Use match-case for operation selection
    # TODO: Validate inputs with conditionals
    # TODO: Handle edge cases (division by zero, overflow)
    # TODO: Implement result chaining
    pass

# Run the calculator
calculator()
```

---

## Resources & References

- **Python Official Docs - Control Flow**: https://docs.python.org/3/tutorial/controlflow.html
- **Python Official Docs - match statement**: https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
- **PEP 634 - Structural Pattern Matching**: https://peps.python.org/pep-0634/

---
