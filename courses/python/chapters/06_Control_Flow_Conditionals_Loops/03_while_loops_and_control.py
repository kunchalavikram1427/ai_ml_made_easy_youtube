"""
While Loops & Loop Control Statements
=======================================
Run: python3 03_while_loops_and_control.py

Covers:
- while loop basics
- break statement (exit loop early)
- continue statement (skip to next iteration)
- pass statement (placeholder)
- Infinite loops and when to use them
- Common while loop patterns
"""


# =============================================================================
# WHILE LOOP BASICS
# =============================================================================

print("=" * 55)
print("  WHILE LOOP BASICS")
print("=" * 55)

# Basic countdown
print(f"\n  --- Countdown ---")
count = 5
while count > 0:
    print(f"    {count}...")
    count -= 1
print(f"    Go!")

# Accumulator pattern
print(f"\n  --- Sum until >= 100 ---")
total = 0
n = 1
while total < 100:
    total += n
    n += 1
print(f"    Sum of 1 to {n-1} = {total} (first sum >= 100)")

# Condition-based loop
print(f"\n  --- Halving until < 1 ---")
value = 100.0
steps = 0
while value >= 1:
    value /= 2
    steps += 1
print(f"    After {steps} halvings: {value:.4f}")


# =============================================================================
# BREAK STATEMENT
# =============================================================================

print(f"\n{'=' * 55}")
print("  BREAK STATEMENT")
print("=" * 55)

# break exits the loop immediately
print(f"\n  --- Find first even number > 10 ---")
numbers = [3, 7, 11, 4, 15, 12, 8, 20]
print(f"  numbers = {numbers}")
for num in numbers:
    if num > 10 and num % 2 == 0:
        print(f"  Found: {num}")
        break
    print(f"    Checking {num}... no")

# break in while loop (input simulation)
print(f"\n  --- Menu with break ---")
menu_items = ["start", "help", "quit"]
for item in menu_items:
    print(f"    Processing: '{item}'")
    if item == "quit":
        print(f"    -> Exiting!")
        break


# =============================================================================
# CONTINUE STATEMENT
# =============================================================================

print(f"\n{'=' * 55}")
print("  CONTINUE STATEMENT")
print("=" * 55)

# continue skips to the next iteration
print(f"\n  --- Print only odd numbers 1-10 ---")
print(f"  ", end="")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"{i} ", end="")
print()

# Skip specific items
print(f"\n  --- Skip errors ---")
data = [10, -1, 20, -1, 30, -1, 40]
clean = []
for val in data:
    if val == -1:
        continue
    clean.append(val)
print(f"  data  = {data}")
print(f"  clean = {clean}")


# =============================================================================
# PASS STATEMENT
# =============================================================================

print(f"\n{'=' * 55}")
print("  PASS STATEMENT")
print("=" * 55)

# pass does nothing — it's a placeholder
print(f"\n  pass is used when syntax requires a statement")
print(f"  but you don't want to do anything yet.\n")

# Placeholder for future implementation
print(f"  --- Placeholder Examples ---")


def process_data():
    pass  # TODO: implement later


class MyClass:
    pass  # TODO: add methods later


# In conditionals
x = 10
if x > 0:
    pass  # Handle positive (not implemented yet)
else:
    pass  # Handle non-positive

print(f"  def process_data(): pass   # Compiles fine!")
print(f"  class MyClass: pass        # Compiles fine!")
print(f"  if condition: pass         # Does nothing")

# pass vs continue in loops
print(f"\n  --- pass vs continue ---")
print(f"  pass: does nothing, continues to NEXT LINE in loop body")
print(f"  continue: skips to NEXT ITERATION of loop")


# =============================================================================
# COMMON WHILE LOOP PATTERNS
# =============================================================================

print(f"\n{'=' * 55}")
print("  COMMON WHILE PATTERNS")
print("=" * 55)

# Pattern 1: Sentinel value
print(f"\n  --- Sentinel Value Pattern ---")
commands = ["run", "test", "deploy", "exit", "cleanup"]
print(f"  commands = {commands}")
i = 0
while i < len(commands):
    cmd = commands[i]
    if cmd == "exit":
        print(f"    '{cmd}' -> stopping!")
        break
    print(f"    '{cmd}' -> executed")
    i += 1

# Pattern 2: Retry with limit
print(f"\n  --- Retry Pattern ---")
import random
random.seed(42)
max_attempts = 5
attempt = 0
success = False

while attempt < max_attempts and not success:
    attempt += 1
    result = random.randint(1, 3)  # Simulate: 1 = success
    if result == 1:
        success = True
        print(f"    Attempt {attempt}: Success!")
    else:
        print(f"    Attempt {attempt}: Failed (got {result})")

if not success:
    print(f"    All {max_attempts} attempts failed!")

# Pattern 3: Converging value
print(f"\n  --- Convergence Pattern ---")
# Newton's method for square root of 25
guess = 25.0
target = 25
tolerance = 0.0001

iterations = 0
while abs(guess * guess - target) > tolerance:
    guess = (guess + target / guess) / 2
    iterations += 1

print(f"  sqrt(25) via Newton's method:")
print(f"    Result: {guess:.6f} (in {iterations} iterations)")


# =============================================================================
# INFINITE LOOPS (and when to use them)
# =============================================================================

print(f"\n{'=' * 55}")
print("  INFINITE LOOPS")
print("=" * 55)

print(f"""
  Infinite loops run forever until break is called.
  Use them when you don't know how many iterations you need.

  Common uses:
  - Interactive menus (loop until user quits)
  - Server event loops (run until shutdown)
  - Game loops (run until game over)
  - Retry until success

  Pattern:
    while True:
        # do something
        if done_condition:
            break
""")

# Example: process items until empty
print(f"  --- Process Queue ---")
queue = [3, 1, 4, 1, 5]
print(f"  queue = {queue}")
while True:
    if not queue:
        print(f"    Queue empty, done!")
        break
    item = queue.pop(0)
    print(f"    Processing: {item}")

print(f"\n{'=' * 55}")
