"""
Video 01: Introduction to Python - Examples
=============================================
This is your first Python file! Run it with:
    python3 examples.py

Or run individual sections in the Python REPL (interactive mode):
    python3
    >>> print("Hello, World!")
"""

# ============================================================
# SECTION 1: Hello, World!
# ============================================================
# Every programming journey begins with "Hello, World!"
# In Python, it's just ONE line:

print("Hello, World!")
print()  # Print a blank line for spacing

# ============================================================
# SECTION 2: Basic Arithmetic in Python
# ============================================================
# Python can be used as a powerful calculator right out of the box

print("=" * 50)
print("BASIC ARITHMETIC")
print("=" * 50)

print(f"Addition:        2 + 3 = {2 + 3}")
print(f"Subtraction:     10 - 4 = {10 - 4}")
print(f"Multiplication:  5 * 6 = {5 * 6}")
print(f"Division:        15 / 4 = {15 / 4}")        # True division (float)
print(f"Floor Division:  15 // 4 = {15 // 4}")      # Integer division
print(f"Modulus:         15 % 4 = {15 % 4}")        # Remainder
print(f"Exponent:        2 ** 10 = {2 ** 10}")      # 2 to the power of 10
print(f"Big numbers:     2 ** 100 = {2 ** 100}")    # Python handles huge numbers!
print()

# ============================================================
# SECTION 3: Python Version & System Info
# ============================================================
# Let's check what version of Python we're running

print("=" * 50)
print("SYSTEM INFORMATION")
print("=" * 50)

import sys
print(f"Python Version: {sys.version}")

import platform
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")
print()

# ============================================================
# SECTION 4: The Zen of Python
# ============================================================
# Uncomment the line below to see Python's guiding philosophy
# (It prints a lot of text, so we keep it commented by default)

# import this

# Instead, here are the first few principles:
print("=" * 50)
print("THE ZEN OF PYTHON (selected)")
print("=" * 50)
print("Beautiful is better than ugly.")
print("Explicit is better than implicit.")
print("Simple is better than complex.")
print("Readability counts.")
print("(Run 'import this' in the REPL to see all 19 principles!)")
print()

# ============================================================
# SECTION 5: A Taste of Python's Readability & Power
# ============================================================
# These examples show WHY Python is loved for its elegance

print("=" * 50)
print("PYTHON'S POWER & READABILITY")
print("=" * 50)

# List comprehension: squares of even numbers from 1 to 20
even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(f"Squares of even numbers (1-20): {even_squares}")

# Swap two variables — no temp variable needed!
a, b = 1, 2
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")

# String multiplication
print("Python! " * 3)

# Multi-line strings with triple quotes
poem = """
    Roses are red,
    Violets are blue,
    Python is awesome,
    And so are you!
"""
print(poem)

# Check if something is in a list (reads like English!)
fruits = ["apple", "banana", "cherry", "mango"]
print(f"Is 'mango' in our fruits? {'mango' in fruits}")
print(f"Is 'grape' in our fruits? {'grape' in fruits}")

print()
print("=" * 50)
print("Congratulations! You just ran your first Python script!")
print("See you in Video 02: Setting Up Your Dev Environment!")
print("=" * 50)
