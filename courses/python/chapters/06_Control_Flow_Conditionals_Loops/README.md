# Control Flow - Conditionals & Loops

## Overview

Control flow is the backbone of any programming language. It determines the order in which statements are executed in your program. Without control flow, programs would simply execute line by line from top to bottom with no ability to make decisions or repeat actions. Python provides elegant and readable control flow structures that make your code both powerful and easy to understand.

In this lesson, we'll cover two major categories of control flow: **conditionals** (if/elif/else, match-case) that allow your program to make decisions, and **loops** (for, while) that allow your program to repeat actions. We'll also explore loop control statements (break, continue, pass) and useful built-in functions like range(), enumerate(), and zip() that make loops more powerful.

By mastering control flow, you'll be able to write programs that respond to different inputs, process collections of data, implement game logic, automate repetitive tasks, and much more. This is where your programs start to become truly interactive and intelligent.

## Learning Objectives

- Write conditional statements using if, elif, and else
- Use the ternary operator for concise conditional expressions
- Implement structural pattern matching with match-case (Python 3.10+)
- Create for loops to iterate over sequences and ranges
- Use while loops for condition-based repetition
- Control loop execution with break, continue, and pass
- Understand and use the loop else clause
- Leverage enumerate() and zip() for cleaner loop code
- Build nested loops for multi-dimensional processing
- Create a Countdown Timer and Number Guessing Game

## Prerequisites

- Variables & Data Types
- Keywords & Identifiers
- Operators (especially comparison and logical operators)
- Strings & Methods (for working with string data in conditions)

## How to Run the Examples

```bash
cd courses/python/chapters/06_Control_Flow_Conditionals_Loops

python3 01_conditionals.py
python3 02_for_loops.py
python3 03_while_loops_and_control.py
python3 countdown_timer.py
python3 quiz_game.py
```

Each script is standalone and prints its output directly. The `countdown_timer.py` and `quiz_game.py` are interactive mini-projects.

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

### 5. for Loops

The `for` loop iterates over items in a sequence (list, string, tuple, range, etc.):

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"I like {fruit}")

# Iterating over a string
for char in "Python":
    print(char, end=" ")  # P y t h o n
print()

# Iterating over a dictionary
student = {"name": "Vikram", "age": 28, "city": "Hyderabad"}
for key in student:
    print(f"{key}: {student[key]}")

# Iterating over dictionary items (key-value pairs)
for key, value in student.items():
    print(f"{key}: {value}")

# Iterating over a tuple
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"x={x}, y={y}")

# for loop with else (else runs if loop completes without break)
for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop completed successfully!")
```

### 6. while Loops

The `while` loop continues executing as long as its condition is `True`:

```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# User input validation with while
while True:
    user_input = input("Enter a positive number: ")
    if user_input.isdigit() and int(user_input) > 0:
        number = int(user_input)
        break
    print("Invalid input. Try again.")
print(f"You entered: {number}")

# While with a flag variable
running = True
attempts = 0
while running:
    attempts += 1
    if attempts >= 5:
        print("Maximum attempts reached!")
        running = False
    else:
        print(f"Attempt {attempts}...")

# While loop counting down
countdown = 10
while countdown > 0:
    print(countdown, end=" ")
    countdown -= 1
print("Liftoff!")

# While with else
n = 5
while n > 0:
    print(n)
    n -= 1
else:
    print("While loop finished normally (no break)")
```

### 7. range() Function

The `range()` function generates a sequence of numbers and is commonly used with for loops:

```python
# range(stop) - 0 to stop-1
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# range(start, stop) - start to stop-1
for i in range(2, 8):
    print(i, end=" ")  # 2 3 4 5 6 7
print()

# range(start, stop, step) - with custom step
for i in range(0, 20, 3):
    print(i, end=" ")  # 0 3 6 9 12 15 18
print()

# Counting backwards
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1
print()

# Even numbers
for i in range(0, 21, 2):
    print(i, end=" ")  # 0 2 4 6 8 10 12 14 16 18 20
print()

# Using range for indexing (less Pythonic, but sometimes needed)
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# Converting range to list
numbers = list(range(1, 11))
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Memory efficiency - range doesn't store all values
# This uses almost no memory regardless of size:
huge_range = range(1_000_000_000)
print(999_999 in huge_range)  # True (fast membership testing)
print(len(huge_range))         # 1000000000
```

### 8. break Statement

`break` immediately terminates the innermost loop it's in:

```python
# Finding the first even number
numbers = [1, 3, 5, 8, 9, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
else:
    print("No even number found")

# Breaking out of a search loop
target = 42
data = [10, 25, 37, 42, 55, 63]
found = False
for index, value in enumerate(data):
    if value == target:
        found = True
        print(f"Found {target} at index {index}")
        break

if not found:
    print(f"{target} not found in data")

# Break in a while loop
import random
secret = random.randint(1, 10)
while True:
    guess = int(input("Guess (1-10): "))
    if guess == secret:
        print("Correct!")
        break
    print("Try again...")
```

### 9. continue Statement

`continue` skips the rest of the current iteration and moves to the next:

```python
# Skip odd numbers
for i in range(10):
    if i % 2 != 0:
        continue
    print(i, end=" ")  # 0 2 4 6 8
print()

# Skip empty strings
words = ["hello", "", "world", "", "python", ""]
for word in words:
    if not word:
        continue
    print(word.upper())

# Process only valid data
data = [12, -5, 0, 38, None, 72, "invalid", 45]
valid_sum = 0
for item in data:
    if not isinstance(item, (int, float)):
        continue
    if item <= 0:
        continue
    valid_sum += item
print(f"Sum of valid positive numbers: {valid_sum}")

# Skip specific lines when processing text
log_lines = [
    "INFO: Server started",
    "DEBUG: Connection established",
    "ERROR: File not found",
    "DEBUG: Query executed",
    "ERROR: Timeout exceeded",
]
print("Errors only:")
for line in log_lines:
    if not line.startswith("ERROR"):
        continue
    print(f"  {line}")
```

### 10. pass Statement

`pass` is a null operation - it does nothing. It's used as a placeholder:

```python
# Placeholder for future code
def calculate_tax(income):
    pass  # TODO: implement this function

# Empty class definition
class MyCustomError(Exception):
    pass

# Placeholder in conditional branches
age = 25
if age < 18:
    pass  # Will handle minors later
elif age < 65:
    print("Working age")
else:
    pass  # Will handle seniors later

# Ignoring specific exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    pass  # Silently ignore the error (use cautiously!)

# Empty loop body (useful in certain patterns)
# Wait for a condition (conceptual - don't actually do this)
# while not is_ready():
#     pass
```

### 11. Nested Loops

Loops inside loops create multi-dimensional iterations:

```python
# Multiplication table
print("Multiplication Table (1-5):")
print("-" * 30)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()  # New line after each row

# Pattern printing - right triangle
print("\nRight Triangle:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern printing - pyramid
print("\nPyramid:")
rows = 5
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "* " * i
    print(spaces + stars)

# Nested loop with break (only breaks inner loop)
print("\nFinding pairs that sum to 10:")
for i in range(1, 10):
    for j in range(i + 1, 10):
        if i + j == 10:
            print(f"  {i} + {j} = 10")
            break  # Only breaks the inner loop

# Matrix operations
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nMatrix:")
for row in matrix:
    for element in row:
        print(f"{element:3}", end="")
    print()

# Flattening a nested list
flat = []
for row in matrix:
    for element in row:
        flat.append(element)
print(f"\nFlattened: {flat}")
```

### 12. Loop else Clause

Python's unique feature - the `else` clause on loops runs when the loop completes normally (without `break`):

```python
# Searching with for-else
def find_prime_factor(n):
    """Find the smallest prime factor of n."""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"Smallest prime factor of {n} is {i}")
            break
    else:
        # This runs only if no break occurred (n is prime)
        print(f"{n} is a prime number!")

find_prime_factor(17)   # 17 is a prime number!
find_prime_factor(24)   # Smallest prime factor of 24 is 2
find_prime_factor(49)   # Smallest prime factor of 49 is 7

# Checking if all items meet a condition
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num % 2 != 0:
        print(f"Found odd number: {num}")
        break
else:
    print("All numbers are even!")

# while-else example
n = 10
while n > 0:
    n -= 1
    if n == -1:  # This never happens
        break
else:
    print(f"While loop completed normally, n = {n}")

# Practical: username availability check
taken_usernames = ["admin", "user1", "python_dev", "coder"]
new_username = "vikram_k"
for username in taken_usernames:
    if username == new_username:
        print(f"Username '{new_username}' is already taken!")
        break
else:
    print(f"Username '{new_username}' is available!")
```

### 13. enumerate() and zip() in Loops

These built-in functions make loops more Pythonic and readable:

```python
# enumerate() - get both index and value
fruits = ["apple", "banana", "cherry", "date"]

# Without enumerate (less Pythonic)
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (Pythonic!)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# enumerate with custom start index
for rank, fruit in enumerate(fruits, start=1):
    print(f"#{rank}: {fruit}")

# zip() - iterate over multiple sequences in parallel
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old, lives in {city}")

# zip stops at the shortest sequence
short = [1, 2]
long = [10, 20, 30, 40]
for a, b in zip(short, long):
    print(f"{a} -> {b}")  # Only prints 2 pairs

# zip_longest for unequal sequences
from itertools import zip_longest
for a, b in zip_longest(short, long, fillvalue=0):
    print(f"{a} -> {b}")  # Prints all 4 pairs

# Combining enumerate and zip
students = ["Alice", "Bob", "Charlie"]
grades = [92, 85, 78]
for i, (student, grade) in enumerate(zip(students, grades), 1):
    print(f"{i}. {student}: {grade}")

# Creating a dictionary from two lists using zip
keys = ["name", "age", "city"]
values = ["Vikram", 28, "Hyderabad"]
person = dict(zip(keys, values))
print(person)  # {'name': 'Vikram', 'age': 28, 'city': 'Hyderabad'}

# Unzipping (transpose)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')
```

### 14. Infinite Loops and When to Use Them

Infinite loops run forever until explicitly stopped. They're useful for certain patterns:

```python
# Menu-driven program (common pattern)
def show_menu():
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    return input("Choose an option: ")

# Main loop pattern
while True:
    choice = show_menu()
    
    if choice == '5':
        print("Goodbye!")
        break
    
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Try again.")
        continue
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    match choice:
        case '1':
            print(f"Result: {a + b}")
        case '2':
            print(f"Result: {a - b}")
        case '3':
            print(f"Result: {a * b}")
        case '4':
            if b != 0:
                print(f"Result: {a / b}")
            else:
                print("Error: Division by zero!")

# Event loop pattern (conceptual)
# while True:
#     event = get_next_event()
#     if event.type == QUIT:
#         break
#     process_event(event)

# Retry with backoff pattern
import time

def connect_to_server():
    """Simulate connection attempt."""
    import random
    return random.random() > 0.7  # 30% success rate

max_retries = 5
retry_count = 0
while True:
    retry_count += 1
    print(f"Connection attempt {retry_count}...")
    
    if connect_to_server():
        print("Connected successfully!")
        break
    
    if retry_count >= max_retries:
        print("Max retries exceeded. Giving up.")
        break
    
    wait_time = 2 ** retry_count  # Exponential backoff
    print(f"  Failed. Retrying in {wait_time}s...")
    time.sleep(wait_time)
```

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

### Example 2: Prime Number Checker and Generator

```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate all prime numbers up to limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Find primes up to 50
print("Primes up to 50:")
print(generate_primes(50))

# Find the nth prime
def nth_prime(n):
    """Find the nth prime number."""
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

print(f"\nThe 10th prime is: {nth_prime(10)}")
print(f"The 100th prime is: {nth_prime(100)}")
```

### Example 3: Pattern Printer

```python
def print_diamond(n):
    """Print a diamond pattern of given size."""
    # Upper half (including middle)
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        print(spaces + stars)
    
    # Lower half
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        stars = "* " * i
        print(spaces + stars)

print("Diamond (n=5):")
print_diamond(5)

def print_number_pattern(n):
    """Print a number pyramid pattern."""
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print numbers going up
        for j in range(1, i + 1):
            print(j, end="")
        # Print numbers going down
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

print("\nNumber Pattern (n=5):")
print_number_pattern(5)
```

### Example 4: Simple ATM Simulator

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

## Exercises

### Exercise 1: Countdown Timer (Beginner)

**Reference**: [Countdown Timer Short](https://youtube.com/shorts/Zr-3nw7g3kk)

**Task**: Create a countdown timer that:

1. Asks the user for the number of seconds to count down
2. Displays the countdown in MM:SS format
3. Prints "TIME'S UP!" when the countdown reaches zero
4. Plays a sound or prints a visual alert at the end
5. Asks if the user wants to set another timer

```python
import time

def countdown_timer():
    """
    A functional countdown timer.
    
    Features:
    - Accept time in seconds
    - Display in MM:SS format
    - Clear previous line for clean display (use \r)
    - Show visual alert when done
    """
    # TODO: Get time from user
    # TODO: Validate input (positive integer)
    # TODO: Loop counting down each second
    # TODO: Display in MM:SS format using divmod()
    # TODO: Use time.sleep(1) for each second
    # TODO: Print completion message
    # TODO: Ask to repeat
    
    # Hints:
    # - divmod(seconds, 60) gives (minutes, remaining_seconds)
    # - print(f"\r{mins:02d}:{secs:02d}", end="") overwrites the line
    # - time.sleep(1) pauses for 1 second
    pass

# Test
countdown_timer()
```

**Expected Output:**
```
Enter countdown time in seconds: 65

Starting countdown...
01:05
01:04
01:03
...
00:02
00:01
00:00

🔔 TIME'S UP! 🔔

Set another timer? (y/n): n
Goodbye!
```

### Exercise 2: Number Guessing Game (Intermediate)

**Task**: Build a number guessing game with the following features:

1. Computer picks a random number between 1 and 100
2. Player has limited attempts based on difficulty level
3. After each guess, provide "higher" or "lower" hints
4. Track the number of attempts and display a score
5. Keep a high score across multiple rounds
6. Implement difficulty levels (Easy: 15 guesses, Medium: 10, Hard: 5)

```python
import random

def number_guessing_game():
    """
    Number guessing game with difficulty levels and scoring.
    
    Features:
    - Multiple difficulty levels
    - Hint system (higher/lower)
    - Score tracking
    - High score persistence (within session)
    - Input validation
    - Play again option
    """
    high_scores = {"easy": None, "medium": None, "hard": None}
    
    print("=" * 50)
    print("       NUMBER GUESSING GAME")
    print("=" * 50)
    
    while True:
        # TODO: Show difficulty menu
        # TODO: Set max_attempts based on difficulty
        # TODO: Generate random number (1-100)
        # TODO: Game loop with guessing
        # TODO: Provide higher/lower hints
        # TODO: Track attempts and calculate score
        # TODO: Update high score if applicable
        # TODO: Ask to play again
        
        # Hints:
        # - Use random.randint(1, 100)
        # - Score formula: max_attempts - attempts_used + 1
        # - Validate input is a number between 1-100
        # - Use match-case for difficulty selection
        pass

# Run the game
number_guessing_game()
```

**Expected Output:**
```
==================================================
       NUMBER GUESSING GAME
==================================================

Select difficulty:
  1. Easy (15 attempts)
  2. Medium (10 attempts)
  3. Hard (5 attempts)
Choice: 2

I'm thinking of a number between 1 and 100...
You have 10 attempts.

Attempt 1/10 - Your guess: 50
📉 Too high! Try lower.

Attempt 2/10 - Your guess: 25
📈 Too low! Try higher.

Attempt 3/10 - Your guess: 37
📉 Too high! Try lower.

Attempt 4/10 - Your guess: 31
🎉 Correct! The number was 31!

Score: 7/10 | Attempts: 4
🏆 New high score for Medium difficulty!

Play again? (y/n): n
Thanks for playing!
```

### Exercise 3: Interactive Menu System - Mini-Project (Advanced)

**Task**: Build a comprehensive interactive grade management system that combines all control flow concepts:

1. A main menu loop with options
2. Add students with their grades
3. Calculate and display statistics (average, highest, lowest)
4. Search for students by name
5. Grade distribution visualization (text-based bar chart)
6. Filter students by grade range
7. Implement proper input validation throughout

```python
def grade_management_system():
    """
    Interactive student grade management system.
    
    Features:
    - Add/remove students
    - Record grades for multiple subjects
    - Calculate statistics (mean, median, highest, lowest)
    - Search students by name (partial match)
    - Display grade distribution as text bar chart
    - Filter by grade range
    - Export summary
    
    Uses: if/elif/else, for loops, while loops, break, continue,
          enumerate, nested loops, match-case
    """
    students = {}  # {"name": {"math": 85, "science": 90, ...}}
    
    while True:
        print("\n" + "=" * 50)
        print("    STUDENT GRADE MANAGEMENT SYSTEM")
        print("=" * 50)
        print("  1. Add Student")
        print("  2. Add/Update Grade")
        print("  3. View All Students")
        print("  4. Search Student")
        print("  5. Class Statistics")
        print("  6. Grade Distribution Chart")
        print("  7. Filter by Grade Range")
        print("  8. Remove Student")
        print("  9. Exit")
        print("-" * 50)
        
        choice = input("  Select option: ")
        
        # TODO: Implement each menu option
        # TODO: Use match-case for option handling
        # TODO: Implement proper input validation
        # TODO: Use nested loops for multi-subject grades
        # TODO: Use enumerate for numbered displays
        # TODO: Use break/continue appropriately
        
        match choice:
            case "1":
                # Add student - validate name not empty, not duplicate
                pass
            case "2":
                # Add grade - validate student exists, grade 0-100
                pass
            case "3":
                # Display all students with grades in formatted table
                pass
            case "4":
                # Search by partial name match (case-insensitive)
                pass
            case "5":
                # Calculate and display statistics
                pass
            case "6":
                # Text-based bar chart of grade distribution
                # A (90-100): ████████ 3
                # B (80-89):  ██████████████ 5
                # etc.
                pass
            case "7":
                # Filter students by min/max grade
                pass
            case "8":
                # Remove student with confirmation
                pass
            case "9":
                print("\n  Goodbye! Keep studying! 📚")
                break
            case _:
                print("  Invalid option. Please try again.")

# Run the system
grade_management_system()
```

**Expected Output (Grade Distribution):**
```
GRADE DISTRIBUTION
──────────────────────────────────────
  A (90-100): ████████░░░░░░░░ 3 students
  B (80-89):  ████████████░░░░ 5 students
  C (70-79):  ████████████████ 7 students
  D (60-69):  ████░░░░░░░░░░░░ 2 students
  F (0-59):   ██░░░░░░░░░░░░░░ 1 student
──────────────────────────────────────
  Total: 18 students | Class Average: 76.4
```

## Resources & References

- **Python Official Docs - Control Flow**: https://docs.python.org/3/tutorial/controlflow.html
- **Python Official Docs - match statement**: https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
- **Real Python - Conditional Statements**: https://realpython.com/python-conditional-statements/
- **Real Python - Python for Loop**: https://realpython.com/python-for-loop/
- **Real Python - Python while Loop**: https://realpython.com/python-while-loop/
- **Programiz - Python if...else**: https://www.programiz.com/python-programming/if-elif-else
- **Programiz - Python for Loop**: https://www.programiz.com/python-programming/for-loop
- **W3Schools - Python Conditions**: https://www.w3schools.com/python/python_conditions.asp
- **W3Schools - Python For Loops**: https://www.w3schools.com/python/python_for_loops.asp
- **GeeksForGeeks - Python Control Flow**: https://www.geeksforgeeks.org/python-programming-language/#Control%20Flow

### Video References
- **Countdown Timer Mini-Project**: https://youtube.com/shorts/Zr-3nw7g3kk
- **PEP 634 - Structural Pattern Matching**: https://peps.python.org/pep-0634/

---
