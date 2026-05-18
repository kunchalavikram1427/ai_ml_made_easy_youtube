"""
argparse File Processor — Types, Defaults, and Validation
===========================================================
Run: python3 05_argparse_file_processor.py input.txt
     python3 05_argparse_file_processor.py input.txt -o output.txt -n 50 --verbose
     python3 05_argparse_file_processor.py data.csv --format csv
     python3 05_argparse_file_processor.py --help

A more realistic example showing how argparse handles:
- Required vs optional arguments
- Type conversion (int, float)
- Default values with %(default)s in help
- Boolean flags
- String arguments with validation

Demonstrates:
- type= for automatic type casting
- default= for fallback values
- required=True for mandatory optional args
- action="store_true" for boolean flags
- Custom validation after parsing
"""

import argparse
import sys


def create_parser():
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Process text files with various options",
        epilog="Examples:\n"
               "  %(prog)s data.txt\n"
               "  %(prog)s data.txt -o result.txt -n 100 --verbose\n"
               "  %(prog)s log.csv --format csv",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Positional: input file (required)
    parser.add_argument(
        "input_file",
        help="Path to the input file to process"
    )

    # Optional: output file
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output file path (default: print to stdout)"
    )

    # Optional: number of lines (type=int handles casting)
    parser.add_argument(
        "-n", "--lines",
        type=int,
        default=0,
        help="Number of lines to process, 0 for all (default: %(default)s)"
    )

    # Optional: format
    parser.add_argument(
        "--format",
        choices=["text", "csv", "json"],
        default="text",
        help="Input file format (default: %(default)s)"
    )

    # Optional: separator for CSV
    parser.add_argument(
        "--separator",
        default=",",
        help="Column separator for CSV files (default: '%(default)s')"
    )

    # Boolean flags
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output with processing details"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without actually processing"
    )

    parser.add_argument(
        "--no-header",
        action="store_true",
        help="Skip the first line (treat as header)"
    )

    # Version
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0"
    )

    return parser


def validate_args(args):
    """Perform additional validation beyond what argparse handles."""
    if args.lines < 0:
        print(f"Error: --lines must be non-negative, got {args.lines}")
        sys.exit(1)

    if args.format == "csv" and args.separator == "":
        print("Error: --separator cannot be empty for CSV format")
        sys.exit(1)


def process_file(args):
    """Simulate file processing (for demo purposes)."""
    print("=" * 55)
    print("  FILE PROCESSOR")
    print("=" * 55)

    if args.dry_run:
        print("\n  [DRY RUN] — No actual processing will occur\n")

    if args.verbose:
        print("  Configuration:")
        print(f"    Input:     {args.input_file}")
        print(f"    Output:    {args.output or '(stdout)'}")
        print(f"    Format:    {args.format}")
        print(f"    Lines:     {args.lines or 'all'}")
        print(f"    Separator: {repr(args.separator)}")
        print(f"    No header: {args.no_header}")
        print(f"    Dry run:   {args.dry_run}")
        print()

    # Simulate processing steps
    steps = [
        f"Opening '{args.input_file}'",
        f"Parsing as {args.format.upper()} format",
    ]

    if args.no_header:
        steps.append("Skipping header row")
    if args.lines > 0:
        steps.append(f"Processing first {args.lines} lines")
    else:
        steps.append("Processing all lines")
    if args.output:
        steps.append(f"Writing results to '{args.output}'")
    else:
        steps.append("Printing results to stdout")

    prefix = "[DRY RUN] " if args.dry_run else ""
    for i, step in enumerate(steps, 1):
        print(f"  {prefix}Step {i}: {step}")

    print(f"\n  {'Would complete' if args.dry_run else 'Complete'}!")
    print("=" * 55)


def main():
    parser = create_parser()
    args = parser.parse_args()
    validate_args(args)
    process_file(args)


if __name__ == "__main__":
    main()
