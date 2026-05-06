"""
Comments in Python - Examples
==============================
Run: python3 examples.py

This script demonstrates all types of comments in Python
using basic variables for context.
"""

# ============================================================
# SECTION 1: Single-Line Comments
# ============================================================
print("=" * 60)
print("  SINGLE-LINE COMMENTS")
print("=" * 60)

# This is a single-line comment — Python ignores this entirely
name = "Vikram"
age = 25
city = "Hyderabad"

# You can explain what a group of variables represents
# User profile information loaded from the database
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")


# ============================================================
# SECTION 2: Inline Comments
# ============================================================
print("\n" + "=" * 60)
print("  INLINE COMMENTS")
print("=" * 60)

seconds_per_day = 86400  # 60 sec * 60 min * 24 hours
max_retries = 3  # API rate limit allows max 3 retries per minute
timeout = 30  # Server drops idle connections after 30 seconds

print(f"Seconds in a day: {seconds_per_day}")
print(f"Max retries: {max_retries}")
print(f"Timeout: {timeout}s")

# Note: the # inside a string is NOT a comment
hashtag = "#Python"  # This part IS a comment
print(f"Hashtag: {hashtag}")


# ============================================================
# SECTION 3: Multi-Line Comments
# ============================================================
print("\n" + "=" * 60)
print("  MULTI-LINE COMMENTS")
print("=" * 60)

# Calculate compound interest
# Formula: A = P(1 + r/n)^(nt)
# Where:
#   P = principal amount
#   r = annual interest rate (as decimal)
#   n = number of times compounded per year
#   t = number of years
principal = 1000
rate = 0.05
compounds_per_year = 12
years = 10

amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
print(f"Principal: ${principal}")
print(f"After {years} years at {rate*100}%: ${amount:.2f}")


# ============================================================
# SECTION 4: Commenting Out Code (Debugging)
# ============================================================
print("\n" + "=" * 60)
print("  COMMENTING OUT CODE")
print("=" * 60)

x = 10
y = 20

# Old approach (disabled for now):
# result = x + y
# print(f"Sum: {result}")

# New approach:
result = x * y  # Changed from addition to multiplication
print(f"Product of {x} and {y}: {result}")

# TODO: Add division with zero-check
# TODO: Move calculations to a separate function


# ============================================================
# SECTION 5: Docstrings Preview
# ============================================================
print("\n" + "=" * 60)
print("  DOCSTRINGS (BRIEF INTRO)")
print("=" * 60)


def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    pi = 3.14159
    return pi * radius ** 2


# Docstrings are accessible at runtime
print(f"Function docstring: {calculate_area.__doc__}")
print(f"Area of circle (r=5): {calculate_area(5):.2f}")


# ============================================================
# SECTION 6: Best Practices Demo
# ============================================================
print("\n" + "=" * 60)
print("  BEST PRACTICES")
print("=" * 60)

# GOOD: Explains WHY, not WHAT
retry_delay = 2  # Exponential backoff starts at 2s (per AWS recommendations)

# GOOD: Explains non-obvious logic
is_leap_year = (2024 % 4 == 0 and 2024 % 100 != 0) or (2024 % 400 == 0)
# A year is a leap year if divisible by 4, UNLESS divisible by 100,
# EXCEPT when also divisible by 400

print(f"Retry delay: {retry_delay}s")
print(f"2024 is a leap year: {is_leap_year}")

# GOOD: Section dividers for visual organization
# ============================================================
print("\n" + "-" * 60)
print("Comments help you write professional, maintainable code!")
print("Remember: explain WHY, not WHAT.")
print("-" * 60)
