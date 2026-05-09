"""
argparse Basics — The Recommended Approach
============================================
Run: python3 05_argparse_basics.py Vikram
     python3 05_argparse_basics.py Vikram -g "Good morning"
     python3 05_argparse_basics.py Vikram --greeting Hey --shout -n 3
     python3 05_argparse_basics.py --help

argparse is the recommended way to handle command line arguments in Python.
It provides automatic help generation, type checking, default values,
and clear error messages.

Demonstrates:
- Positional arguments (required)
- Optional arguments with short and long forms
- Default values
- Boolean flags (store_true)
- Type conversion (type=int)
- Auto-generated --help
"""

import argparse


def create_parser():
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="A friendly greeting program",
        epilog="Example: %(prog)s Vikram -g 'Good morning' --shout -n 3"
    )

    # Positional argument (required — no -- prefix)
    parser.add_argument(
        "name",
        help="Name of the person to greet"
    )

    # Optional arguments (with -- prefix)
    parser.add_argument(
        "-g", "--greeting",
        default="Hello",
        help="Greeting word to use (default: %(default)s)"
    )

    parser.add_argument(
        "-n", "--times",
        type=int,
        default=1,
        help="Number of times to repeat the greeting (default: %(default)s)"
    )

    # Boolean flag (False by default, True when --shout is present)
    parser.add_argument(
        "--shout",
        action="store_true",
        help="SHOUT the greeting in uppercase"
    )

    parser.add_argument(
        "--formal",
        action="store_true",
        help="Use formal greeting style"
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    # Build the greeting message
    if args.formal:
        message = f"Dear {args.name}, {args.greeting}. It is a pleasure to meet you."
    else:
        message = f"{args.greeting}, {args.name}!"

    # Apply shout modifier
    if args.shout:
        message = message.upper()

    # Print the greeting
    print()
    for i in range(args.times):
        print(f"  {message}")
    print()

    # Show what argparse parsed (educational)
    print("-" * 40)
    print("  Parsed arguments:")
    print(f"    name:     {args.name}")
    print(f"    greeting: {args.greeting}")
    print(f"    times:    {args.times}")
    print(f"    shout:    {args.shout}")
    print(f"    formal:   {args.formal}")
    print("-" * 40)


if __name__ == "__main__":
    main()
