"""
sys.argv Manual Flag Parsing
==============================
Run: python3 03_sys_argv_flags.py --verbose data.csv --output result.txt
     python3 03_sys_argv_flags.py data.csv
     python3 03_sys_argv_flags.py --help

Demonstrates how to manually parse flags and options from sys.argv.
This is how it was done before getopt/argparse — educational, but
use argparse for real projects!

Demonstrates:
- Checking for boolean flags (--verbose, --help)
- Extracting flag values (--output <filename>)
- Separating flags from positional arguments
"""

import sys


def show_help():
    """Display help message."""
    print(f"Usage: {sys.argv[0]} [OPTIONS] <input_file>")
    print(f"\nOptions:")
    print(f"  --help       Show this help message")
    print(f"  --verbose    Enable detailed output")
    print(f"  --output F   Specify output file (default: stdout)")
    print(f"  --count N    Number of lines to process (default: all)")
    print(f"\nExamples:")
    print(f"  python3 {sys.argv[0]} data.csv")
    print(f"  python3 {sys.argv[0]} --verbose data.csv --output result.txt")
    print(f"  python3 {sys.argv[0]} data.csv --count 100 --verbose")
    sys.exit(0)


def parse_args(argv):
    """Manually parse command line arguments."""
    args = {
        "verbose": False,
        "output": None,
        "count": None,
        "input_file": None,
    }

    i = 1  # Skip script name (argv[0])
    positional = []

    while i < len(argv):
        if argv[i] == "--help":
            show_help()
        elif argv[i] == "--verbose":
            args["verbose"] = True
        elif argv[i] == "--output":
            if i + 1 >= len(argv):
                print("Error: --output requires a filename!")
                sys.exit(1)
            args["output"] = argv[i + 1]
            i += 1  # Skip the value
        elif argv[i] == "--count":
            if i + 1 >= len(argv):
                print("Error: --count requires a number!")
                sys.exit(1)
            try:
                args["count"] = int(argv[i + 1])
            except ValueError:
                print(f"Error: --count value must be a number, got '{argv[i + 1]}'")
                sys.exit(1)
            i += 1  # Skip the value
        elif argv[i].startswith("--"):
            print(f"Error: Unknown option '{argv[i]}'")
            print(f"Run with --help for usage information")
            sys.exit(1)
        else:
            positional.append(argv[i])
        i += 1

    # Get input file from positional arguments
    if positional:
        args["input_file"] = positional[0]

    return args


def main():
    if len(sys.argv) < 2:
        print("Error: No input file specified!")
        print(f"Run: python3 {sys.argv[0]} --help")
        sys.exit(1)

    args = parse_args(sys.argv)

    # Display parsed results
    print("=" * 50)
    print("  PARSED ARGUMENTS")
    print("=" * 50)
    print(f"\n  Input file: {args['input_file']}")
    print(f"  Output:     {args['output'] or '(stdout)'}")
    print(f"  Verbose:    {args['verbose']}")
    print(f"  Count:      {args['count'] or '(all lines)'}")

    if args["verbose"]:
        print(f"\n  [VERBOSE] Raw sys.argv: {sys.argv}")
        print(f"  [VERBOSE] Total args: {len(sys.argv)}")

    # Simulate processing
    print(f"\n  Would process: {args['input_file']}")
    if args["output"]:
        print(f"  Would write to: {args['output']}")
    if args["count"]:
        print(f"  Would limit to: {args['count']} lines")

    print("=" * 50)


if __name__ == "__main__":
    main()
