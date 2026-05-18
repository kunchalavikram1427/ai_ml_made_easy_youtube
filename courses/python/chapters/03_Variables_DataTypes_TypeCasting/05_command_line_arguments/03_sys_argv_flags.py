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
import csv


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
                if args["count"] <= 0:
                    print("Error: --count must be greater than 0")
                    sys.exit(1)
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


def _build_table(headers, rows):
    """Return a plain-text table string with aligned columns."""
    if not headers:
        return "(No headers found in CSV)"

    column_count = max(len(headers), max((len(row) for row in rows), default=0))
    normalized_headers = list(headers) + [f"column_{i}" for i in range(len(headers) + 1, column_count + 1)]
    normalized_rows = [
        list(row) + [""] * (column_count - len(row))
        for row in rows
    ]

    widths = [len(str(normalized_headers[i])) for i in range(column_count)]
    for row in normalized_rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    border = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def format_row(row):
        return "| " + " | ".join(f"{str(row[i]):<{widths[i]}}" for i in range(column_count)) + " |"

    lines = [border, format_row(normalized_headers), border]
    lines.extend(format_row(row) for row in normalized_rows)
    lines.append(border)
    return "\n".join(lines)


def process_csv(input_file, count=None):
    """Read CSV file and return headers + rows (optionally limited by count)."""
    try:
        with open(input_file, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.reader(file)
            all_rows = list(reader)
    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied while reading: {input_file}")
        sys.exit(1)
    except csv.Error as err:
        print(f"Error: Invalid CSV content in '{input_file}': {err}")
        sys.exit(1)

    if not all_rows:
        print(f"Error: CSV file is empty: {input_file}")
        sys.exit(1)

    headers = all_rows[0]
    data_rows = all_rows[1:]

    if count is not None:
        data_rows = data_rows[:count]

    return headers, data_rows


def main():
    if len(sys.argv) < 2:
        print("Error: No input file specified!")
        print(f"Run: python3 {sys.argv[0]} --help")
        sys.exit(1)

    args = parse_args(sys.argv)

    if not args["input_file"]:
        print("Error: No input file specified!")
        print(f"Run: python3 {sys.argv[0]} --help")
        sys.exit(1)

    headers, rows = process_csv(args["input_file"], args["count"])
    table = _build_table(headers, rows)

    # Display parsed results
    print("=" * 50)
    print("  PARSED ARGUMENTS")
    print("=" * 50)
    print(f"\n  Input file: {args['input_file']}")
    print(f"  Output:     {args['output'] or '(stdout)'}")
    print(f"  Verbose:    {args['verbose']}")
    print(f"  Count:      {args['count'] or '(all lines)'}")
    print(f"  Rows shown: {len(rows)}")

    if args["verbose"]:
        print(f"\n  [VERBOSE] Raw sys.argv: {sys.argv}")
        print(f"  [VERBOSE] Total args: {len(sys.argv)}")

    print(f"\n  CSV Table from: {args['input_file']}")
    print(table)

    if args["output"]:
        try:
            with open(args["output"], "w", encoding="utf-8") as out_file:
                out_file.write(table + "\n")
            print(f"\n  Saved table output to: {args['output']}")
        except OSError as err:
            print(f"\n  Error: Could not write to output file '{args['output']}': {err}")
            sys.exit(1)

    print("=" * 50)


if __name__ == "__main__":
    main()
