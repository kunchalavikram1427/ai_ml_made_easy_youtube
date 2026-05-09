"""
f-Strings — The Preferred Formatting Method (Python 3.6+)
==========================================================
Run: python3 04_fstrings.py

Demonstrates:
- Basic f-string syntax
- Expressions and method calls inside {}
- Number formatting (decimals, commas, scientific)
- Binary/Hex formatting
- Alignment and padding
- Debug mode (f"{x=}")  — Python 3.8+
- Date/time formatting
- repr vs str (!r vs !s)
"""

from datetime import datetime

# =============================================================================
# BASIC f-STRINGS
# =============================================================================
print("=" * 70)
print("  f-STRINGS (PREFERRED METHOD)")
print("=" * 70)

name = "Vikram"
age = 25

print(f"\n--- Basic f-string ---")
print(f"Hello, {name}!")
print(f"{name} is {age} years old.")

# =============================================================================
# EXPRESSIONS INSIDE f-STRINGS
# =============================================================================
print(f"\n--- Expressions inside {{}} ---")
print(f"Sum: {2 + 3}")
print(f"Product: {7 * 8}")
print(f"Even check: {age % 2 == 0}")
print(f"Status: {'adult' if age >= 18 else 'minor'}")
print(f"List: {[x**2 for x in range(5)]}")

# =============================================================================
# METHOD CALLS
# =============================================================================
print(f"\n--- Method calls ---")
msg = "hello world"
print(f"Upper: {msg.upper()}")
print(f"Title: {msg.title()}")
print(f"Length: {len(msg)}")
print(f"Replace: {msg.replace('world', 'Python')}")

items = ["apple", "banana", "cherry"]
print(f"Joined: {', '.join(items)}")

# =============================================================================
# NUMBER FORMATTING
# =============================================================================
print(f"\n--- Number formatting ---")
price = 49.99
count = 1500000
pi = 3.14159265
tiny = 0.00123

print(f"Price: ${price:.2f}")
print(f"Count (commas): {count:,}")
print(f"Count (underscores): {count:_}")
print(f"Pi (3 decimals): {pi:.3f}")
print(f"Pi (6 decimals): {pi:.6f}")
print(f"Percentage: {0.856:.1%}")
print(f"Percentage: {0.5:.0%}")
print(f"Scientific: {tiny:.2e}")
print(f"Scientific: {count:.2e}")

# =============================================================================
# BINARY, HEX FORMATTING
# =============================================================================
print(f"\n--- Binary and Hex ---")
num = 42
print(f"Binary: {num:b}")
print(f"Binary (8-bit): {num:08b}")
print(f"Hex: {num:x}")
print(f"Hex (uppercase): {num:X}")
print(f"Hex (with prefix): {num:#x}")
print(f"Octal: {num:o}")

# Practical: RGB color
r, g, b = 255, 128, 0
print(f"RGB({r},{g},{b}) = #{r:02X}{g:02X}{b:02X}")

# =============================================================================
# ALIGNMENT AND PADDING
# =============================================================================
print(f"\n--- Alignment ---")
print(f"|{'Left':<15}|")
print(f"|{'Right':>15}|")
print(f"|{'Center':^15}|")
print(f"|{'Filled':*^15}|")
print(f"|{'Dashed':-^15}|")

# Formatted price list
print(f"\n--- Formatted Price List ---")
items = [("Coffee", 4.50), ("Sandwich", 8.99), ("Cake", 12.00), ("Smoothie", 6.75)]
for item, price in items:
    print(f"  {item:<12} ${price:>6.2f}")

# =============================================================================
# DEBUG MODE (Python 3.8+) — f"{x=}"
# =============================================================================
print(f"\n--- Debug mode (= syntax) ---")
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")
print(f"{name=}, {age=}")
print(f"{len(items)=}")
print(f"{pi=:.4f}")

# =============================================================================
# DATE/TIME FORMATTING
# =============================================================================
print(f"\n--- Date/Time formatting ---")
now = datetime.now()
print(f"ISO format: {now:%Y-%m-%d}")
print(f"Time: {now:%H:%M:%S}")
print(f"Readable: {now:%B %d, %Y}")
print(f"Short: {now:%b %d, %Y %I:%M %p}")
print(f"Day of week: {now:%A}")

# =============================================================================
# repr vs str (!r vs !s)
# =============================================================================
print(f"\n--- repr vs str ---")
text = "Hello\tWorld"
path = "C:\\Users\\file.txt"
print(f"str:  {text}")
print(f"repr: {text!r}")
print(f"str:  {path}")
print(f"repr: {path!r}")

# Useful for debugging — shows exact string content
data = "  spaces  "
print(f"\ndata = {data!r}  (shows hidden spaces)")

print(f"\n" + "=" * 70)
print(f"TIP: f-strings are the fastest and most readable. Use them by default!")
print(f"=" * 70)
