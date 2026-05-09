"""
The print() Function Parameters — sep, end, file, flush
=========================================================
Run: python3 01_print_function_params.py

Demonstrates:
- Multiple arguments in print()
- sep parameter (separator between arguments)
- end parameter (what prints at the end)
- file parameter (print to a file)
- flush parameter (force immediate output)
- Printing to stderr
- Unpacking lists with *
"""

import sys
from datetime import datetime

# =============================================================================
# MULTIPLE ARGUMENTS (comma-separated)
# =============================================================================
print("=" * 70)
print("  print() FUNCTION PARAMETERS")
print("=" * 70)

name = "Vikram"
age = 25
city = "Hyderabad"
print("\n--- Multiple arguments ---")
print("Name:", name, "Age:", age, "City:", city)

# =============================================================================
# sep PARAMETER: separator between arguments
# =============================================================================
print("\n--- sep parameter ---")
print("2024", "01", "15", sep="-")          # 2024-01-15
print("usr", "local", "bin", sep="/")        # usr/local/bin
print("A", "B", "C", "D", sep=" -> ")       # A -> B -> C -> D
print("192", "168", "1", "1", sep=".")       # 192.168.1.1
print("one", "two", "three", sep="\n  ")     # Each on new line

# =============================================================================
# end PARAMETER: what to print at the end
# =============================================================================
print("\n--- end parameter ---")
print("Loading", end="...")
print("Done!")  # Same line: Loading...Done!

print("Item 1", end=", ")
print("Item 2", end=", ")
print("Item 3")  # Item 1, Item 2, Item 3

# Countdown on one line
print("Countdown: ", end="")
for i in range(5, 0, -1):
    print(i, end=" ")
print("GO!")

# =============================================================================
# file PARAMETER: print to a file
# =============================================================================
print("\n--- file parameter ---")
with open("/tmp/print_demo_log.txt", "w") as log_file:
    print("This goes to the log file", file=log_file)
    print("Timestamp:", datetime.now(), file=log_file)
print("Written to /tmp/print_demo_log.txt")

# Print to stderr (for error messages)
print("This is an error message!", file=sys.stderr)
print("(The line above went to stderr)")

# =============================================================================
# flush PARAMETER: force immediate output
# =============================================================================
print("\n--- flush parameter ---")
print("Processing", end="", flush=True)
for i in range(5):
    print(".", end="", flush=True)
print(" Complete!")

print("  (flush=True ensures dots appear immediately, not buffered)")

# =============================================================================
# UNPACKING WITH * OPERATOR
# =============================================================================
print("\n--- Unpacking a list with * ---")
fruits = ["apple", "banana", "cherry", "date"]
print("Unpacked:", *fruits)
print("Joined:", *fruits, sep=", ")
print("Path:", *["usr", "local", "bin"], sep="/")

numbers = list(range(1, 11))
print("Numbers:", *numbers, sep=" | ")

print("\n" + "=" * 70)
