"""
Comparison & Logical Operators
================================
Run: python3 02_comparison_and_logical.py

Covers:
- Comparison operators: ==, !=, <, >, <=, >=
- Chained comparisons (Python's elegant feature)
- Logical operators: and, or, not
- Short-circuit evaluation
- Practical defaults pattern with 'or'
"""


# =============================================================================
# COMPARISON (RELATIONAL) OPERATORS
# =============================================================================

print("=" * 55)
print("  COMPARISON OPERATORS")
print("=" * 55)

# Numeric comparisons
print(f"\n  --- Numeric Comparisons ---")
print(f"  10 == 10   -> {10 == 10}")     # True
print(f"  10 == 10.0 -> {10 == 10.0}")   # True (cross-type works for numbers)
print(f"  10 != 5    -> {10 != 5}")      # True
print(f"  5 < 10     -> {5 < 10}")       # True
print(f"  10 > 10    -> {10 > 10}")      # False
print(f"  10 >= 10   -> {10 >= 10}")     # True
print(f"  5 <= 4     -> {5 <= 4}")       # False

# Chained comparisons (Python's elegant feature!)
print(f"\n  --- Chained Comparisons ---")
x = 15
print(f"  x = {x}")
print(f"  10 < x < 20   -> {10 < x < 20}")      # True (is x between 10 and 20?)
print(f"  1 <= x <= 100  -> {1 <= x <= 100}")    # True
print(f"  0 < x < 10    -> {0 < x < 10}")        # False

age = 25
print(f"\n  age = {age}")
print(f"  18 <= age < 65 -> {18 <= age < 65}")   # Working age check

# Comparison with different types
print(f"\n  --- Type Comparisons ---")
print(f"  1 == True   -> {1 == True}")     # True (bool is subclass of int)
print(f"  0 == False  -> {0 == False}")    # True
print(f"  '1' == 1    -> {'1' == 1}")      # False (no implicit conversion!)
print(f"  None == 0   -> {None == 0}")     # False


# =============================================================================
# LOGICAL OPERATORS
# =============================================================================

print(f"\n{'=' * 55}")
print("  LOGICAL OPERATORS")
print("=" * 55)


# Basic logical operations
print(f"\n  --- Truth Table: AND ---")
print(f"  True  and True  -> {True and True}")     # True
print(f"  True  and False -> {True and False}")    # False
print(f"  False and True  -> {False and True}")    # False
print(f"  False and False -> {False and False}")   # False

'''
In Python, the and operator returns the first falsy value or the last truthy value.

x = 5
y = 10

print(x and y) # returns 10 because both x and y are truthy, so it returns the last value. If x were falsy (like 0), it would return x instead.

print(0 and 10)      # 0
print(5 and 10)      # 10
print("" and "Hi")   # ""
print(True and 7)    # 7
'''

print(f"\n  --- Truth Table: OR ---")
print(f"  True  or True  -> {True or True}")      # True
print(f"  True  or False -> {True or False}")     # True
print(f"  False or True  -> {False or True}")     # True
print(f"  False or False -> {False or False}")    # False

'''
For or, Python stops immediately and returns the first truthy value it encounters. If all values are falsy, it returns the last value.

print(0 or 10)        # 10
print(5 or 10)        # 5
print("" or "Hello")  # "Hello"
print(None or 7)      # 7
'''

print(f"\n  --- NOT ---")
print(f"  not True  -> {not True}")    # False
print(f"  not False -> {not False}")   # True

# Real-world example
print("\n--- Website Login Access ---")

is_logged_in = True
has_subscription = False

if is_logged_in and has_subscription:
    print("Premium content unlocked")

if is_logged_in or has_subscription:
    print("Basic access granted")

# =============================================================================
# SHORT-CIRCUIT EVALUATION
# =============================================================================

'''
They are called short-circuit because Python stops evaluating as soon as it already knows the final result.
It takes a “shorter path” instead of checking everything.

Example with and:

print(0 and 42)

Python checks:

0 → falsy
For and, one falsy value already makes the whole expression falsy
So Python stops immediately
42 is never evaluated

Example with or:

print(42 or 0)

Python checks:

42 → truthy
For or, one truthy value already makes the expression truthy
So Python stops immediately
0 is never evaluated

That stopping behavior is called short-circuit evaluation.
'''

print(f"\n{'=' * 55}")
print("  SHORT-CIRCUIT EVALUATION")
print("=" * 55)

# 'and' short-circuits on False (returns first falsy value)
print(f"\n  --- AND short-circuits ---")
print(f"  0 and 42       -> {0 and 42}")         # 0 (stops at first falsy)
print(f"  42 and 0       -> {42 and 0}")         # 0 (continues, returns second)
print(f"  42 and 'hello' -> {42 and 'hello'}")   # 'hello' (both truthy, returns last)

# 'or' short-circuits on True (returns first truthy value)
print(f"\n  --- OR short-circuits ---")
print(f"  0 or 42          -> {0 or 42}")            # 42
print(f"  42 or 0          -> {42 or 0}")            # 42 (stops at first truthy)
print(f"  '' or 'default'  -> {'' or 'default'}")    # 'default'
print(f"  None or 'fallback' -> {None or 'fallback'}")  # 'fallback'

# Practical: defaults pattern
print(f"\n  --- Defaults Pattern ---")
username = ""  # Empty (user didn't provide)
display_name = username or "Anonymous"
print(f"  username = '' ")
print(f"  username or 'Anonymous' -> '{display_name}'")