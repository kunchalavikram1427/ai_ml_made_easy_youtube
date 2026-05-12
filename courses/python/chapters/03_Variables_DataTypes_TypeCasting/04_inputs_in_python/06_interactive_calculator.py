"""
Interactive Calculator — Putting It All Together
==================================================
Run: python3 06_interactive_calculator.py

Demonstrates:
- Combining input(), type casting, split(), and validation
- Building a complete interactive program
- Menu-style loop with quit option
- Error handling for bad input

This file is INTERACTIVE — it will ask you for input when you run it!
"""


def calculator():
    """Simple calculator that demonstrates input patterns."""
    print("=" * 40)
    print("  SIMPLE CALCULATOR")
    print("=" * 40)
    print("  Operations: +, -, *, /")
    print("  Type 'quit' to exit")
    print("=" * 40)

    while True:
        print()
        expression = input("  Enter expression (e.g., 5 + 3): ").strip()

        if expression.lower() == "quit":
            print("\n  Goodbye!")
            break

        try:
            parts = expression.split()
            if len(parts) != 3:
                print("  Format: number operator number")
                continue

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("  Error: Division by zero!")
                    continue
                result = num1 / num2
            else:
                print(f"  Unknown operator: {operator}")
                print("  Use: +, -, *, /")
                continue

            # Show clean output (no decimals if result is a whole number)
            if result == int(result):
                print(f"  = {int(result)}")
            else:
                print(f"  = {result}")

        except ValueError:
            print("  Error: Invalid numbers. Try again.")
        except IndexError:
            print("  Format: number operator number")


# Run the calculator
calculator()
