"""
argparse Choices, Mutually Exclusive Groups, and nargs
========================================================
Run: python3 06_argparse_choices.py --format json --level 2
     python3 06_argparse_choices.py --format csv --output table
     python3 06_argparse_choices.py --numbers 1 2 3 4 5
     python3 06_argparse_choices.py --tags python cli argparse
     python3 06_argparse_choices.py --help

Demonstrates advanced argparse features:
- choices= to restrict values to a set
- Mutually exclusive argument groups
- nargs for accepting multiple values
- nargs="+" (one or more), "*" (zero or more), N (exact count)
"""

import argparse


def create_parser():
    """Create parser demonstrating choices, groups, and nargs."""
    parser = argparse.ArgumentParser(
        description="Demo: choices, mutually exclusive groups, and nargs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --format json --level 2
  %(prog)s --format csv --output table --numbers 10 20 30
  %(prog)s --tags python cli tools --format json
  %(prog)s --numbers 1 2 3 4 5 --output json
        """
    )

    # --- Choices: restricted set of values ---
    parser.add_argument(
        "--format",
        choices=["json", "csv", "xml", "yaml"],
        default="json",
        help="Data format (default: %(default)s)"
    )

    parser.add_argument(
        "--level",
        type=int,
        choices=[1, 2, 3, 4, 5],
        default=1,
        help="Processing level 1-5 (default: %(default)s)"
    )

    parser.add_argument(
        "--color",
        choices=["red", "green", "blue", "yellow"],
        default=None,
        help="Highlight color (optional)"
    )

    # --- Mutually exclusive: only one can be used ---
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument(
        "--output",
        choices=["table", "json", "plain"],
        default="plain",
        help="Display format (default: plain)"
    )
    output_group.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress all output (can't use with --output)"
    )

    # --- nargs: accept multiple values ---
    parser.add_argument(
        "--numbers",
        type=int,
        nargs="+",
        help="One or more numbers to process (at least 1 required)"
    )

    parser.add_argument(
        "--tags",
        nargs="*",
        default=[],
        help="Zero or more tags (optional)"
    )

    parser.add_argument(
        "--range",
        type=int,
        nargs=2,
        metavar=("START", "END"),
        help="Exactly two numbers: start and end"
    )

    return parser


def display_results(args):
    """Display the parsed arguments in a nice format."""
    print("=" * 55)
    print("  PARSED ARGUMENTS")
    print("=" * 55)

    if args.quiet:
        print("\n  [QUIET MODE — minimal output]")
        print(f"  Format: {args.format}, Level: {args.level}")
        print("=" * 55)
        return

    # Choices results
    print(f"\n  --- Choices ---")
    print(f"  Format: {args.format}")
    print(f"  Level:  {args.level}")
    print(f"  Color:  {args.color or '(none)'}")

    # Mutually exclusive results
    print(f"\n  --- Output Mode ---")
    print(f"  Output: {args.output}")
    print(f"  Quiet:  {args.quiet}")

    # nargs results
    print(f"\n  --- Multiple Values (nargs) ---")
    print(f"  Numbers: {args.numbers or '(none provided)'}")
    print(f"  Tags:    {args.tags or '(none provided)'}")
    print(f"  Range:   {args.range or '(none provided)'}")

    # Process numbers if provided
    if args.numbers:
        print(f"\n  --- Number Statistics ---")
        print(f"  Sum:     {sum(args.numbers)}")
        print(f"  Average: {sum(args.numbers) / len(args.numbers):.2f}")
        print(f"  Min:     {min(args.numbers)}")
        print(f"  Max:     {max(args.numbers)}")

    # Process range if provided
    if args.range:
        start, end = args.range
        print(f"\n  --- Range ---")
        print(f"  From {start} to {end} (span: {end - start})")

    # Show output format
    if args.output == "table":
        print(f"\n  --- Table Output ---")
        print(f"  {'Key':<12} {'Value'}")
        print(f"  {'-'*12} {'-'*20}")
        print(f"  {'format':<12} {args.format}")
        print(f"  {'level':<12} {args.level}")
        print(f"  {'color':<12} {args.color or 'N/A'}")

    elif args.output == "json":
        import json
        data = {
            "format": args.format,
            "level": args.level,
            "color": args.color,
            "numbers": args.numbers,
            "tags": args.tags,
        }
        print(f"\n  --- JSON Output ---")
        print(f"  {json.dumps(data, indent=4)}")

    print("\n" + "=" * 55)


def main():
    parser = create_parser()
    args = parser.parse_args()
    display_results(args)


if __name__ == "__main__":
    main()
