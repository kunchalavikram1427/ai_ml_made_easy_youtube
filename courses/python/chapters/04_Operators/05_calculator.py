"""
Full-Featured Terminal Calculator
==================================
Run: python3 05_calculator.py

Features:
- Basic arithmetic (+, -, *, /, //, %, **)
- Expression evaluation (calculator in 1 line!)
- Bitwise operations demo
- Operator precedence examples
- Interactive menu-driven interface
"""

# ============================================================
# CALCULATOR FUNCTIONS
# ============================================================


def basic_calculator():
    """Perform basic arithmetic operations between two numbers."""
    print("\n┌─────────────────────────────────────┐")
    print("│  BASIC ARITHMETIC CALCULATOR        │")
    print("├─────────────────────────────────────┤")
    print("│  Operations: + - * / // % **        │")
    print("│  Type 'back' to return to menu       │")
    print("└─────────────────────────────────────┘")

    while True:
        try:
            num1 = input("\n  First number (or 'back'): ")
            if num1.lower() == 'back':
                return

            num1 = float(num1)
            op = input("  Operator (+, -, *, /, //, %, **): ")
            num2 = float(input("  Second number: "))

            operations = {
                '+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: a / b if b != 0 else "Error: Division by zero!",
                '//': lambda a, b: a // b if b != 0 else "Error: Division by zero!",
                '%': lambda a, b: a % b if b != 0 else "Error: Division by zero!",
                '**': lambda a, b: a ** b,
            }

            if op in operations:
                result = operations[op](num1, num2)
                print(f"\n  ✅ {num1} {op} {num2} = {result}")
            else:
                print(f"  ❌ Unknown operator: '{op}'")

        except ValueError:
            print("  ❌ Invalid number! Please enter a numeric value.")


def expression_calculator():
    """The 'calculator in 1 line' - evaluate any math expression."""
    print("\n┌─────────────────────────────────────────────┐")
    print("│  EXPRESSION CALCULATOR (eval power!)        │")
    print("├─────────────────────────────────────────────┤")
    print("│  Type any math expression:                  │")
    print("│  Examples:                                  │")
    print("│    2 + 3 * 4                                │")
    print("│    (10 + 5) ** 2 / 3                        │")
    print("│    100 // 7 + 100 % 7                       │")
    print("│  Type 'back' to return to menu              │")
    print("└─────────────────────────────────────────────┘")
    print("\n  ⚠️  Note: eval() is powerful but dangerous with")
    print("  untrusted input. We restrict to math only here.\n")

    # Safe math functions to allow
    import math
    safe_dict = {"__builtins__": None}
    safe_dict.update({name: getattr(math, name) for name in dir(math) if not name.startswith("_")})

    while True:
        expr = input("  >>> ")
        if expr.lower() == 'back':
            return
        if not expr.strip():
            continue

        try:
            # Using eval with restricted builtins for safety
            result = eval(expr, safe_dict)
            print(f"  = {result}")
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            print(f"  ❌ Error: {e}")


def bitwise_demo():
    """Demonstrate bitwise operations with visual binary representation."""
    print("\n┌─────────────────────────────────────────────┐")
    print("│  BITWISE OPERATIONS DEMO                    │")
    print("└─────────────────────────────────────────────┘")

    a, b = 12, 10  # 1100 and 1010 in binary

    print(f"\n  a = {a:>3}  →  {a:08b}")
    print(f"  b = {b:>3}  →  {b:08b}")
    print(f"  {'─' * 35}")

    operations = [
        ("a & b  (AND)", a & b),
        ("a | b  (OR)", a | b),
        ("a ^ b  (XOR)", a ^ b),
        ("~a     (NOT)", ~a),
        ("a << 1 (Left Shift)", a << 1),
        ("a >> 1 (Right Shift)", a >> 1),
    ]

    for label, result in operations:
        # Handle negative numbers (NOT) display
        if result < 0:
            print(f"  {label:<22} = {result:>4}  →  {result & 0xFF:08b} (8-bit)")
        else:
            print(f"  {label:<22} = {result:>4}  →  {result:08b}")

    # Practical use cases
    print(f"\n  --- Practical Bitwise Tricks ---")
    print(f"  Check if 7 is odd:  7 & 1 = {7 & 1} (1=odd, 0=even)")
    print(f"  Check if 8 is odd:  8 & 1 = {8 & 1} (1=odd, 0=even)")
    print(f"  Multiply 5 by 4:   5 << 2 = {5 << 2}")
    print(f"  Divide 20 by 4:   20 >> 2 = {20 >> 2}")
    print(f"  Swap without temp:  a^=b; b^=a; a^=b")

    a, b = 5, 9
    print(f"\n  Before swap: a={a}, b={b}")
    a ^= b
    b ^= a
    a ^= b
    print(f"  After XOR swap: a={a}, b={b}")

    input("\n  Press Enter to return to menu...")


def precedence_demo():
    """Show operator precedence with examples."""
    print("\n┌─────────────────────────────────────────────┐")
    print("│  OPERATOR PRECEDENCE (highest to lowest)    │")
    print("└─────────────────────────────────────────────┘")

    precedence_table = """
  ┌────────┬─────────────────────────────────────┐
  │ Level  │ Operators                           │
  ├────────┼─────────────────────────────────────┤
  │   1    │ **        (exponentiation)          │
  │   2    │ ~ + -     (unary)                   │
  │   3    │ * / // %  (multiplication/division) │
  │   4    │ + -       (addition/subtraction)    │
  │   5    │ << >>     (bitwise shifts)          │
  │   6    │ &         (bitwise AND)             │
  │   7    │ ^ |       (bitwise XOR, OR)         │
  │   8    │ == != < > <= >=  (comparison)       │
  │   9    │ not       (logical NOT)             │
  │  10    │ and       (logical AND)             │
  │  11    │ or        (logical OR)              │
  └────────┴─────────────────────────────────────┘
"""
    print(precedence_table)

    # Tricky examples
    print("  --- Can You Guess the Results? ---\n")
    examples = [
        ("2 + 3 * 4", 2 + 3 * 4),
        ("(2 + 3) * 4", (2 + 3) * 4),
        ("2 ** 3 ** 2", 2 ** 3 ** 2),        # Right-associative!
        ("(2 ** 3) ** 2", (2 ** 3) ** 2),
        ("-2 ** 2", -2 ** 2),                  # Surprising!
        ("10 - 3 - 2", 10 - 3 - 2),          # Left-associative
        ("10 - (3 - 2)", 10 - (3 - 2)),
        ("True + True + True", True + True + True),  # Booleans are ints!
        ("15 // 4 * 4 + 15 % 4", 15 // 4 * 4 + 15 % 4),  # Reconstructs 15!
    ]

    for expr, result in examples:
        print(f"  {expr:<25} = {result}")

    print(f"\n  💡 Key insight: 2 ** 3 ** 2 = 2 ** (3 ** 2) = 2 ** 9 = 512")
    print(f"     Exponentiation is RIGHT-associative!")
    print(f"     -2 ** 2 = -(2 ** 2) = -4 (** binds tighter than unary -)")

    input("\n  Press Enter to return to menu...")


# ============================================================
# MAIN MENU
# ============================================================

def main():
    """Main menu loop for the calculator application."""
    while True:
        print("\n" + "=" * 50)
        print("  🧮 PYTHON CALCULATOR")
        print("=" * 50)
        print("""
  [1] Basic Arithmetic Calculator
  [2] Expression Calculator (eval magic)
  [3] Bitwise Operations Demo
  [4] Operator Precedence Guide
  [5] Quick Calculation (one-shot)
  [0] Exit
""")
        choice = input("  Choose an option: ").strip()

        if choice == '1':
            basic_calculator()
        elif choice == '2':
            expression_calculator()
        elif choice == '3':
            bitwise_demo()
        elif choice == '4':
            precedence_demo()
        elif choice == '5':
            expr = input("\n  Enter expression: ")
            try:
                print(f"  = {eval(expr)}")
            except Exception as e:
                print(f"  ❌ Error: {e}")
        elif choice == '0':
            print("\n  👋 Goodbye! Keep calculating!")
            break
        else:
            print("  ❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
