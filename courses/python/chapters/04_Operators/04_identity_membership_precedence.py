"""
Identity, Membership & Operator Precedence
============================================
Run: python3 04_identity_membership_precedence.py

Covers:
- Identity operators: is, is not
- Why use 'is' for None
- Membership operators: in, not in
- Operator precedence table and examples
"""


# =============================================================================
# IDENTITY OPERATORS (is / is not)
# =============================================================================

print("=" * 55)
print("  IDENTITY OPERATORS")
print("=" * 55)

# 'is' checks IDENTITY (same object in memory)
# '==' checks EQUALITY (same value)
print(f"\n  --- is vs == ---")

# Small integers are cached by Python (-5 to 256)
a = 256
b = 256
print(f"  a = 256, b = 256")
print(f"  a == b  -> {a == b}")   # True (same value)
print(f"  a is b  -> {a is b}")   # True (same cached object)

# Lists — mutable objects are never cached
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # Same reference

print(f"\n  list1 = [1,2,3], list2 = [1,2,3], list3 = list1")
print(f"  list1 == list2  -> {list1 == list2}")   # True (same content)
print(f"  list1 is list2  -> {list1 is list2}")   # False (different objects!)
print(f"  list1 is list3  -> {list1 is list3}")   # True (same object)

# ALWAYS use 'is' for None comparisons
print(f"\n  --- Always use 'is' for None ---")
x = None
print(f"  x = None")
print(f"  x is None     -> {x is None}")       # Correct
print(f"  x is not None -> {x is not None}")   # Correct


# =============================================================================
# MEMBERSHIP OPERATORS (in / not in)
# Membership operators check whether a value exists inside a collection. Whereas identity operators check if two variables point to the same object in memory.
# =============================================================================

print(f"\n{'=' * 55}")
print("  MEMBERSHIP OPERATORS")
print("=" * 55)

# Lists
fruits = ['apple', 'banana', 'cherry']
print(f"\n  fruits = {fruits}")
print(f"  'banana' in fruits     -> {'banana' in fruits}")       # True
print(f"  'grape' in fruits      -> {'grape' in fruits}")        # False
print(f"  'grape' not in fruits  -> {'grape' not in fruits}")    # True

# Strings (substring check)
message = "Hello, World!"
print(f"\n  message = '{message}'")
print(f"  'World' in message     -> {'World' in message}")      # True
print(f"  'world' in message     -> {'world' in message}")      # False (case-sensitive)

# Dictionaries (checks KEYS, not values!)
user = {'name': 'Vikram', 'age': 28}
print(f"\n  user = {user}")
print(f"  'name' in user          -> {'name' in user}")           # True (key exists)
print(f"  'Vikram' in user        -> {'Vikram' in user}")         # False (not a key!)
print(f"  'Vikram' in user.values() -> {'Vikram' in user.values()}")  # True

# Sets (very fast membership testing)
allowed = {'.py', '.txt', '.json'}
print(f"\n  allowed = {allowed}")
print(f"  '.py' in allowed  -> {'.py' in allowed}")    # True
print(f"  '.exe' in allowed -> {'.exe' in allowed}")   # False


# =============================================================================
# OPERATOR PRECEDENCE
# =============================================================================

print(f"\n{'=' * 55}")
print("  OPERATOR PRECEDENCE (highest to lowest)")
print("=" * 55)

print("""
  1.  ()         Parentheses
  2.  **         Exponentiation
  3.  +x -x ~x  Unary plus, minus, bitwise NOT
  4.  * / // %  Multiplication, division, modulo
  5.  + -       Addition, subtraction
  6.  << >>     Bitwise shifts
  7.  &         Bitwise AND
  8.  ^ |       Bitwise XOR, OR
  9.  == != < > <= >=  is  in    Comparisons
  10. not       Logical NOT
  11. and       Logical AND
  12. or        Logical OR
""")

# Tricky examples
print("  --- Precedence Examples ---")
print(f"  2 + 3 * 4     = {2 + 3 * 4}")         # 14 (not 20)
print(f"  (2 + 3) * 4   = {(2 + 3) * 4}")       # 20
print(f"  -2 ** 2       = {-2 ** 2}")            # -4 (** before unary -)
print(f"  2 ** 3 ** 2   = {2 ** 3 ** 2}")        # 512 (right-associative!)
print(f"  (2 ** 3) ** 2 = {(2 ** 3) ** 2}")      # 64

print(f"\n  Key insight: ** is RIGHT-associative")
print(f"  2 ** 3 ** 2 = 2 ** (3**2) = 2 ** 9 = 512")