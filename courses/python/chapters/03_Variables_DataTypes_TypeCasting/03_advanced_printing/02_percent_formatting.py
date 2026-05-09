"""
%-Formatting (printf-style / Old Style)
=========================================
Run: python3 02_percent_formatting.py

Demonstrates:
- %s (string), %d (integer), %f (float) format specifiers
- Multiple values with tuples
- Hex (%x), Octal (%o) formatting
- Padding and alignment
- Width and precision

Note: This is the oldest formatting method. Use f-strings for new code,
but know %-formatting for reading legacy code and logging.
"""

# =============================================================================
# BASIC FORMAT SPECIFIERS
# =============================================================================
print("=" * 70)
print("  %-FORMATTING (printf-style)")
print("=" * 70)

name = "Vikram"
age = 25
height = 5.9

print("\n--- Basic specifiers ---")
print("String: %s" % name)
print("Integer: %d" % age)
print("Float: %f" % height)
print("Float (2 decimal): %.2f" % height)
print("Float (1 decimal): %.1f" % height)

# =============================================================================
# MULTIPLE VALUES (tuple)
# =============================================================================
print("\n--- Multiple values (tuple) ---")
print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))

# Real-world example
firmware_version = "v2.3.1"
url = "https://firmware.company.com/api/v2"
print("[Info]: Firmware %s from %s" % (firmware_version, url))

# =============================================================================
# HEX, OCTAL, BINARY
# =============================================================================
print("\n--- Hex and Octal ---")
num = 255
print("Decimal: %d" % num)
print("Hex (lower): %x" % num)
print("Hex (upper): %X" % num)
print("Octal: %o" % num)

# With prefix
print("With prefix: 0x%x, 0o%o" % (num, num))

# =============================================================================
# PADDING AND ALIGNMENT
# =============================================================================
print("\n--- Padding and Alignment ---")
print("Zero-padded: %05d" % 42)
print("Zero-padded: %08d" % 42)
print("Left-aligned: |%-10s|" % "left")
print("Right-aligned: |%10s|" % "right")
print("Space-padded int: |%6d|" % 42)

# =============================================================================
# WIDTH AND PRECISION COMBINED
# =============================================================================
print("\n--- Formatted Price List ---")
items = [
    ("Coffee", 4.50),
    ("Sandwich", 8.99),
    ("Cake", 12.00),
    ("Smoothie", 6.75),
    ("Salad", 9.50),
]

print("%-15s %8s" % ("Item", "Price"))
print("-" * 25)
for item, price in items:
    print("%-15s $%7.2f" % (item, price))

total = sum(p for _, p in items)
print("-" * 25)
print("%-15s $%7.2f" % ("TOTAL", total))

# =============================================================================
# COMMON PATTERNS
# =============================================================================
print("\n--- Common Patterns ---")
# Padding with zeros (useful for file naming)
for i in range(1, 6):
    print("file_%03d.txt" % i)

print("\n" + "=" * 70)
print("NOTE: Use f-strings for new code. %-formatting is for legacy/logging.")
print("=" * 70)
