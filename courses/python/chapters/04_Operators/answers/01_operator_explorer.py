"""
Exercise 1 Solution: Operator Explorer (Beginner)
===================================================
Run: python3 01_operator_explorer.py

Demonstrates:
- All arithmetic operators (+, -, *, /, //, %, **)
- All comparison operators (==, !=, >, <, >=, <=)
- Bitwise operators (&, |, ^, ~, <<, >>)
- Membership operator (in)
- Formatted table output
"""


def operator_explorer():
    """
    Explore all Python operators with two user-provided numbers.
    Displays results in a clean, formatted table.
    """
    print("=" * 50)
    print("       OPERATOR EXPLORER")
    print("=" * 50)

    # Get user input with validation
    while True:
        try:
            a = int(input("\n  Enter first number: "))
            break
        except ValueError:
            print("  Please enter a valid integer.")

    while True:
        try:
            b = int(input("  Enter second number: "))
            break
        except ValueError:
            print("  Please enter a valid integer.")

    print()

    # ── Arithmetic Operators ─────────────────────────────────────
    print(f"  ╔══ ARITHMETIC ═══════════════════════════╗")
    print(f"  ║  {a} + {b:<4} = {a + b:<28}║")
    print(f"  ║  {a} - {b:<4} = {a - b:<28}║")
    print(f"  ║  {a} * {b:<4} = {a * b:<28}║")

    if b != 0:
        print(f"  ║  {a} / {b:<4} = {a / b:<28}║")
        print(f"  ║  {a} // {b:<3} = {a // b:<28}║")
        print(f"  ║  {a} % {b:<4} = {a % b:<28}║")
    else:
        print(f"  ║  {a} / {b:<4} = {'Error: div by zero':<28}║")
        print(f"  ║  {a} // {b:<3} = {'Error: div by zero':<28}║")
        print(f"  ║  {a} % {b:<4} = {'Error: div by zero':<28}║")

    # Guard against very large exponentiation
    if abs(b) <= 20:
        print(f"  ║  {a} ** {b:<3} = {a ** b:<28}║")
    else:
        print(f"  ║  {a} ** {b:<3} = {'(too large to display)':<28}║")

    # ── Comparison Operators ─────────────────────────────────────
    print(f"  ╠══ COMPARISON ═══════════════════════════╣")
    print(f"  ║  {a} == {b:<3} -> {str(a == b):<27}║")
    print(f"  ║  {a} != {b:<3} -> {str(a != b):<27}║")
    print(f"  ║  {a} > {b:<4} -> {str(a > b):<27}║")
    print(f"  ║  {a} < {b:<4} -> {str(a < b):<27}║")
    print(f"  ║  {a} >= {b:<3} -> {str(a >= b):<27}║")
    print(f"  ║  {a} <= {b:<3} -> {str(a <= b):<27}║")

    # ── Bitwise Operators ────────────────────────────────────────
    print(f"  ╠══ BITWISE ══════════════════════════════╣")

    # Determine bit width for display
    max_val = max(abs(a), abs(b), abs(a & b), abs(a | b), abs(a ^ b))
    bit_width = max(4, max_val.bit_length())

    a_bin = format(a & ((1 << bit_width) - 1), f'0{bit_width}b') if a >= 0 else bin(a)
    b_bin = format(b & ((1 << bit_width) - 1), f'0{bit_width}b') if b >= 0 else bin(b)

    and_result = a & b
    or_result = a | b
    xor_result = a ^ b
    not_result = ~a
    lshift = a << 1
    rshift = a >> 1

    and_bin = format(and_result & ((1 << bit_width) - 1), f'0{bit_width}b')
    or_bin = format(or_result & ((1 << bit_width) - 1), f'0{bit_width}b')
    xor_bin = format(xor_result & ((1 << bit_width) - 1), f'0{bit_width}b')

    print(f"  ║  a = {a} ({a_bin})")
    print(f"  ║  b = {b} ({b_bin})")
    print(f"  ║  {'─' * 38}║")
    print(f"  ║  {a} & {b:<4} = {and_result:<4} ({and_bin}){' ' * (20 - bit_width)}║")
    print(f"  ║  {a} | {b:<4} = {or_result:<4} ({or_bin}){' ' * (20 - bit_width)}║")
    print(f"  ║  {a} ^ {b:<4} = {xor_result:<4} ({xor_bin}){' ' * (20 - bit_width)}║")
    print(f"  ║  ~{a:<7} = {not_result:<30}║")
    print(f"  ║  {a} << 1 = {lshift:<30}║")
    print(f"  ║  {a} >> 1 = {rshift:<30}║")

    # ── Membership Operator ──────────────────────────────────────
    print(f"  ╠══ MEMBERSHIP ═════════════════════════════╣")
    range_end = abs(b) if b != 0 else 10
    in_range = a in range(0, range_end + 1)
    print(f"  ║  {a} in range(0, {range_end + 1}) -> {str(in_range):<20}║")

    # Check if a is in a list containing b
    sample_list = list(range(0, max(abs(a), abs(b)) + 5))
    print(f"  ║  {a} in [0..{sample_list[-1]}] -> {str(a in sample_list):<22}║")

    print(f"  ╚═══════════════════════════════════════════╝")

    # ── Summary ──────────────────────────────────────────────────
    print(f"\n  --- Quick Summary ---")
    print(f"  Largest result:  {a} ** {b} = {a ** b if abs(b) <= 20 else '(overflow)'}")
    print(f"  Are they equal?  {'Yes' if a == b else 'No'}")
    print(f"  Which is larger? {'a' if a > b else 'b' if b > a else 'equal'}")


# Run the program
if __name__ == "__main__":
    operator_explorer()
