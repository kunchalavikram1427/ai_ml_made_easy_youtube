# Strings & Methods

## Overview

Strings are one of the most fundamental and frequently used data types in Python. A string is a sequence of characters enclosed in quotes, and Python provides an incredibly rich set of built-in methods to manipulate them. Whether you're processing user input, reading files, building web applications, or working with APIs, you'll constantly be working with strings.

In this lesson, we'll explore everything from basic string creation to advanced formatting techniques. You'll learn how to slice strings, search within them, transform their case, split and join them, and format them for output. Understanding strings deeply will make you a more effective Python programmer, as string manipulation is at the heart of most real-world applications.

By the end of this lesson, you'll be comfortable creating, manipulating, and formatting strings in multiple ways. You'll also build a Password Generator as a mini-project that combines many of the concepts covered here.

## Learning Objectives

- Create strings using single, double, and triple quotes
- Access individual characters and substrings using indexing and slicing
- Understand string immutability and its implications
- Use escape characters and raw strings effectively
- Apply common string methods for text processing
- Format strings using f-strings, .format(), and % operator
- Compare strings
- Build a functional Password Generator

## Prerequisites

- Variables & Data Types (understanding of variable assignment and basic types)
- Keywords & Identifiers (Python reserved words)
- Operators (arithmetic, comparison, and logical operators)

## How to Run the Examples

```bash
cd courses/python/chapters/05_Strings_And_Methods

python3 01_string_creation_and_indexing.py
python3 02_string_methods.py
python3 03_string_formatting.py
python3 04_string_operations.py
python3 05_password_generator.py
python3 06_email_validator.py
```

Each script is standalone and prints its output directly. The `05_password_generator.py` and `06_email_validator.py` are interactive mini-projects.

---

## Detailed Explanation

### 1. String Creation

Python offers multiple ways to create strings, each with its own use case:

```python
# Single quotes - most common for short strings
name = 'Vikram'

# Double quotes - useful when string contains single quotes
message = "It's a beautiful day"

# Triple quotes (single) - for multi-line strings
poem = '''Roses are red,
Violets are blue,
Python is awesome,
And so are you!'''

# Triple quotes (double) - also for multi-line strings and docstrings
description = """This is a multi-line
string that preserves
all line breaks and spacing."""

# Empty string
empty = ''
also_empty = ""
```

**When to use which:**
- Use single quotes for simple strings: `'hello'`
- Use double quotes when the string contains apostrophes: `"don't stop"`
- Use triple quotes for multi-line strings or docstrings

### 2. String Indexing and Slicing

Strings in Python are sequences, meaning each character has a position (index). Python uses **zero-based indexing**, so the first character is at index 0.

```python
text = "Python"

# Positive indexing (left to right, starts at 0)
print(text[0])   # 'P'
print(text[1])   # 'y'
print(text[5])   # 'n'

# Negative indexing (right to left, starts at -1)
print(text[-1])  # 'n' (last character)
print(text[-2])  # 'o' (second to last)
print(text[-6])  # 'P' (first character)

# IndexError if out of range
# print(text[10])  # IndexError: string index out of range
```

**Slicing** allows you to extract substrings using the syntax `string[start:stop:step]`:

```python
text = "Hello, World!"

# Basic slicing [start:stop] - stop is exclusive
print(text[0:5])    # 'Hello'
print(text[7:12])   # 'World'

# Omitting start or stop
print(text[:5])     # 'Hello' (from beginning)
print(text[7:])     # 'World!' (to end)
print(text[:])      # 'Hello, World!' (full copy)

# Using step
print(text[::2])    # 'Hlo ol!' (every 2nd character)
print(text[::3])    # 'Hl r!'  (every 3rd character)

# Reversing a string
print(text[::-1])   # '!dlroW ,olleH'

# Negative indices in slicing
print(text[-6:-1])  # 'World'
print(text[-6:])    # 'World!'
```

### 3. String Immutability

Strings in Python are **immutable** - once created, they cannot be changed. Any operation that appears to modify a string actually creates a new string.

```python
name = "Python"

# This will raise an error:
# name[0] = 'J'  # TypeError: 'str' object does not support item assignment

# Instead, create a new string:
new_name = 'J' + name[1:]
print(new_name)  # 'Jython'

# Even methods return NEW strings:
greeting = "hello"
upper_greeting = greeting.upper()
print(greeting)        # 'hello' (unchanged!)
print(upper_greeting)  # 'HELLO' (new string)

# Reassignment is fine (points variable to new string object):
greeting = greeting.upper()  # Now greeting points to 'HELLO'
```

**Why immutability matters:**
- Strings can be used as dictionary keys (they're hashable)
- Strings are safe to share between different parts of your program
- Python can optimize memory by reusing identical string objects (string interning)

### 4. Escape Characters

Escape characters allow you to include special characters in strings that would otherwise be impossible or confusing to type:

```python
# Newline
print("Line 1\nLine 2")
# Output:
# Line 1
# Line 2

# Tab
print("Name:\tVikram")
# Output: Name:    Vikram

# Backslash
print("Path: C:\\Users\\Vikram")
# Output: Path: C:\Users\Vikram

# Single quote inside single-quoted string
print('It\'s a test')
# Output: It's a test

# Double quote inside double-quoted string
print("He said \"Hello\"")
# Output: He said "Hello"

# Carriage return (overwrites from beginning of line)
print("Hello\rWorld")
# Output: World

# Null character
print("Hello\0World")
# Output: HelloWorld (null is invisible)

# Unicode characters
print("❤")   # Heart symbol
print("Hello")  # Hello

# Octal and Hex
print("\110\145\154\154\157")  # Hello (octal)
print("\x48\x65\x6C\x6C\x6F")  # Hello (hex)
```

### 5. Raw Strings

Raw strings treat backslashes as literal characters - no escape processing occurs:

```python
# Regular string - \n is interpreted as newline
print("Hello\nWorld")
# Output:
# Hello
# World

# Raw string - \n is treated as literal backslash + n
print(r"Hello\nWorld")
# Output: Hello\nWorld

# Very useful for Windows file paths
path = r"C:\Users\Vikram\Documents\new_file.txt"
print(path)  # C:\Users\Vikram\Documents\new_file.txt

# Useful for regex patterns
import re
pattern = r"\d+\.\d+"  # Matches decimal numbers
result = re.findall(pattern, "Price is 19.99 and tax is 2.50")
print(result)  # ['19.99', '2.50']

# Note: raw string cannot end with an odd number of backslashes
# path = r"C:\Users\"  # SyntaxError!
# Workaround:
path = r"C:\Users" + "\\"
```

### 6. String Methods

Python provides dozens of built-in string methods. Here are the most important ones:

#### Case Conversion Methods

```python
text = "Hello, World!"

print(text.upper())       # 'HELLO, WORLD!'
print(text.lower())       # 'hello, world!'
print(text.title())       # 'Hello, World!'
print(text.capitalize())  # 'Hello, world!'
print(text.swapcase())    # 'hELLO, wORLD!'
```

#### Stripping / Trimming Methods

```python
text = "   Hello, World!   "

print(text.strip())       # 'Hello, World!' (both sides)
print(text.lstrip())      # 'Hello, World!   ' (left only)
print(text.rstrip())      # '   Hello, World!' (right only)

# Strip specific characters
url = "###www.example.com###"
print(url.strip('#'))     # 'www.example.com'

csv_line = ",,value1,,value2,,"
print(csv_line.strip(','))  # 'value1,,value2'
```

#### Split and Join Methods

```python
# split() - splits string into a list
sentence = "Python is an amazing language"
words = sentence.split()
print(words)  # ['Python', 'is', 'an', 'amazing', 'language']

# Split by specific delimiter
csv_data = "name,age,city"
fields = csv_data.split(',')
print(fields)  # ['name', 'age', 'city']

# Split with maxsplit parameter
text = "one:two:three:four"
print(text.split(':', 2))  # ['one', 'two', 'three:four']

# splitlines() - splits by line breaks
multi = "Line 1\nLine 2\nLine 3"
print(multi.splitlines())  # ['Line 1', 'Line 2', 'Line 3']

# join() - joins a list into a string
words = ['Python', 'is', 'awesome']
print(' '.join(words))     # 'Python is awesome'
print('-'.join(words))     # 'Python-is-awesome'
print(', '.join(words))    # 'Python, is, awesome'

# join with empty string (concatenation)
letters = ['H', 'e', 'l', 'l', 'o']
print(''.join(letters))    # 'Hello'
```

#### Search and Replace Methods

```python
text = "Hello, World! Hello, Python!"

# find() - returns index of first occurrence (-1 if not found)
print(text.find('World'))     # 7
print(text.find('Java'))      # -1
print(text.find('Hello', 5))  # 14 (search from index 5)

# rfind() - search from right
print(text.rfind('Hello'))    # 14

# index() - like find() but raises ValueError if not found
print(text.index('World'))    # 7
# print(text.index('Java'))  # ValueError!

# count() - counts non-overlapping occurrences
print(text.count('Hello'))    # 2
print(text.count('l'))        # 4

# replace() - replaces occurrences
print(text.replace('Hello', 'Hi'))      # 'Hi, World! Hi, Python!'
print(text.replace('Hello', 'Hi', 1))   # 'Hi, World! Hello, Python!' (max 1 replacement)

# startswith() and endswith()
filename = "document.pdf"
print(filename.startswith('doc'))   # True
print(filename.endswith('.pdf'))    # True
print(filename.endswith(('.pdf', '.doc', '.txt')))  # True (tuple of suffixes)
```

#### Validation Methods

```python
# isalpha() - all characters are alphabetic
print("Hello".isalpha())       # True
print("Hello123".isalpha())    # False
print("Hello World".isalpha()) # False (space is not alphabetic)

# isdigit() - all characters are digits
print("12345".isdigit())       # True
print("123.45".isdigit())      # False (dot is not a digit)

# isalnum() - all characters are alphanumeric
print("Hello123".isalnum())    # True
print("Hello 123".isalnum())   # False (space)

# isspace() - all characters are whitespace
print("   ".isspace())         # True
print(" \t\n".isspace())       # True

# isupper() / islower()
print("HELLO".isupper())       # True
print("hello".islower())       # True

# isnumeric() - broader than isdigit (includes fractions, etc.)
print("123".isnumeric())       # True
print("½".isnumeric())    # True (fraction 1/2)

# isdecimal() - strict decimal digits only
print("123".isdecimal())       # True
```

#### Padding and Alignment Methods

```python
text = "Python"

# center(), ljust(), rjust()
print(text.center(20))        # '       Python       '
print(text.center(20, '-'))   # '-------Python-------'
print(text.ljust(20, '.'))    # 'Python..............'
print(text.rjust(20, '.'))    # '..............Python'

# zfill() - pad with zeros
num = "42"
print(num.zfill(5))           # '00042'
print("-42".zfill(5))         # '-0042'
```

### 7. f-strings (Formatted String Literals)

Introduced in Python 3.6, f-strings are the most readable and efficient way to format strings:

```python
name = "Vikram"
age = 28
height = 5.9

# Basic f-string
print(f"My name is {name}")
print(f"I am {age} years old")

# Expressions inside f-strings
print(f"Next year I'll be {age + 1}")
print(f"Name in uppercase: {name.upper()}")

# Formatting numbers
price = 49.99
print(f"Price: ${price:.2f}")          # Price: $49.99
print(f"Price: ${price:>10.2f}")       # Price: $     49.99

pi = 3.14159265359
print(f"Pi: {pi:.4f}")                 # Pi: 3.1416

# Formatting with thousands separator
population = 1400000000
print(f"Population: {population:,}")    # Population: 1,400,000,000
print(f"Population: {population:_}")    # Population: 1_400_000_000

# Percentage
ratio = 0.756
print(f"Success rate: {ratio:.1%}")     # Success rate: 75.6%

# Padding and alignment in f-strings
for item in ['Apple', 'Banana', 'Cherry']:
    print(f"{item:<10} | {'fruit':>10}")

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"Today: {now:%Y-%m-%d}")
print(f"Time: {now:%H:%M:%S}")

# Debugging with = (Python 3.8+)
x = 42
y = 3.14
print(f"{x = }")            # x = 42
print(f"{x + y = :.2f}")   # x + y = 45.14

# Multi-line f-strings
name = "Vikram"
role = "Developer"
message = (
    f"Name: {name}\n"
    f"Role: {role}\n"
    f"Status: Active"
)
print(message)
```

### 8. String Formatting: Comparison of Methods

Python has three main formatting approaches. Here's a comparison:

```python
name = "Vikram"
age = 28
gpa = 3.85

# Method 1: % operator (old-style, C-like)
print("Name: %s, Age: %d, GPA: %.2f" % (name, age, gpa))

# Method 2: .format() method (Python 2.6+)
print("Name: {}, Age: {}, GPA: {:.2f}".format(name, age, gpa))
print("Name: {0}, Age: {1}, GPA: {2:.2f}".format(name, age, gpa))
print("Name: {n}, Age: {a}, GPA: {g:.2f}".format(n=name, a=age, g=gpa))

# Method 3: f-strings (Python 3.6+) - RECOMMENDED
print(f"Name: {name}, Age: {age}, GPA: {gpa:.2f}")
```

**Recommendation**: Use f-strings for most cases. They're the most readable, fastest, and most Pythonic. Use `.format()` when you need to reuse a template. The `%` operator is mostly seen in legacy code.

### 9. String Concatenation and Repetition

```python
# Concatenation with +
first = "Hello"
second = "World"
result = first + ", " + second + "!"
print(result)  # 'Hello, World!'

# Repetition with *
border = "=" * 40
print(border)  # '========================================'

laugh = "Ha" * 5
print(laugh)   # 'HaHaHaHaHa'

# Implicit concatenation (adjacent string literals)
message = "Hello, " "World!"  # No + needed for literals
print(message)  # 'Hello, World!'

# Building strings efficiently with join (preferred over + in loops)
# BAD (creates many intermediate strings):
result = ""
for i in range(1000):
    result += str(i)  # Slow for large iterations

# GOOD (efficient):
result = ''.join(str(i) for i in range(1000))
```

### 10. String Comparison

```python
# Equality
print("hello" == "hello")   # True
print("hello" == "Hello")   # False (case-sensitive)

# Case-insensitive comparison
print("hello".lower() == "Hello".lower())  # True

# Membership testing with 'in'
print("Py" in "Python")     # True
print("java" in "Python")   # False
```

### 11. Multi-line Strings

```python
# Using triple quotes (preserves formatting)
sql_query = """
SELECT name, age, city
FROM users
WHERE age > 25
ORDER BY name ASC;
"""
print(sql_query)

# Using parentheses for implicit line continuation
long_message = (
    "This is a very long message that "
    "spans multiple lines in the source code "
    "but appears as a single line when printed."
)
print(long_message)

# Using backslash for line continuation
long_calc = "This is also a way to " \
            "continue a string across " \
            "multiple lines."

# textwrap.dedent for cleaner multi-line strings
import textwrap
def get_help():
    help_text = textwrap.dedent("""\
        Usage: program [options]
        
        Options:
            -h  Show help
            -v  Verbose mode
            -o  Output file
    """)
    return help_text

print(get_help())
```

## Code Examples

### Example 1: Text Analyzer

```python
def analyze_text(text):
    """Analyze a text string and return statistics."""
    print(f"{'=' * 50}")
    print(f"TEXT ANALYSIS REPORT")
    print(f"{'=' * 50}")
    print(f"\nOriginal text: '{text}'")
    print(f"\nCharacter count: {len(text)}")
    print(f"Word count: {len(text.split())}")
    print(f"Sentence count: {text.count('.') + text.count('!') + text.count('?')}")
    print(f"\nUppercase letters: {sum(1 for c in text if c.isupper())}")
    print(f"Lowercase letters: {sum(1 for c in text if c.islower())}")
    print(f"Digits: {sum(1 for c in text if c.isdigit())}")
    print(f"Spaces: {text.count(' ')}")
    print(f"\nStarts with uppercase: {text[0].isupper() if text else False}")
    print(f"Ends with punctuation: {text[-1] in '.!?' if text else False}")
    print(f"{'=' * 50}")

# Test it
analyze_text("Hello World! Python 3.12 is amazing. Let's code!")
```

### Example 2: String Formatter Utility

```python
def format_name(first, last, style="full"):
    """Format a name in various styles."""
    first = first.strip().capitalize()
    last = last.strip().capitalize()
    
    styles = {
        "full": f"{first} {last}",
        "last_first": f"{last}, {first}",
        "initials": f"{first[0]}.{last[0]}.",
        "formal": f"Mr./Ms. {last}",
        "username": f"{first.lower()}.{last.lower()}",
        "email": f"{first.lower()}.{last.lower()}@company.com"
    }
    
    return styles.get(style, styles["full"])

# Demo
print(format_name("vikram", "kunchala", "full"))
print(format_name("vikram", "kunchala", "last_first"))
print(format_name("vikram", "kunchala", "initials"))
print(format_name("vikram", "kunchala", "username"))
print(format_name("vikram", "kunchala", "email"))
```

## Exercises

### Exercise 1: String Manipulation Toolkit (Beginner)

**Task**: Create a program that takes a user input string and performs the following operations, displaying each result:

1. Print the string in all uppercase
2. Print the string in all lowercase
3. Print the string reversed
4. Count the number of vowels (a, e, i, o, u - both cases)
5. Replace all spaces with underscores
6. Print the first and last character
7. Check if the string is a palindrome (reads the same forwards and backwards)

```python
# Starter code
def string_toolkit(text):
    """Perform various string operations and display results."""
    print(f"\nOriginal string: '{text}'")
    print(f"{'-' * 40}")
    
    # TODO: Implement all 7 operations
    # Hint: Use string methods and slicing
    pass

# Test with:
string_toolkit("Hello World")
string_toolkit("racecar")
string_toolkit("Python Programming")
```

**Expected Output (for "Hello World"):**
```
Original string: 'Hello World'
----------------------------------------
Uppercase: HELLO WORLD
Lowercase: hello world
Reversed: dlroW olleH
Vowel count: 3
With underscores: Hello_World
First char: H, Last char: d
Is palindrome: False
```

### Exercise 2: Text Formatter (Intermediate)

**Task**: Create a function that formats a paragraph of text according to specified rules:

1. Accept a paragraph of text and a maximum line width
2. Word-wrap the text so no line exceeds the max width
3. Center each line within the max width
4. Add a decorative border around the text
5. Support left-align, right-align, and center-align options

```python
# Starter code
def format_paragraph(text, width=50, align="center", border_char="*"):
    """
    Format text into a bordered, aligned paragraph.
    
    Args:
        text: The input text string
        width: Maximum width of each line (default 50)
        align: 'left', 'right', or 'center' (default 'center')
        border_char: Character for the border (default '*')
    """
    # TODO: Implement word wrapping
    # TODO: Apply alignment
    # TODO: Add border
    # Hint: Use split(), join(), ljust(), rjust(), center()
    pass

# Test with:
sample = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability."
format_paragraph(sample, width=40, align="center")
format_paragraph(sample, width=40, align="left")
```

**Expected Output (centered, width=40):**
```
******************************************
*  Python is an interpreted, high-level  *
*  general-purpose programming language  *
*  Created by Guido van Rossum and first *
*  released in 1991, Python's design     *
*  philosophy emphasizes code            *
*  readability.                          *
******************************************
```

### Exercise 3: Email Validator - Mini-Project (Intermediate)

**Task**: Build an email login system that validates email addresses using string methods:

1. Accept email input from the user
2. Validate the email format (check for `@`, valid username, valid domain)
3. Check if the domain is in the supported list (gmail.com, outlook.com, yahoo.com, hotmail.com, icloud.com)
4. Accept a password (hidden using `getpass`)
5. Display login success/failure with appropriate messages

```python
import getpass

SUPPORTED_DOMAINS = [
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "hotmail.com",
    "icloud.com"
]

def validate_email(email):
    """Basic email validation using string methods."""
    email = email.strip()

    # Check for exactly one @
    if email.count('@') != 1:
        return False, "Must contain @ symbol"

    # Split into username and domain parts
    username, domain = email.split('@')

    # Check username part
    if not username:
        return False, "Username (before @) cannot be empty"
    if username.startswith('.') or username.endswith('.'):
        return False, "Username cannot start or end with a dot"

    # Check domain part
    if not domain:
        return False, "Domain part (after @) cannot be empty"
    if '.' not in domain:
        return False, "Domain must contain at least one dot"
    if domain.startswith('.') or domain.endswith('.'):
        return False, "Domain cannot start or end with a dot"

    # Check domain extension
    extension = domain.split('.')[-1]
    if len(extension) < 2:
        return False, "Domain extension must be at least 2 characters"
    if not extension.isalpha():
        return False, "Domain extension must contain only letters"

    # Check if domain is supported
    if domain.lower() not in SUPPORTED_DOMAINS:
        supported_list = ", ".join(SUPPORTED_DOMAINS)
        return False, f"Domain '{domain}' is not supported. Supported domains: {supported_list}"

    return True, "Valid email format"


def login():
    """Simple login that validates email and accepts any password."""
    print("=" * 40)
    print("       EMAIL LOGIN SYSTEM")
    print("=" * 40)

    email = input("\nEnter your email: ")
    is_valid, message = validate_email(email)

    if not is_valid:
        print(f"\n  Login FAILED: {message}")
        return

    password = getpass.getpass("Enter your password: ")

    if not password:
        print("\n  Login FAILED: Password cannot be empty")
        return

    username = email.split('@')[0]
    print(f"\n  Login SUCCESSFUL!")
    print(f"  Welcome, {username}")


if __name__ == "__main__":
    login()
```

**Expected Output:**
```
========================================
       EMAIL LOGIN SYSTEM
========================================

Enter your email: vikram@gmail.com
Enter your password:

  Login SUCCESSFUL!
  Welcome, vikram
```

**String methods used**: `strip()`, `count()`, `split()`, `startswith()`, `endswith()`, `isalpha()`, `lower()`, `join()`

---

### Exercise 4: Password Generator - Mini-Project (Advanced)

**Reference**: [Password Generator Short](https://youtube.com/shorts/BN6IBv6scrY)

**Task**: Build a complete password generator that:

1. Asks the user for desired password length
2. Asks which character types to include (uppercase, lowercase, digits, special)
3. Generates a random password meeting the criteria
4. Checks the password strength (weak, medium, strong, very strong)
5. Displays the password with a strength indicator
6. Optionally generates multiple passwords for the user to choose from

```python
import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, 
                     use_digits=True, use_special=True):
    """
    Generate a random password based on specified criteria.
    
    Args:
        length: Length of password (minimum 4)
        use_upper: Include uppercase letters
        use_lower: Include lowercase letters
        use_digits: Include digits
        use_special: Include special characters
    
    Returns:
        Generated password string
    """
    # TODO: Build character pool based on options
    # TODO: Ensure at least one character from each selected type
    # TODO: Fill remaining length with random choices
    # TODO: Shuffle the result
    # Hint: Use string.ascii_uppercase, string.ascii_lowercase, 
    #       string.digits, string.punctuation
    pass

def check_strength(password):
    """
    Check password strength and return rating.
    
    Criteria:
    - Length >= 8: +1 point
    - Length >= 12: +1 point
    - Has uppercase: +1 point
    - Has lowercase: +1 point
    - Has digits: +1 point
    - Has special chars: +1 point
    - No repeated characters (3+): +1 point
    
    Rating: 0-2 Weak, 3-4 Medium, 5-6 Strong, 7 Very Strong
    """
    # TODO: Implement strength checking
    pass

def password_generator_app():
    """Main application loop for the password generator."""
    print("=" * 50)
    print("    SECURE PASSWORD GENERATOR")
    print("=" * 50)
    
    # TODO: Get user preferences
    # TODO: Generate and display password(s)
    # TODO: Show strength rating
    # TODO: Option to generate more
    pass

# Run the app
password_generator_app()
```

**Expected Output:**
```
==================================================
    SECURE PASSWORD GENERATOR
==================================================
Enter password length (8-50): 16
Include uppercase? (y/n): y
Include lowercase? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): y

Generated Password: Kx#9mP$2nL@8wQz!
Strength: [████████████] VERY STRONG

Generate another? (y/n): y

Generated Password: hR4$pN7@kM2&
Strength: [██████████░░] STRONG

Generate another? (y/n): n
Goodbye! Stay secure!
```

**Bonus Challenge**: Also check out the [Coolshapes video](https://www.youtube.com/shorts/CihzL31JD9U) for inspiration on creating visual patterns using string repetition and formatting!

## Resources & References

- **Python Official Docs - String Methods**: https://docs.python.org/3/library/stdtypes.html#string-methods
- **Python Official Docs - Format String Syntax**: https://docs.python.org/3/library/string.html#formatstrings
- **Python Official Docs - f-strings (PEP 498)**: https://docs.python.org/3/reference/lexical_analysis.html#f-strings

---


