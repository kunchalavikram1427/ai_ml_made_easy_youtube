"""
Exercise 3 Solution: Menu-Driven Calculator (Advanced)
=======================================================
Run: python3 03_calculator.py

Demonstrates:
- match-case for operation selection
- if/elif/else for input validation and edge cases
- Nested conditionals for complex decision-making
- Ternary operators for concise formatting
- Result chaining (use previous answer)
"""


def calculator():
    """
    Interactive calculator using match-case and conditionals.

    Features:
    - Basic operations (+, -, *, /, //, %, **)
    - Input validation with helpful error messages
    - Result chaining (use previous answer)
    - Precision modes (integer, 2 decimal, full)
    - Operation history
    """
    history = []
    last_result = None
    precision = "2"  # Default: 2 decimal places

    print("=" * 50)
    print("       PYTHON CALCULATOR")
    print("=" * 50)
    print("  Type 'ans' to use the previous result.")
    print("  Type 'menu' to see all options.")

    def format_result(value):
        """Format result based on current precision mode."""
        match precision:
            case "int":
                return f"{int(value)}"
            case "2":
                return f"{value:.2f}"
            case "full":
                return f"{value}"
            case _:
                return f"{value:.2f}"

    def get_number(prompt, allow_ans=True):
        """Get a valid number from user, supporting 'ans' keyword."""
        nonlocal last_result

        while True:
            user_input = input(prompt).strip().lower()

            # Allow using previous result
            if user_input == "ans" and allow_ans:
                if last_result is not None:
                    print(f"    (using previous result: {format_result(last_result)})")
                    return last_result
                else:
                    print("    No previous result available.")
                    continue

            # Validate number
            try:
                return float(user_input)
            except ValueError:
                print("    Invalid number. Please try again.")

    def show_menu():
        """Display the full menu."""
        print(f"\n  {'─' * 44}")
        print("  OPERATIONS:")
        print("    1. Add (+)")
        print("    2. Subtract (-)")
        print("    3. Multiply (*)")
        print("    4. Divide (/)")
        print("    5. Floor Divide (//)")
        print("    6. Modulo (%)")
        print("    7. Power (**)")
        print("  SETTINGS:")
        print("    8. Change Precision Mode")
        print("    9. View History")
        print("    0. Exit")
        print(f"  {'─' * 44}")

    show_menu()

    while True:
        # Show current state
        if last_result is not None:
            print(f"\n  [Last result: {format_result(last_result)}]")

        choice = input("\n  Select operation (0-9, or 'menu'): ").strip()

        if choice == "menu":
            show_menu()
            continue

        match choice:
            case "0":
                print("\n  Calculator history:")
                if history:
                    for i, entry in enumerate(history[-10:], 1):
                        print(f"    {i}. {entry}")
                else:
                    print("    (empty)")
                print("\n  Goodbye!")
                break

            case "1" | "2" | "3" | "4" | "5" | "6" | "7":
                # Get operation symbol
                operations = {
                    "1": ("+", "Addition"),
                    "2": ("-", "Subtraction"),
                    "3": ("*", "Multiplication"),
                    "4": ("/", "Division"),
                    "5": ("//", "Floor Division"),
                    "6": ("%", "Modulo"),
                    "7": ("**", "Power"),
                }
                symbol, name = operations[choice]
                print(f"\n  --- {name} ---")

                # Get operands
                a = get_number("  Enter first number: ")
                b = get_number("  Enter second number: ")

                # Perform operation with edge case handling
                error = None
                result = None

                if choice in ("4", "5", "6") and b == 0:
                    # Division by zero check
                    error = "Error: Division by zero is undefined!"
                elif choice == "7":
                    # Power overflow check
                    if abs(a) > 1000 and abs(b) > 100:
                        error = "Error: Result too large! Use smaller values."
                    elif a == 0 and b < 0:
                        error = "Error: Cannot raise 0 to a negative power!"
                    else:
                        try:
                            result = a ** b
                        except OverflowError:
                            error = "Error: Result too large (overflow)!"
                else:
                    # Standard operations
                    match choice:
                        case "1":
                            result = a + b
                        case "2":
                            result = a - b
                        case "3":
                            result = a * b
                        case "4":
                            result = a / b
                        case "5":
                            result = a // b
                        case "6":
                            result = a % b

                # Display result or error
                if error:
                    print(f"  {error}")
                else:
                    formatted = format_result(result)
                    expression = f"{format_result(a)} {symbol} {format_result(b)} = {formatted}"
                    print(f"\n  Result: {expression}")

                    # Update state
                    last_result = result
                    history.append(expression)

                    # Bonus info for certain operations
                    if choice == "5" and a / b != a // b:
                        print(f"  (Regular division would give: {format_result(a / b)})")
                    elif choice == "6":
                        quotient = int(a // b)
                        print(f"  (Quotient: {quotient}, Remainder: {formatted})")

            case "8":
                # Change precision mode
                print("\n  --- Precision Mode ---")
                print("    Current:", end=" ")
                match precision:
                    case "int":
                        print("Integer (no decimals)")
                    case "2":
                        print("2 decimal places")
                    case "full":
                        print("Full precision")

                print("\n    1. Integer (no decimals)")
                print("    2. 2 decimal places")
                print("    3. Full precision")

                mode_choice = input("    Select mode (1-3): ").strip()

                match mode_choice:
                    case "1":
                        precision = "int"
                        print("    Precision set to: Integer")
                    case "2":
                        precision = "2"
                        print("    Precision set to: 2 decimal places")
                    case "3":
                        precision = "full"
                        print("    Precision set to: Full precision")
                    case _:
                        print("    Invalid choice. Keeping current mode.")

            case "9":
                # View history
                print("\n  --- Calculation History ---")
                if history:
                    # Show last 10 entries
                    start = max(0, len(history) - 10)
                    for i, entry in enumerate(history[start:], start + 1):
                        print(f"    {i}. {entry}")
                    total_msg = f"  ({len(history)} total)" if len(history) > 10 else ""
                    print(f"  {total_msg}")
                else:
                    print("    No calculations yet.")

            case _:
                print("  Invalid option. Enter 'menu' to see options.")


# Run the calculator
if __name__ == "__main__":
    calculator()
