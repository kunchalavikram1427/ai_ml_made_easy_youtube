# Command Line Arguments in Python

## Overview

Most real-world Python scripts don't just run in isolation — they accept input at the time of execution through **command line arguments**. Whether you're building automation scripts, data processing pipelines, or CLI tools, understanding how to parse and use command line arguments is essential. Python provides several approaches ranging from the simple `sys.argv` list to the powerful `argparse` module that auto-generates help messages and handles type checking.

In this lesson, we'll explore all the ways to handle command line arguments in Python, from basic to advanced, and learn when to use each approach.

## Learning Objectives

By the end of this lesson, you will be able to:

- Access command line arguments using `sys.argv`
- Understand the structure of `sys.argv` (script name + arguments)
- Build professional CLIs with `argparse` including help messages, types, and defaults
- Add positional arguments, optional flags, and mutually exclusive groups
- Choose the right approach based on your use case

## Prerequisites

- Comments in Python (annotating code)
- Variables and Typecasting (understanding types and casting)
- Advanced Printing (output formatting with f-strings)
- Inputs in Python (understanding user input)

## How to Run the Examples

```bash
cd courses/python/chapters/03_Variables_DataTypes_TypeCasting/05_command_line_arguments

python3 01_sys_argv_basics.py hello world 42
python3 02_sys_argv_adder.py 5 10 15 20
python3 03_sys_argv_flags.py --verbose data.csv --output result.txt
python3 04_argparse_basics.py Vikram -g "Good morning" --shout
python3 05_argparse_file_processor.py input.txt -o output.txt -n 50 --verbose
python3 06_argparse_choices.py --format json --level 2 --numbers 10 20 30
python3 07_argparse_subcommands.py commit -m "Initial commit"
```

Each script is standalone. Use `--help` with argparse scripts (04-07) to see auto-generated usage.

---

## Detailed Explanation

### 1. What Are Command Line Arguments?

Command line arguments are values passed to a script when you execute it from the terminal:

```bash
python3 script.py arg1 arg2 arg3
```

They allow your script to behave differently based on input **without** needing interactive prompts. This makes scripts automatable, composable, and suitable for pipelines.

```bash
# Examples of command line arguments in the real world:
python3 resize_images.py --width 800 --height 600 images/
python3 train_model.py --epochs 50 --learning-rate 0.001 data.csv
python3 deploy.py --env production --verbose
```

---

### 2. `sys.argv` — The Simplest Approach

The `sys` module provides `sys.argv`, a list containing command line arguments passed to the script:

```python
import sys

# sys.argv is a list of strings
print("Total arguments:", len(sys.argv))
print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
```

#### Running:
```bash
python3 greet.py Vikram 25
```

#### Output:
```
Total arguments: 3
Script name: greet.py
Arguments: ['Vikram', '25']
```

#### Key Facts About `sys.argv`:
- **`sys.argv[0]`** — Always the script name (or path)
- **`sys.argv[1:]`** — The actual arguments you passed
- **All values are strings** — you must cast to int/float yourself
- **No built-in validation** — you handle errors manually

#### Practical Example: Simple Adder

```python
import sys

if len(sys.argv) < 3:
    print("Usage: python3 add.py <num1> <num2>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print(f"{num1} + {num2} = {num1 + num2}")
except ValueError:
    print("Error: Both arguments must be numbers!")
    sys.exit(1)
```

```bash
python3 add.py 5 10
# Output: 5.0 + 10.0 = 15.0
```

---

### 3. `argparse` Module — The Recommended Approach

`argparse` is the most powerful and Pythonic way to handle command line arguments. It provides automatic help generation, type checking, default values, and clear error messages.

#### Basic Usage:

```python
import argparse

parser = argparse.ArgumentParser(description="A simple greeting program")
parser.add_argument("name", help="Name of the person to greet")
parser.add_argument("-g", "--greeting", default="Hello", help="Greeting to use (default: Hello)")

args = parser.parse_args()
print(f"{args.greeting}, {args.name}!")
```

```bash
python3 greet.py Vikram
# Output: Hello, Vikram!

python3 greet.py Vikram -g "Good morning"
# Output: Good morning, Vikram!

python3 greet.py --help
# Output:
# usage: greet.py [-h] [-g GREETING] name
#
# A simple greeting program
#
# positional arguments:
#   name                  Name of the person to greet
#
# options:
#   -h, --help            show this help message and exit
#   -g GREETING, --greeting GREETING
#                         Greeting to use (default: Hello)
```

#### Positional vs Optional Arguments:

```python
import argparse

parser = argparse.ArgumentParser(description="File processor")

# Positional arguments (required, no -- prefix)
parser.add_argument("filename", help="File to process")

# Optional arguments (use -- prefix)
parser.add_argument("-o", "--output", default="output.txt", help="Output filename")
parser.add_argument("-n", "--lines", type=int, default=10, help="Number of lines to process")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()

print(f"Processing: {args.filename}")
print(f"Output to: {args.output}")
print(f"Lines: {args.lines}")
print(f"Verbose: {args.verbose}")
```

```bash
python3 process.py data.csv -o results.json -n 50 --verbose
```

#### Argument Types and Choices:

```python
import argparse

parser = argparse.ArgumentParser(description="Image resizer")

parser.add_argument("image", help="Path to image file")
parser.add_argument("--width", type=int, required=True, help="Target width in pixels")
parser.add_argument("--height", type=int, required=True, help="Target height in pixels")
parser.add_argument("--format", choices=["png", "jpg", "webp"], default="png",
                    help="Output format (default: png)")
parser.add_argument("--quality", type=int, default=85,
                    help="Compression quality 1-100 (default: 85)")

args = parser.parse_args()
```

#### Boolean Flags:

```python
# store_true: flag is False by default, True when present
parser.add_argument("--verbose", action="store_true", help="Show detailed output")
parser.add_argument("--quiet", action="store_true", help="Suppress all output")

# store_false: flag is True by default, False when present
parser.add_argument("--no-color", action="store_false", dest="color",
                    help="Disable colored output")
```

#### Mutually Exclusive Groups:

```python
import argparse

parser = argparse.ArgumentParser(description="Output formatter")
group = parser.add_mutually_exclusive_group()
group.add_argument("--json", action="store_true", help="Output as JSON")
group.add_argument("--csv", action="store_true", help="Output as CSV")
group.add_argument("--table", action="store_true", help="Output as table")

args = parser.parse_args()
```

```bash
python3 format.py --json --csv
# Error: argument --csv: not allowed with argument --json
```

#### Multiple Values (nargs):

```python
import argparse

parser = argparse.ArgumentParser(description="Calculator")

# Accept exactly 2 numbers
parser.add_argument("numbers", type=float, nargs=2, help="Two numbers to operate on")

# Accept one or more files
parser.add_argument("--files", nargs="+", help="One or more files to process")

# Accept zero or more tags
parser.add_argument("--tags", nargs="*", default=[], help="Optional tags")

args = parser.parse_args()
```

---

### 4. Comparing the Approaches

| Feature | `sys.argv` | `argparse` |
|---------|-----------|------------|
| Complexity | Minimal | Medium |
| Help messages | Manual | Automatic |
| Type checking | Manual | Built-in |
| Default values | Manual | Built-in |
| Error handling | Manual | Built-in |
| Best for | Quick scripts | Production CLIs |

#### Rules of Thumb:
- **1-2 simple args** → `sys.argv`
- **Anything more complex** → `argparse` (recommended default)

---

### 5. Best Practices

```python
import argparse
import sys

def create_parser():
    """Create and return the argument parser."""
    parser = argparse.ArgumentParser(
        description="Process data files and generate reports",
        epilog="Example: %(prog)s data.csv --output report.pdf --verbose"
    )

    parser.add_argument("input_file", help="Path to input data file")
    parser.add_argument("-o", "--output", default="output.txt",
                        help="Output file path (default: %(default)s)")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable verbose logging")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.verbose:
        print(f"Processing: {args.input_file}")
        print(f"Output: {args.output}")

    # ... rest of your program logic


if __name__ == "__main__":
    main()
```

#### Best Practices Summary:
1. **Always provide `help` text** for every argument
2. **Use `type=`** to let argparse handle type conversion
3. **Set sensible `default` values** for optional arguments
4. **Use `%(default)s`** in help strings to show defaults automatically
5. **Wrap in `if __name__ == "__main__"`** so the script is importable
6. **Use `description` and `epilog`** for context in the help message
7. **Validate early, fail fast** — check arguments before doing work

---

## Code Examples

### Example 1: File Word Counter (sys.argv)

```python
"""
Count words in a file using sys.argv
Usage: python3 word_count.py <filename>
"""
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <filename>")
    sys.exit(1)

filename = sys.argv[1]
try:
    with open(filename, "r") as f:
        content = f.read()
    words = content.split()
    lines = content.count("\n")
    print(f"File: {filename}")
    print(f"Lines: {lines}")
    print(f"Words: {len(words)}")
    print(f"Characters: {len(content)}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found!")
    sys.exit(1)
```

### Example 2: Mini grep (argparse)

```python
"""
Search for patterns in files — a simplified grep
Usage: python3 mini_grep.py PATTERN FILE [--ignore-case] [--line-numbers]
"""
import argparse

def create_parser():
    parser = argparse.ArgumentParser(
        description="Search for a pattern in a file (mini grep)"
    )
    parser.add_argument("pattern", help="Text pattern to search for")
    parser.add_argument("file", help="File to search in")
    parser.add_argument("-i", "--ignore-case", action="store_true",
                        help="Case-insensitive search")
    parser.add_argument("-n", "--line-numbers", action="store_true",
                        help="Show line numbers")
    parser.add_argument("-c", "--count", action="store_true",
                        help="Only show count of matching lines")
    return parser

def search_file(filename, pattern, ignore_case, show_numbers):
    matches = []
    with open(filename, "r") as f:
        for i, line in enumerate(f, 1):
            check_line = line.lower() if ignore_case else line
            check_pattern = pattern.lower() if ignore_case else pattern
            if check_pattern in check_line:
                if show_numbers:
                    matches.append(f"{i}: {line.rstrip()}")
                else:
                    matches.append(line.rstrip())
    return matches

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    try:
        results = search_file(args.file, args.pattern,
                             args.ignore_case, args.line_numbers)
        if args.count:
            print(f"{len(results)} matches found")
        else:
            for line in results:
                print(line)
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found!")
```

---

## Exercises

### Exercise 1: Calculator CLI (Beginner)

**Objective:** Build a command line calculator using `sys.argv`.

**Instructions:**
1. Accept three arguments: `number1`, `operator`, `number2`
2. Support operators: `+`, `-`, `*`, `/`
3. Handle errors: wrong number of arguments, invalid numbers, division by zero
4. Print usage message if arguments are wrong

```bash
python3 calc.py 10 + 5    # Output: 15.0
python3 calc.py 10 / 0    # Output: Error: Division by zero!
```

---

### Exercise 2: File Renamer (Intermediate)

**Objective:** Build a batch file renamer using `argparse`.

**Instructions:**
1. Accept a directory path (positional)
2. Add `--prefix` option to add a prefix to filenames
3. Add `--suffix` option to add a suffix before the extension
4. Add `--dry-run` flag to show what would happen without actually renaming
5. Add `--extension` option to filter only specific file types

```bash
python3 renamer.py ./photos --prefix "vacation_" --extension .jpg --dry-run
```

---

### Exercise 3: Data Pipeline CLI (Advanced)

**Objective:** Build a data processing tool using argparse with subcommands.

**Instructions:**
1. Create subcommands: `load`, `transform`, `export`
2. `load` takes a filename and optional `--format` (csv, json)
3. `transform` takes operations like `--sort-by`, `--filter`, `--limit`
4. `export` takes output filename and `--format`
5. Add a `--verbose` flag that works across all subcommands

```bash
python3 pipeline.py load data.csv --format csv
python3 pipeline.py transform --sort-by name --limit 100
python3 pipeline.py export output.json --format json --verbose
```

---

## Resources & References

- **Python Official Docs — sys.argv:** https://docs.python.org/3/library/sys.html#sys.argv
- **Python Official Docs — argparse:** https://docs.python.org/3/library/argparse.html
- **Real Python — Command Line Interfaces:** https://realpython.com/command-line-interfaces-python-argparse/
- **GeeksforGeeks — Command Line Arguments in Python:** https://www.geeksforgeeks.org/python/command-line-arguments-in-python/

---

## Key Takeaways

1. **`sys.argv`** is a list of strings — `[0]` is the script name, `[1:]` are arguments
2. **All command line arguments are strings** — cast to int/float as needed
3. **`argparse` is the recommended approach** — auto-generates help, validates types, sets defaults
4. **Positional arguments** are required; **optional arguments** use `--` prefix
5. **`action="store_true"`** creates boolean flags (default False, True when present)
6. **Always validate arguments early** and provide clear error messages
7. **Use `if __name__ == "__main__"`** so scripts with argparse remain importable

---
