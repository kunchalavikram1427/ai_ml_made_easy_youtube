"""
sys.argv Practical Example — Number Adder
==========================================
Run: python3 02_sys_argv_adder.py 5 10 15 20

Accepts one or more numbers as command line arguments,
validates them, and calculates sum/average/min/max.

Demonstrates:
- Argument count validation
- Type casting with error handling
- sys.exit() for error codes
- Usage messages
"""

import sys


def print_usage():
    """Print usage instructions and exit."""
    print(f"Usage: {sys.argv[0]} <num1> <num2> [num3 ...]")
    print(f"\nExamples:")
    print(f"  python3 {sys.argv[0]} 5 10 15")
    print(f"  python3 {sys.argv[0]} 3.14 2.71 1.41")
    print(f"  python3 {sys.argv[0]} -5 10 -3 8")
    sys.exit(1)


def main():
    # Check minimum argument count
    if len(sys.argv) < 3:
        print("Error: Need at least 2 numbers!")
        print_usage()

    # Convert arguments to numbers
    numbers = []
    for arg in sys.argv[1:]:
        try:
            numbers.append(float(arg))
        except ValueError:
            print(f"Error: '{arg}' is not a valid number!")
            sys.exit(1)

    # Calculate and display statistics
    print("=" * 40)
    print("  NUMBER STATISTICS")
    print("=" * 40)
    print(f"\n  Input:   {numbers}")
    print(f"  Count:   {len(numbers)}")
    print(f"  Sum:     {sum(numbers)}")
    print(f"  Average: {sum(numbers) / len(numbers):.2f}")
    print(f"  Min:     {min(numbers)}")
    print(f"  Max:     {max(numbers)}")
    print(f"  Range:   {max(numbers) - min(numbers)}")

    # Show as integers if all are whole numbers
    if all(n == int(n) for n in numbers):
        int_numbers = [int(n) for n in numbers]
        print(f"\n  (All whole numbers: {int_numbers})")

    print("=" * 40)


if __name__ == "__main__":
    main()
