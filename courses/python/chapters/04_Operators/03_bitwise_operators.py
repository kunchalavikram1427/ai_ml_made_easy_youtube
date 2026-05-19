"""
Bitwise Operators
==================
Run: python3 03_bitwise_operators.py

Covers:
- AND (&), OR (|), XOR (^)
- Left shift (<<), Right shift (>>)
- Binary visualization of operations
- Practical uses: even/odd check, XOR swap, permission flags
"""


# =============================================================================
# BITWISE OPERATORS EXPLAINED
# =============================================================================

print("=" * 55)
print("  BITWISE OPERATORS")
print("=" * 55)

a = 12  # Binary: 1100
b = 10  # Binary: 1010

print(f"\n  a = {a}  -> binary: {a:08b}")
print(f"  b = {b}  -> binary: {b:08b}")
print(f"  {'─' * 40}")

# AND — both bits must be 1
result = a & b
print(f"\n  a & b (AND)  = {result:>2} -> {result:04b}")
print(f"    {a:04b}")
print(f"  & {b:04b}")
print(f"  ------")
print(f"    {result:04b}")

# OR — either bit can be 1
result = a | b
print(f"\n  a | b (OR)   = {result:>2} -> {result:04b}")
print(f"    {a:04b}")
print(f"  | {b:04b}")
print(f"  ------")
print(f"    {result:04b}")

# XOR — bits must differ (Symbol name is Caret)
result = a ^ b
print(f"\n  a ^ b (XOR)  = {result:>2} -> {result:04b}")
print(f"    {a:04b}")
print(f"  ^ {b:04b}")
print(f"  ------")
print(f"    {result:04b}")

# Left shift — multiply by 2^n
print(f"\n  a << 1 (Left Shift)  = {a << 1:>2} -> {a << 1:05b}")
print(f"    {a:04b} shifted left by 1 = {a << 1:05b}")

# Right shift — divide by 2^n (floor)
print(f"\n  a >> 1 (Right Shift) = {a >> 1:>2} -> {a >> 1:04b}")
print(f"    {a:04b} shifted right by 1 = {a >> 1:04b}")


# =============================================================================
# PRACTICAL USES
# =============================================================================

print(f"\n{'=' * 55}")
print("  PRACTICAL BITWISE TRICKS")
print("=" * 55)

# 1. XOR swap (swap without temp variable)
print(f"\n  --- XOR Swap ---")
x, y = 5, 9
print(f"  Before: x={x}, y={y}")
x ^= y
y ^= x
x ^= y
print(f"  After:  x={x}, y={y}")

# 2. Powers of 2 with left shift
print(f"\n  --- Powers of 2 ---")
print(f"  1 << 0  = {1 << 0}")    # 1
print(f"  1 << 1  = {1 << 1}")    # 2
print(f"  1 << 4  = {1 << 4}")    # 16
print(f"  1 << 10 = {1 << 10}")   # 1024

print(f"\n{'=' * 55}")
