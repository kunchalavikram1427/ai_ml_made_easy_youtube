"""
.format() Method — String Formatting
======================================
Run: python3 03_dot_format_method.py

Demonstrates:
- Basic positional and named arguments
- Explicit index reuse
- Alignment: left, right, center, fill chars
- Number formatting: decimals, commas, signs, percentages
- Binary, Hex, Octal with .format()
"""

# =============================================================================
# BASIC POSITIONAL
# =============================================================================
print("=" * 70)
print("  .format() METHOD")
print("=" * 70)

name = "Vikram"
age = 25

print("\n--- Basic positional ---")
print("Hello, {}!".format(name))
print("{} is {} years old.".format(name, age))

# =============================================================================
# EXPLICIT INDEX (reuse arguments)
# =============================================================================
print("\n--- Explicit positional index ---")
print("{0} likes {1}. {0} also likes {2}.".format("Vikram", "Python", "AI"))
print("{0}! {0}! {0}!".format("Go"))

# =============================================================================
# NAMED ARGUMENTS
# =============================================================================
print("\n--- Named arguments ---")
print("{name} lives in {city}".format(name="Vikram", city="Hyderabad"))

# From a dictionary
data = {"product": "Laptop", "price": 999.99, "stock": 15}
print("{product}: ${price:.2f} ({stock} in stock)".format(**data))

# =============================================================================
# ALIGNMENT
# =============================================================================
print("\n--- Alignment ---")
print("|{:<20}|".format("Left aligned"))
print("|{:>20}|".format("Right aligned"))
print("|{:^20}|".format("Centered"))

# Custom fill characters
print("|{:*^20}|".format("Stars"))
print("|{:-<20}|".format("Dashes"))
print("|{:.>20}|".format("Dots"))

# =============================================================================
# NUMBER FORMATTING
# =============================================================================
print("\n--- Number formatting ---")
pi = 3.14159265
big_number = 1000000
negative = -42.5

print("Pi (2 decimals): {:.2f}".format(pi))
print("Pi (5 decimals): {:.5f}".format(pi))
print("Big with commas: {:,}".format(big_number))
print("Big with underscores: {:_}".format(big_number))
print("Signed positive: {:+.2f}".format(pi))
print("Signed negative: {:+.2f}".format(negative))
print("Percentage: {:.1%}".format(0.856))
print("Percentage: {:.0%}".format(0.5))
print("Scientific: {:.2e}".format(0.00123))

# =============================================================================
# BINARY, HEX, OCTAL
# =============================================================================
print("\n--- Binary, Hex, Octal ---")
num = 42
print("Decimal: {:d}".format(num))
print("Binary: {:b}".format(num))
print("Hex: {:x}".format(num))
print("Octal: {:o}".format(num))
print("With prefix: {:#b}, {:#x}, {:#o}".format(42, 255, 8))

# =============================================================================
# PRACTICAL: FORMATTED TABLE
# =============================================================================
print("\n--- Formatted Table ---")
header = "{:<12} {:>8} {:>10}".format("Language", "Users(M)", "Growth")
print(header)
print("-" * len(header))

languages = [
    ("Python", 15.7, 0.25),
    ("JavaScript", 17.4, 0.12),
    ("Rust", 2.8, 0.45),
    ("Go", 3.5, 0.18),
]

for lang, users, growth in languages:
    print("{:<12} {:>8.1f} {:>9.0%}".format(lang, users, growth))

print("\n" + "=" * 70)
