"""
Advanced Printing in Python - Examples
=======================================
Run: python3 examples.py

Covers:
  - print() function parameters (sep, end, file, flush)
  - %-formatting (printf-style / old style)
  - .format() method
  - f-strings (preferred, Python 3.6+)
  - Template strings
  - Special print techniques (colors, progress, tables)
"""

import sys
import time
from string import Template
from datetime import datetime
from pprint import pprint

# =============================================================================
# SECTION 1: BASIC print() FUNCTION
# =============================================================================
print("=" * 70)
print("SECTION 1: BASIC print() FUNCTION")
print("=" * 70)

# --- Multiple arguments (comma-separated) ---
name = "Vikram"
age = 25
city = "Hyderabad"
print("Name:", name, "Age:", age, "City:", city)

# --- sep parameter: separator between arguments ---
print("2024", "01", "15", sep="-")          # 2024-01-15
print("usr", "local", "bin", sep="/")        # usr/local/bin
print("A", "B", "C", "D", sep=" -> ")       # A -> B -> C -> D
print("192", "168", "1", "1", sep=".")       # 192.168.1.1

# --- end parameter: what to print at the end ---
print("Loading", end="...")
print("Done!")  # Appears on same line: Loading...Done!

print("Item 1", end=", ")
print("Item 2", end=", ")
print("Item 3")  # Item 1, Item 2, Item 3

# --- file parameter: print to a file ---
with open("/tmp/print_demo_log.txt", "w") as log_file:
    print("This goes to the log file", file=log_file)
    print("Timestamp:", datetime.now(), file=log_file)
print("(Written to /tmp/print_demo_log.txt)")

# --- flush parameter: force immediate output ---
print("Processing", end="", flush=True)
for i in range(3):
    print(".", end="", flush=True)
print(" Complete!")

# --- Printing to stderr ---
print("This is an error message!", file=sys.stderr)

# --- Unpacking a list with print ---
fruits = ["apple", "banana", "cherry", "date"]
print("Unpacked:", *fruits)
print("Joined:", *fruits, sep=", ")


# =============================================================================
# SECTION 2: %-FORMATTING (printf-style)
# =============================================================================
print("\n" + "=" * 70)
print("SECTION 2: %-FORMATTING (printf-style)")
print("=" * 70)

# --- Basic format specifiers ---
name = "Vikram"
age = 25
height = 5.9
print("String: %s" % name)
print("Integer: %d" % age)
print("Float: %f" % height)
print("Float (2 decimal): %.2f" % height)

# --- Multiple values (tuple) ---
print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))

# --- Real-world example ---
firmware_version = "v2.3.1"
url = "https://firmware.company.com/api/v2"
print("[Info]: Firmware version for: %s to be fetched from: %s" % (firmware_version, url))

# --- Hex and Octal ---
num = 255
print("Decimal: %d, Hex: %x, HEX: %X, Octal: %o" % (num, num, num, num))

# --- Padding and alignment ---
print("Zero-padded: %05d" % 42)
print("Left-aligned: %-10s|" % "left")
print("Right-aligned: %10s|" % "right")

# --- Width and precision combined ---
print("\n--- Formatted Price List ---")
for item, price in [("Coffee", 4.5), ("Sandwich", 8.99), ("Cake", 12.0)]:
    print("%-12s $%6.2f" % (item, price))


# =============================================================================
# SECTION 3: .format() METHOD
# =============================================================================
print("\n" + "=" * 70)
print("SECTION 3: .format() METHOD")
print("=" * 70)

# --- Basic positional ---
print("Hello, {}!".format(name))
print("{} is {} years old.".format(name, age))

# --- Explicit positional index ---
print("{0} likes {1}. {0} also likes {2}.".format("Vikram", "Python", "AI"))

# --- Named arguments ---
print("{name} lives in {city}".format(name="Vikram", city="Hyderabad"))

# --- Alignment ---
print("{:<20}|".format("Left aligned"))
print("{:>20}|".format("Right aligned"))
print("{:^20}|".format("Centered"))
print("{:*^20}|".format("Centered"))

# --- Number formatting ---
pi = 3.14159265
big_number = 1000000
print("Pi: {:.2f}".format(pi))
print("Big: {:,}".format(big_number))
print("Signed: {:+.2f}".format(pi))
print("Percentage: {:.1%}".format(0.856))

# --- Binary, Hex, Octal ---
print("Binary: {:b}".format(42))
print("Hex: {:x}".format(255))
print("With prefix: {:#b}, {:#x}, {:#o}".format(42, 255, 8))


# =============================================================================
# SECTION 4: f-STRINGS (Python 3.6+ / PREFERRED)
# =============================================================================
print("\n" + "=" * 70)
print("SECTION 4: f-STRINGS (PREFERRED METHOD)")
print("=" * 70)

# --- Basic f-string ---
name = "Vikram"
age = 25
print(f"Hello, {name}!")
print(f"{name} is {age} years old.")

# --- Expressions inside f-strings ---
print(f"Sum: {2 + 3}")
print(f"Even check: {age % 2 == 0}")
print(f"Ternary: {'adult' if age >= 18 else 'minor'}")

# --- Method calls ---
msg = "hello world"
print(f"Upper: {msg.upper()}")
print(f"Title: {msg.title()}")
print(f"Length: {len(msg)}")

# --- Number formatting ---
price = 49.99
count = 1500000
pi = 3.14159265
print(f"Price: ${price:.2f}")
print(f"Count: {count:,}")
print(f"Count: {count:_}")
print(f"Pi (3 decimals): {pi:.3f}")
print(f"Percentage: {0.856:.1%}")
print(f"Scientific: {0.00123:.2e}")

# --- Binary, Hex formatting ---
num = 42
print(f"Binary: {num:b}")
print(f"Binary (8-bit): {num:08b}")
print(f"Hex: {num:x}")
print(f"Hex (uppercase): {num:X}")

# --- Alignment in f-strings ---
print("\n--- Formatted Price List (f-strings) ---")
for item, price in [("Coffee", 4.5), ("Sandwich", 8.99), ("Cake", 12.0)]:
    print(f"{item:<12} ${price:>6.2f}")

# --- f-string debugging (Python 3.8+) ---
x = 10
y = 20
print(f"\n{x=}, {y=}, {x+y=}")

# --- Date formatting ---
now = datetime.now()
print(f"Date: {now:%Y-%m-%d}")
print(f"Time: {now:%H:%M:%S}")
print(f"Readable: {now:%B %d, %Y}")

# --- repr vs str in f-strings ---
text = "Hello\tWorld"
print(f"str: {text}")
print(f"repr: {text!r}")


# =============================================================================
# SECTION 5: TEMPLATE STRINGS
# =============================================================================
print("\n" + "=" * 70)
print("SECTION 5: TEMPLATE STRINGS (string.Template)")
print("=" * 70)

# --- Basic template ---
t = Template("Hello, $name! You are $age years old.")
result = t.substitute(name="Vikram", age=25)
print(result)

# --- Safe substitution (no KeyError on missing keys) ---
t = Template("$greeting, $name! Your role is $role.")
result = t.safe_substitute(greeting="Hi", name="Vikram")
print(result)  # $role remains as-is

# --- Security advantage ---
user_format = "$name has $count items"
t = Template(user_format)
print(t.substitute(name="Vikram", count=5))


# =============================================================================
# SECTION 6: COMPARISON - ALL 4 METHODS
# =============================================================================
print("\n" + "=" * 70)
print("SECTION 6: ALL 4 METHODS SIDE BY SIDE")
print("=" * 70)

name = "Vikram"
age = 25
gpa = 3.856

print("--- Same output, 4 methods ---")
print("%%-formatting: Name: %s, Age: %d, GPA: %.2f" % (name, age, gpa))
print(".format():     Name: {}, Age: {}, GPA: {:.2f}".format(name, age, gpa))
print(f"f-string:      Name: {name}, Age: {age}, GPA: {gpa:.2f}")
t = Template("Template:      Name: $name, Age: $age, GPA: $gpa")
print(t.substitute(name=name, age=age, gpa=f"{gpa:.2f}"))


# =============================================================================
# SECTION 7: SPECIAL PRINT TECHNIQUES
# =============================================================================
print("\n" + "=" * 70)
print("SECTION 7: SPECIAL PRINT TECHNIQUES")
print("=" * 70)

# --- ANSI Color Codes ---
print("\n--- ANSI Color Codes ---")
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f"{GREEN}[PASS]{RESET} Test 1 passed")
print(f"{RED}[FAIL]{RESET} Test 2 failed")
print(f"{YELLOW}[WARN]{RESET} Deprecation warning")
print(f"{BOLD}{BLUE}[INFO]{RESET} Application started")

# --- Tabular Output ---
print("\n--- Tabular Output ---")
header = f"{'Name':<15}{'Age':>5}{'City':<15}{'GPA':>6}"
print(header)
print("-" * len(header))
data = [
    ("Vikram", 25, "Hyderabad", 3.85),
    ("Alice", 22, "Bangalore", 3.92),
    ("Bob", 28, "Mumbai", 3.45),
    ("Charlie", 24, "Delhi", 3.78),
]
for name, age, city, gpa in data:
    print(f"{name:<15}{age:>5}{city:<15}{gpa:>6.2f}")

# --- Pretty Printing ---
print("\n--- Pretty Printing (pprint) ---")
complex_data = {
    "name": "Vikram",
    "skills": ["Python", "JavaScript", "Rust", "Go"],
    "experience": {
        "company": "Tech Corp",
        "years": 3,
        "projects": ["API Gateway", "ML Pipeline", "CLI Tools"]
    }
}
print("Regular print:")
print(complex_data)
print("\nPretty print:")
pprint(complex_data, width=50)

# --- Progress Bar ---
print("\n--- Progress Bar Demo ---")
total = 20
for i in range(total + 1):
    percent = (i / total) * 100
    bar = "#" * i + "." * (total - i)
    print(f"\r[{bar}] {percent:.0f}%", end="", flush=True)
    # time.sleep(0.1)  # Uncomment for animation effect
print()  # Final newline

# --- Logging-style output ---
print("\n--- Logging-style Output ---")


def log(level, message):
    """Simple logging function using formatted print."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    colors = {"INFO": GREEN, "WARN": YELLOW, "ERROR": RED}
    color = colors.get(level, RESET)
    print(f"{timestamp} {color}[{level:>5}]{RESET} {message}")


log("INFO", "Application started")
log("WARN", "Memory usage at 80%")
log("ERROR", "Connection timeout after 30s")


# =============================================================================
# SECTION 8: BEST PRACTICES SUMMARY
# =============================================================================
print("\n" + "=" * 70)
print("SECTION 8: BEST PRACTICES SUMMARY")
print("=" * 70)

print("""
+------------------+------------------------------------------+------------------+
| Method           | Use When                                 | Python Version   |
+------------------+------------------------------------------+------------------+
| f-strings        | Default choice, most readable            | 3.6+             |
| .format()        | Dynamic format strings, complex patterns | 2.6+ / 3.0+     |
| %-formatting     | Legacy code, C-style habits, logging     | All versions     |
| Template         | User-provided format strings (security)  | All versions     |
+------------------+------------------------------------------+------------------+

RULES OF THUMB:
  1. Use f-strings for almost everything (fastest & most readable)
  2. Use .format() when format string is stored in a variable
  3. Use %-formatting only in legacy code or logging module
  4. Use Template strings when format comes from untrusted input
  5. Always use flush=True for real-time progress output
  6. Use sep/end parameters instead of manual string concatenation
  7. Use file=sys.stderr for error messages
""")

print("=" * 70)
print("END OF ADVANCED PRINTING TUTORIAL")
print("=" * 70)
