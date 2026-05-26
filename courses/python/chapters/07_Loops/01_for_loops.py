"""
For Loops — Iteration, range(), enumerate(), zip()
====================================================
Run: python3 02_for_loops.py

Covers:
- for loop basics (iterating over sequences)
- range() function (start, stop, step)
- enumerate() for index + value
- zip() for parallel iteration
- Nested loops
- Loop else clause
"""


# =============================================================================
# FOR LOOP BASICS
# =============================================================================

print("=" * 55)
print("  FOR LOOP BASICS")
print("=" * 55)

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
print(f"\n  fruits = {fruits}")
print(f"  for fruit in fruits:")
for fruit in fruits:
    print(f"    -> {fruit}")

# Iterating over a string
print(f"\n  for char in 'Python':")
for char in "Python":
    print(f"    -> '{char}'")

# Iterating over a dictionary
user = {"name": "Vikram", "age": 28, "city": "Hyderabad"}
print(f"\n  for key, value in user.items():")
for key, value in user.items():
    print(f"    {key}: {value}")


# =============================================================================
# range() FUNCTION
# =============================================================================

print(f"\n{'=' * 55}")
print("  range() FUNCTION")
print("=" * 55)

# range(stop) — 0 to stop-1
print(f"\n  range(5)       = {list(range(5))}")

# range(start, stop)
print(f"  range(2, 7)    = {list(range(2, 7))}")

# range(start, stop, step)
print(f"  range(0, 10, 2) = {list(range(0, 10, 2))}")   # Even numbers
print(f"  range(10, 0, -1) = {list(range(10, 0, -1))}")  # Countdown
print(f"  range(10, 0, -3) = {list(range(10, 0, -3))}")  # Skip by 3

# Practical: sum of 1 to 100
total = sum(range(1, 101))
print(f"\n  sum(range(1, 101)) = {total}")

# Practical: multiplication table
print(f"\n  --- 5x Table ---")
for i in range(1, 6):
    print(f"    5 x {i} = {5 * i}")


# =============================================================================
# enumerate() — INDEX + VALUE
# =============================================================================

print(f"\n{'=' * 55}")
print("  enumerate() — INDEX + VALUE")
print("=" * 55)

# Without enumerate (ugly)
print(f"\n  --- Without enumerate (don't do this) ---")
colors = ["red", "green", "blue"]
for i in range(len(colors)):
    print(f"    {i}: {colors[i]}")

# With enumerate (Pythonic!)
print(f"\n  --- With enumerate (Pythonic!) ---")
for i, color in enumerate(colors):
    print(f"    {i}: {color}")

# Custom start index
print(f"\n  --- enumerate with start=1 ---")
for rank, color in enumerate(colors, start=1):
    print(f"    #{rank}: {color}")


# =============================================================================
# zip() — PARALLEL ITERATION
# =============================================================================

print(f"\n{'=' * 55}")
print("  zip() — PARALLEL ITERATION")
print("=" * 55)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"\n  names  = {names}")
print(f"  scores = {scores}")
print(f"\n  for name, score in zip(names, scores):")
for name, score in zip(names, scores):
    print(f"    {name}: {score}")

# zip with three lists
cities = ["Delhi", "Mumbai", "Bangalore"]
print(f"\n  --- Three lists ---")
for name, score, city in zip(names, scores, cities):
    print(f"    {name} from {city} scored {score}")

# zip stops at shortest list
short = [1, 2]
long = [10, 20, 30, 40]
print(f"\n  zip([1,2], [10,20,30,40]) = {list(zip(short, long))}")
print(f"  (stops at shortest!)")


# =============================================================================
# NESTED LOOPS
# =============================================================================

print(f"\n{'=' * 55}")
print("  NESTED LOOPS")
print("=" * 55)

# Multiplication table
print(f"\n  --- 3x3 Multiplication Table ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"    {i} x {j} = {i * j:>2}", end="  ")
    print()  # New line after each row

# Pattern: right triangle
print(f"\n  --- Right Triangle (n=5) ---")
for i in range(1, 6):
    print(f"    {'* ' * i}")

# Pattern: pyramid
print(f"\n  --- Pyramid (n=5) ---")
n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(f"    {spaces}{stars}")


# =============================================================================
# LOOP ELSE CLAUSE
# =============================================================================

print(f"\n{'=' * 55}")
print("  LOOP ELSE CLAUSE")
print("=" * 55)

# else runs ONLY if loop completes WITHOUT break
print(f"\n  --- Search with loop else ---")
numbers = [2, 4, 6, 8, 10]
target = 7

print(f"  Looking for {target} in {numbers}...")
for num in numbers:
    if num == target:
        print(f"  Found {target}!")
        break
else:
    # This runs because loop finished without break
    print(f"  {target} not found in list!")

# Compare: found case
target = 6
print(f"\n  Looking for {target} in {numbers}...")
for num in numbers:
    if num == target:
        print(f"  Found {target}!")
        break
else:
    print(f"  {target} not found in list!")

print(f"\n{'=' * 55}")
