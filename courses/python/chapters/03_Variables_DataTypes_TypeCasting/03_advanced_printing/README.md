# Advanced Printing in Python

## Overview

The `print()` function is something you'll use in every single Python program, but most beginners only scratch the surface of what it can do. Beyond simple `print("Hello")`, Python offers powerful string formatting methods that control how your output looks — from aligning columns in tables to formatting currency values to building progress bars in the terminal.

In this lesson, we'll master the `print()` function's parameters, explore all four string formatting methods (%-formatting, `.format()`, f-strings, and Template strings), and learn special techniques like colored terminal output and tabular formatting.

## Learning Objectives

By the end of this lesson, you will be able to:

- Use all `print()` parameters: `sep`, `end`, `file`, `flush`
- Format strings using %-formatting (printf-style)
- Format strings using the `.format()` method
- Format strings using f-strings (the preferred modern approach)
- Use Template strings for security-sensitive formatting
- Choose the right formatting method for each situation
- Create colored terminal output with ANSI codes
- Build progress bars and formatted tables

## Prerequisites

- Comments in Python (annotating code)
- Variables and Typecasting (data types, basic variable usage)

## How to Run the Examples

```bash
cd courses/python/chapters/03_Variables_DataTypes_TypeCasting/03_advanced_printing

python3 01_print_function_params.py   # sep, end, file, flush
python3 02_percent_formatting.py      # %-formatting (printf-style)
python3 03_dot_format_method.py       # .format() method
python3 04_fstrings.py                # f-strings (preferred)
python3 05_template_strings.py        # Template strings + comparison
python3 06_special_print_techniques.py # Colors, tables, progress bars
```

Each script is self-contained — run them in any order.

---

## Detailed Explanation

### 1. The `print()` Function Deep Dive

#### Signature

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

#### Parameters

| Parameter | Default      | Purpose                                    |
|-----------|--------------|--------------------------------------------|
| `*objects`| —            | Values to print (any number)               |
| `sep`     | `' '`        | String inserted between objects             |
| `end`     | `'\n'`       | String appended after the last object       |
| `file`    | `sys.stdout` | File-like object to write to                |
| `flush`   | `False`      | Force stream flush after write              |

#### Examples

```python
# Multiple arguments with separator
print("2024", "01", "15", sep="-")          # 2024-01-15
print("192", "168", "1", "1", sep=".")      # 192.168.1.1

# Custom end (no newline)
print("Loading", end="...")
print("Done!")                               # Loading...Done!

# Print to file
with open("log.txt", "a") as f:
    print("Error occurred", file=f)

# Print to stderr
import sys
print("Critical error!", file=sys.stderr)

# Force flush (important for progress indicators)
print("Processing", end="", flush=True)

# Unpack a list
items = ["a", "b", "c"]
print(*items, sep=", ")                     # a, b, c
```

---

### 2. %-Formatting (printf-style)

The oldest string formatting method in Python. Uses `%` operator with format specifiers. You'll still see this in legacy code and the `logging` module.

#### Format Specifiers

| Specifier | Type                    | Example                   |
|-----------|-------------------------|---------------------------|
| `%s`      | String                  | `"Hi %s" % "Vikram"`     |
| `%d`      | Integer (decimal)       | `"Age: %d" % 25`         |
| `%f`      | Float                   | `"Pi: %f" % 3.14`        |
| `%e`      | Scientific notation     | `"%e" % 0.001`           |
| `%x`      | Hex (lowercase)         | `"%x" % 255` -> `ff`     |
| `%X`      | Hex (uppercase)         | `"%X" % 255` -> `FF`     |
| `%o`      | Octal                   | `"%o" % 8` -> `10`       |
| `%%`      | Literal `%` sign        | `"100%%"` -> `100%`      |

#### Width, Padding, and Precision

```python
# Zero-padding
print("%05d" % 42)              # 00042

# Left-align with width
print("%-10s|" % "left")       # left      |

# Right-align (default)
print("%10s|" % "right")       #      right|

# Float precision
print("%.2f" % 3.14159)        # 3.14
print("%8.2f" % 3.14159)       #     3.14
```

#### Real-World Example

```python
firmware_version = "v2.3.1"
url = "https://firmware.company.com/api/v2"
print("[Info]: Firmware version for: %s to be fetched from: %s" % (firmware_version, url))
```

---

### 3. `.format()` Method

Introduced in Python 2.6 / 3.0. More powerful and readable than %-formatting.

#### Positional and Named Arguments

```python
# Implicit positional
"Hello, {}!".format("Vikram")

# Explicit positional (reusable)
"{0} likes {1}. {0} also likes {2}.".format("Vikram", "Python", "AI")

# Named arguments
"{name} is {age}".format(name="Vikram", age=25)
```

#### Alignment and Fill

| Syntax     | Meaning        | Example Output      |
|------------|----------------|---------------------|
| `{:<10}`   | Left-align     | `text______`        |
| `{:>10}`   | Right-align    | `______text`        |
| `{:^10}`   | Center         | `___text___`        |
| `{:*^10}`  | Center + fill  | `***text***`        |

#### Number Formatting

```python
"{:.2f}".format(3.14159)         # 3.14
"{:,}".format(1000000)           # 1,000,000
"{:+.2f}".format(3.14)           # +3.14
"{:.1%}".format(0.856)           # 85.6%
"{:b}".format(42)                # 101010
"{:#x}".format(255)              # 0xff
```

#### Nested Format Specs

```python
width = 15
precision = 3
"{:{w}.{p}f}".format(3.14159, w=width, p=precision)
```

---

### 4. f-Strings (Preferred Method)

Introduced in Python 3.6. **The recommended method for most use cases.**

#### Why f-strings?

- Most readable syntax
- Fastest execution (compiled at parse time)
- Support arbitrary expressions
- Support format specifiers

#### Basic Usage

```python
name = "Vikram"
age = 25
print(f"Hello, {name}! You are {age} years old.")
```

#### Expressions

```python
f"Sum: {2 + 3}"                          # Sum: 5
f"{'adult' if age >= 18 else 'minor'}"   # adult
f"{name.upper()}"                        # VIKRAM
f"Length: {len(name)}"                   # Length: 6
```

#### Number Formatting

```python
price = 49.99
count = 1500000
num = 42

f"${price:.2f}"          # $49.99
f"{count:,}"             # 1,500,000
f"{count:_}"             # 1_500_000
f"{num:08b}"             # 00101010
f"{num:#x}"              # 0x2a
f"{0.856:.1%}"           # 85.6%
f"{0.00123:.2e}"         # 1.23e-03
```

#### Debugging (Python 3.8+)

```python
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")     # x=10, y=20, x+y=30
```

#### Date Formatting

```python
from datetime import datetime
now = datetime.now()
f"{now:%Y-%m-%d %H:%M:%S}"       # 2024-01-15 14:30:00
f"{now:%B %d, %Y}"               # January 15, 2024
```

#### repr() in f-strings

```python
text = "Hello\tWorld"
f"{text}"       # Hello	World    (str)
f"{text!r}"     # 'Hello\tWorld'  (repr)
f"{text!a}"     # 'Hello\tWorld'  (ascii)
```

#### Multiline f-strings

```python
message = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"City: {city}"
)
```

---

### 5. Template Strings

From the `string` module. **Use when format strings come from untrusted sources.**

```python
from string import Template

# Basic
t = Template("Hello, $name!")
t.substitute(name="Vikram")          # Hello, Vikram!

# Safe substitution (missing keys don't raise errors)
t = Template("$greeting, $name! Role: $role")
t.safe_substitute(greeting="Hi", name="Vikram")
# Output: Hi, Vikram! Role: $role
```

#### Security Advantage

```python
# f-strings and .format() can access attributes/methods - DANGEROUS with user input
# Template strings ONLY do simple substitution - SAFE
user_template = "$name has $count items"  # From user
t = Template(user_template)
t.substitute(name="Vikram", count=5)
```

---

### 6. Special Techniques

#### ANSI Color Codes

```python
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f"{GREEN}[PASS]{RESET} Test passed")
print(f"{RED}[FAIL]{RESET} Test failed")
print(f"{BOLD}{YELLOW}[WARN]{RESET} Deprecation notice")
```

#### Progress Bar

```python
import time

total = 50
for i in range(total + 1):
    percent = (i / total) * 100
    bar = "█" * i + "░" * (total - i)
    print(f"\r[{bar}] {percent:.0f}%", end="", flush=True)
    time.sleep(0.05)
print()  # Final newline
```

#### Tabular Output

```python
header = f"{'Name':<15}{'Age':>5}{'City':<15}{'GPA':>6}"
print(header)
print("-" * len(header))
for name, age, city, gpa in data:
    print(f"{name:<15}{age:>5}{city:<15}{gpa:>6.2f}")
```

#### Pretty Printing

```python
from pprint import pprint
pprint(complex_dict, width=60, depth=2)
```

---

### 7. Comparison Table

| Feature              | %-format         | .format()          | f-string           | Template        |
|----------------------|------------------|--------------------|--------------------|-----------------|
| Python version       | All              | 2.6+ / 3.0+       | 3.6+               | All             |
| Readability          | Low              | Medium             | **High**           | Medium          |
| Performance          | Medium           | Medium             | **Fast**           | Slow            |
| Expressions          | No               | Limited            | **Yes**            | No              |
| Positional reuse     | No               | Yes (`{0}...{0}`)  | Variable reuse     | No              |
| Security (user input)| Risky            | Risky              | Risky              | **Safe**        |
| Dynamic format spec  | Limited          | Yes                | Yes                | No              |

---

### 8. Best Practices

1. **Use f-strings as your default** — they're the fastest and most readable
2. **Use .format() when the format string is a variable** (loaded from config, etc.)
3. **Use %-formatting only in legacy code** or with the `logging` module
4. **Use Template for user-supplied format strings** (security!)
5. **Always add `flush=True`** for real-time progress output
6. **Use `sep` and `end` parameters** instead of manual string concatenation
7. **Print errors to stderr**: `print("error", file=sys.stderr)`
8. **Use `pprint` for debugging** complex data structures

---

### 9. Common Mistakes & Gotchas

#### Forgetting the tuple with %-formatting

```python
# WRONG - TypeError if name is a tuple
print("Hello %s" % name)

# SAFE - always use a tuple
print("Hello %s" % (name,))
```

#### Mixing up `%d` and `%s` for numbers

```python
# %d truncates floats!
print("%d" % 3.99)    # 3 (not 4!)
print("%s" % 3.99)    # 3.99
```

#### Curly braces in .format() and f-strings

```python
# To print literal { } you must double them
print(f"Set notation: {{1, 2, 3}}")    # Set notation: {1, 2, 3}
```

#### f-string with backslashes

```python
# WRONG - Can't use backslashes inside f-string expressions
# print(f"{'hello\nworld'}")  # SyntaxError!

# CORRECT - Use a variable
newline = '\n'
print(f"Line 1{newline}Line 2")

# In Python 3.12+, backslashes are allowed in f-string expressions
```

#### Forgetting flush for progress output

```python
# WRONG - output may be buffered
print("Processing...", end="")

# CORRECT - forces immediate display
print("Processing...", end="", flush=True)
```

#### print() returns None

```python
# WRONG
result = print("hello")     # result is None!

# print() is for side effects, not return values
```

---

## Code Examples

### Example: All 4 Methods Side by Side

```python
name = "Vikram"
age = 25
gpa = 3.856

# Same output, 4 different methods:
print("%-formatting:  Name: %s, Age: %d, GPA: %.2f" % (name, age, gpa))
print(".format():     Name: {}, Age: {}, GPA: {:.2f}".format(name, age, gpa))
print(f"f-string:      Name: {name}, Age: {age}, GPA: {gpa:.2f}")

from string import Template
t = Template("Template:      Name: $name, Age: $age, GPA: $gpa")
print(t.substitute(name=name, age=age, gpa=f"{gpa:.2f}"))
```

---

## Exercises

### Exercise 1: Format a Receipt (Beginner)

**Objective:** Use f-strings to format a shopping receipt with aligned columns.

**Instructions:**
Create a script that prints a receipt with items left-aligned (20 chars), quantity right-aligned (5 chars), and price right-aligned (8 chars with 2 decimal places). Add a total at the bottom.

### Exercise 2: Build a Progress Bar (Intermediate)

**Objective:** Create a reusable progress bar function using `\r`, `end=""`, and `flush=True`.

### Exercise 3: Colored Logger (Advanced)

**Objective:** Build a `log(level, message)` function that prints timestamped, color-coded log messages to the terminal.

---

## Resources & References

- **Python Official Docs — Format String Syntax:** https://docs.python.org/3/library/string.html#format-string-syntax
- **Python Official Docs — f-strings (PEP 498):** https://peps.python.org/pep-0498/
- **Real Python — Python String Formatting Best Practices:** https://realpython.com/python-string-formatting/
- **Real Python — f-Strings:** https://realpython.com/python-f-strings/
- **ANSI Escape Codes Reference:** https://en.wikipedia.org/wiki/ANSI_escape_code

---

## Quick Reference Card

```python
# %-formatting
"Name: %s, Age: %d, GPA: %.2f" % (name, age, gpa)

# .format()
"Name: {}, Age: {}, GPA: {:.2f}".format(name, age, gpa)

# f-string (USE THIS)
f"Name: {name}, Age: {age}, GPA: {gpa:.2f}"

# Template
Template("Name: $name, Age: $age").substitute(name=name, age=age)
```

---

## Key Takeaways

1. **f-strings are the default choice** — fastest, most readable, support expressions
2. **`print()` has powerful parameters** — `sep`, `end`, `file`, `flush` eliminate manual string work
3. **Use `flush=True`** for real-time output (progress bars, status updates)
4. **Template strings for security** — only option safe for user-provided format strings
5. **%-formatting lives on** in `logging` module and legacy code
6. **`{:.2f}` for money, `{:,}` for thousands** — know the common format specs

---
