"""
getopt Module — Unix-Style Option Parsing
===========================================
Run: python3 04_getopt_demo.py -i data.csv -o result.json -v
     python3 04_getopt_demo.py --input data.csv --output result.json --verbose
     python3 04_getopt_demo.py -h

The getopt module parses command line options in the traditional
Unix style — both short (-h, -v, -i) and long (--help, --verbose,
--input) formats.

Demonstrates:
- Short options (single dash + letter)
- Long options (double dash + word)
- Options with required values (colon / equals)
- Error handling for invalid options
"""

import sys
import getopt


def show_help():
    """Display usage information."""
    print(f"Usage: {sys.argv[0]} [OPTIONS]")
    print(f"\nOptions:")
    print(f"  -h, --help              Show this help message")
    print(f"  -i, --input FILE        Input file path (required)")
    print(f"  -o, --output FILE       Output file path (default: output.txt)")
    print(f"  -v, --verbose           Enable verbose mode")
    print(f"  -n, --lines NUM         Number of lines to process")
    print(f"\nExamples:")
    print(f"  python3 {sys.argv[0]} -i data.csv -o result.json -v")
    print(f"  python3 {sys.argv[0]} --input data.csv --output result.json")
    print(f"  python3 {sys.argv[0]} -i data.csv -n 100 -v")


def main():
    # Default values
    input_file = ""
    output_file = "output.txt"
    verbose = False
    num_lines = None

    # Define expected options
    # Short: "hi:o:vn:" -> h (flag), i: (value), o: (value), v (flag), n: (value)
    # Long: ["help", "input=", "output=", "verbose", "lines="]
    short_opts = "hi:o:vn:"
    long_opts = ["help", "input=", "output=", "verbose", "lines="]

    try:
        opts, remaining_args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError as e:
        print(f"Error: {e}")
        print(f"Run '{sys.argv[0]} --help' for usage information")
        sys.exit(2)

    # Process parsed options
    for opt, value in opts:
        if opt in ("-h", "--help"):
            show_help()
            sys.exit(0)
        elif opt in ("-i", "--input"):
            input_file = value
        elif opt in ("-o", "--output"):
            output_file = value
        elif opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-n", "--lines"):
            try:
                num_lines = int(value)
            except ValueError:
                print(f"Error: --lines must be a number, got '{value}'")
                sys.exit(2)

    # Validate required options
    if not input_file:
        print("Error: Input file is required! Use -i or --input")
        print(f"Run '{sys.argv[0]} --help' for usage information")
        sys.exit(2)

    # Display results
    print("=" * 50)
    print("  getopt PARSING RESULTS")
    print("=" * 50)

    if verbose:
        print(f"\n  [DEBUG] Raw opts: {opts}")
        print(f"  [DEBUG] Remaining args: {remaining_args}")

    print(f"\n  Input file:  {input_file}")
    print(f"  Output file: {output_file}")
    print(f"  Verbose:     {verbose}")
    print(f"  Lines:       {num_lines or '(all)'}")

    if remaining_args:
        print(f"  Extra args:  {remaining_args}")

    # Simulate processing
    print(f"\n  Processing '{input_file}' -> '{output_file}'", end="")
    if num_lines:
        print(f" (first {num_lines} lines)", end="")
    print(" ... done!")

    print("=" * 50)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments provided!")
        print(f"Run: python3 {sys.argv[0]} --help")
        sys.exit(1)
    main()
