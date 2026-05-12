"""
Template Strings — Safe Formatting for Untrusted Input
========================================================
Run: python3 05_template_strings.py

Demonstrates:
- Basic Template substitution
- safe_substitute() (no KeyError on missing keys)
- When to use Template strings
- Comparison of all 4 formatting methods
"""

from string import Template

# =============================================================================
# BASIC TEMPLATE STRINGS
# =============================================================================
print("=" * 70)
print("  TEMPLATE STRINGS (string.Template)")
print("=" * 70)

# --- Basic template ---
print("\n--- Basic substitution ---")
t = Template("Hello, $name! You are $age years old.")
result = t.substitute(name="Vikram", age=25)
print(result)

# Using ${} for clarity (when followed by valid identifier chars)
t = Template("${item}s cost $$$price each")
result = t.substitute(item="Widget", price="9.99")
print(result)

# =============================================================================
# safe_substitute() — NO KeyError ON MISSING KEYS
# =============================================================================
print("\n--- safe_substitute (missing keys stay as-is) ---")
t = Template("$greeting, $name! Your role is $role.")

# substitute() would raise KeyError for missing 'role'
result = t.safe_substitute(greeting="Hi", name="Vikram")
print(result)  # $role remains as-is — no crash!

# Compare with substitute (would crash)
try:
    t.substitute(greeting="Hi", name="Vikram")
except KeyError as e:
    print(f"substitute() raised KeyError: {e}")


# =============================================================================
# COMPARISON: ALL 4 FORMATTING METHODS
# =============================================================================
print("\n" + "=" * 70)
print("  ALL 4 METHODS SIDE BY SIDE")
print("=" * 70)

name = "Vikram"
age = 25
gpa = 3.856

print("\n--- Same output, 4 methods ---")
print("%%-formatting: Name: %s, Age: %d, GPA: %.2f" % (name, age, gpa))
print(".format():     Name: {}, Age: {}, GPA: {:.2f}".format(name, age, gpa))
print(f"f-string:      Name: {name}, Age: {age}, GPA: {gpa:.2f}")
t = Template("Template:      Name: $name, Age: $age, GPA: $gpa")
print(t.substitute(name=name, age=age, gpa=f"{gpa:.2f}"))

# =============================================================================
# WHEN TO USE WHAT
# =============================================================================
print("\n" + "=" * 70)
print("  WHEN TO USE WHAT")
print("=" * 70)

print("""
  +------------------+------------------------------------------+
  | Method           | Use When                                 |
  +------------------+------------------------------------------+
  | f-strings        | Default choice, most readable (3.6+)     |
  | .format()        | Dynamic format strings, complex patterns |
  | %-formatting     | Legacy code, logging module              |
  | Template         | User-provided format strings (SECURITY)  |
  +------------------+------------------------------------------+
""")

print("=" * 70)
