"""
Exercise 3 Solution: Full-Featured Calculator (Advanced)
=========================================================
Run: python3 03_calculator.py

Reference: Calculator in 1 Line - https://youtube.com/shorts/Xb6wWEcSeuk

Demonstrates:
- All Python operators in practical use
- Multiple calculator modes (Basic, Expression, Conversion, Bitwise)
- Input validation and error handling
- History tracking
- Safe expression evaluation
"""

import re
import math


def full_calculator():
    """
    Comprehensive calculator supporting all Python operators.

    Modes:
    - Basic: Two numbers and an operator (safe, no eval)
    - Expression: Parse and evaluate mathematical expressions
    - Conversion: Binary, Decimal, Hex, Octal conversions
    - Bitwise: Visualize bitwise operations with binary representation
    - History: View last 10 calculations
    """
    history = []

    def add_to_history(entry):
        """Add an entry to calculation history."""
        history.append(entry)
        if len(history) > 10:
            history.pop(0)

    def basic_mode():
        """Basic calculator: two numbers and an operator."""
        print("\n  --- Basic Mode ---")
        print("  Operators: +, -, *, /, //, %, **")

        # Get first number
        while True:
            try:
                a = float(input("  Enter first number: "))
                break
            except ValueError:
                print("  Invalid number. Try again.")

        # Get operator
        valid_ops = ["+", "-", "*", "/", "//", "%", "**"]
        while True:
            op = input(f"  Operator ({', '.join(valid_ops)}): ").strip()
            if op in valid_ops:
                break
            print(f"  Invalid operator. Choose from: {', '.join(valid_ops)}")

        # Get second number
        while True:
            try:
                b = float(input("  Enter second number: "))
                break
            except ValueError:
                print("  Invalid number. Try again.")

        # Calculate
        try:
            if op in ("/", "//", "%") and b == 0:
                print("  Error: Division by zero!")
                return
            elif op == "**" and abs(b) > 1000:
                print("  Error: Exponent too large!")
                return

            operations = {
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
                "/": lambda x, y: x / y,
                "//": lambda x, y: x // y,
                "%": lambda x, y: x % y,
                "**": lambda x, y: x ** y,
            }

            result = operations[op](a, b)

            # Format nicely (show as int if it's a whole number)
            if isinstance(result, float) and result == int(result):
                result_str = str(int(result))
            else:
                result_str = f"{result:.6g}"

            a_str = int(a) if a == int(a) else a
            b_str = int(b) if b == int(b) else b

            entry = f"{a_str} {op} {b_str} = {result_str}"
            print(f"\n  Result: {entry}")
            add_to_history(entry)

        except OverflowError:
            print("  Error: Result too large (overflow)!")

    def expression_mode():
        """Expression calculator with safe evaluation."""
        print("\n  --- Expression Mode ---")
        print("  Enter a math expression (e.g., (2 + 3) * 4 - 1)")
        print("  Supported: +, -, *, /, //, %, **, (, )")
        print("  Functions: sqrt(), abs(), round(), pow()")

        expr = input("  Expression: ").strip()

        if not expr:
            print("  Empty expression!")
            return

        # Sanitize input - only allow safe characters
        # Allow numbers, operators, parentheses, spaces, dots, and function names
        safe_pattern = r'^[\d\s\+\-\*\/\%\.\(\)\,a-z_]+$'
        if not re.match(safe_pattern, expr):
            print("  Error: Expression contains invalid characters!")
            return

        # Only allow specific function names
        allowed_funcs = {"sqrt", "abs", "round", "pow", "min", "max"}
        func_pattern = r'[a-z_]+'
        found_funcs = set(re.findall(func_pattern, expr))
        # Remove 'e' from scientific notation
        found_funcs.discard("e")

        for func in found_funcs:
            if func not in allowed_funcs:
                print(f"  Error: Function '{func}' is not allowed!")
                return

        # Create safe namespace
        safe_globals = {
            "__builtins__": {},
            "sqrt": math.sqrt,
            "abs": abs,
            "round": round,
            "pow": pow,
            "min": min,
            "max": max,
        }

        try:
            result = eval(expr, safe_globals)

            if isinstance(result, float) and result == int(result) and abs(result) < 1e15:
                result_str = str(int(result))
            else:
                result_str = f"{result:.6g}"

            entry = f"{expr} = {result_str}"
            print(f"\n  Result: {entry}")
            add_to_history(entry)

        except ZeroDivisionError:
            print("  Error: Division by zero!")
        except SyntaxError:
            print("  Error: Invalid expression syntax!")
        except (ValueError, TypeError) as e:
            print(f"  Error: {e}")
        except OverflowError:
            print("  Error: Result too large!")

    def conversion_mode():
        """Number base conversion mode."""
        print("\n  --- Conversion Mode ---")
        print("  Convert between Decimal, Binary, Octal, and Hex")

        # Get input format
        print("  Input format: [d]ecimal, [b]inary, [o]ctal, [h]ex")
        fmt = input("  Format: ").strip().lower()

        num_input = input("  Number: ").strip()

        try:
            # Parse based on input format
            if fmt in ("d", "decimal"):
                number = int(num_input)
            elif fmt in ("b", "binary"):
                number = int(num_input.replace("0b", ""), 2)
            elif fmt in ("o", "octal"):
                number = int(num_input.replace("0o", ""), 8)
            elif fmt in ("h", "hex"):
                number = int(num_input.replace("0x", ""), 16)
            else:
                print("  Invalid format! Use d, b, o, or h.")
                return

            # Display all conversions
            print(f"\n  Results:")
            print(f"    Decimal: {number}")
            print(f"    Binary:  {bin(number)}")
            print(f"    Octal:   {oct(number)}")
            print(f"    Hex:     {hex(number)}")

            if number >= 0:
                print(f"    Bits:    {number.bit_length()} bits needed")

            entry = f"{num_input} ({fmt}) -> dec:{number}, bin:{bin(number)}, hex:{hex(number)}"
            add_to_history(entry)

        except ValueError:
            print(f"  Error: '{num_input}' is not a valid {fmt} number!")

    def bitwise_mode():
        """Bitwise operation visualizer."""
        print("\n  --- Bitwise Mode ---")
        print("  Visualize bitwise operations with binary representation")

        # Get two numbers
        while True:
            try:
                a = int(input("  Enter A (integer): "))
                break
            except ValueError:
                print("  Please enter a valid integer.")

        while True:
            try:
                b = int(input("  Enter B (integer): "))
                break
            except ValueError:
                print("  Please enter a valid integer.")

        # Determine display width
        bit_width = max(8, max(abs(a), abs(b)).bit_length() + 1)

        def to_bin(n):
            """Convert to binary string with fixed width."""
            if n >= 0:
                return format(n, f'0{bit_width}b')
            else:
                # Show two's complement for negative numbers
                return format(n & ((1 << bit_width) - 1), f'0{bit_width}b')

        # Display results
        print(f"\n  A = {a:>6}  ({to_bin(a)})")
        print(f"  B = {b:>6}  ({to_bin(b)})")
        print(f"  {'─' * 40}")

        results = [
            ("A & B ", a & b, "AND"),
            ("A | B ", a | b, "OR"),
            ("A ^ B ", a ^ b, "XOR"),
            ("~A    ", ~a, "NOT A"),
            ("A << 1", a << 1, "Left shift A"),
            ("A >> 1", a >> 1, "Right shift A"),
        ]

        for label, result, desc in results:
            print(f"  {label} = {result:>6}  ({to_bin(result)})  # {desc}")

        entry = f"Bitwise: A={a}, B={b} -> A&B={a & b}, A|B={a | b}, A^B={a ^ b}"
        add_to_history(entry)

    def show_history():
        """Display calculation history."""
        print("\n  --- Calculation History ---")
        if not history:
            print("  (empty)")
        else:
            for i, entry in enumerate(history, 1):
                print(f"    {i:>2}. {entry}")
        print(f"\n  Total calculations this session: {len(history)}")

    # ── Main Loop ────────────────────────────────────────────────
    print("=" * 55)
    print("       PYTHON CALCULATOR")
    print("=" * 55)

    while True:
        print(f"\n  Modes: [B]asic | [E]xpression | [C]onversion | [Bi]twise | [H]istory | [Q]uit")
        mode = input("  Mode: ").strip().lower()

        match mode:
            case "b" | "basic":
                basic_mode()
            case "e" | "expression":
                expression_mode()
            case "c" | "conversion":
                conversion_mode()
            case "bi" | "bitwise":
                bitwise_mode()
            case "h" | "history":
                show_history()
            case "q" | "quit":
                print(f"\n  Goodbye! Total calculations: {len(history)}")
                break
            case _:
                print("  Invalid mode. Choose B, E, C, Bi, H, or Q.")


# Run the calculator
if __name__ == "__main__":
    full_calculator()
