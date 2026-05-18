"""
sys.argv Basics — Understanding Command Line Arguments
=======================================================
Run: python3 01_sys_argv_basics.py hello world 42

sys.argv is a list that contains all command line arguments.
- sys.argv[0] is always the script name
- sys.argv[1:] contains the actual arguments
- ALL values are strings (you must cast them yourself)
"""

import sys

# =============================================================================
# SECTION 1: INSPECTING sys.argv
# =============================================================================
print("=" * 60)
print("  INSPECTING sys.argv")
print("=" * 60)

print(f"\n  sys.argv type: {type(sys.argv)}")
print(f"  Total arguments (including script name): {len(sys.argv)}")
print(f"  Script name: {sys.argv[0]}")
print(f"  All arguments: {sys.argv}")
print(f"  User arguments only: {sys.argv[1:]}")

# =============================================================================
# SECTION 2: ALL ARGUMENTS ARE STRINGS
# =============================================================================
print("\n" + "=" * 60)
print("  ALL ARGUMENTS ARE STRINGS")
print("=" * 60)

print("\n  Each argument and its type:")
for i, arg in enumerate(sys.argv):
    print(f"    sys.argv[{i}] = {arg!r:<25} type = {type(arg).__name__}")

# =============================================================================
# SECTION 3: ACCESSING INDIVIDUAL ARGUMENTS
# =============================================================================
print("\n" + "=" * 60)
print("  ACCESSING INDIVIDUAL ARGUMENTS")
print("=" * 60)

if len(sys.argv) > 1:
    print(f"\n  First argument:  {sys.argv[1]}")
    if len(sys.argv) > 2:
        print(f"  Second argument: {sys.argv[2]}")
    if len(sys.argv) > 3:
        print(f"  Third argument:  {sys.argv[3]}")
else:
    print("\n  No arguments provided!")
    print("  Try: python3 01_sys_argv_basics.py hello world 42")

# =============================================================================
# SECTION 4: TYPE CASTING ARGUMENTS
# =============================================================================
print("\n" + "=" * 60)
print("  TYPE CASTING ARGUMENTS")
print("=" * 60)

print("\n  Attempting to cast arguments to numbers:")
for arg in sys.argv[1:]:
    try:
        as_int = int(arg)
        print(f"    '{arg}' -> int({as_int})")
    except ValueError:
        try:
            as_float = float(arg)
            print(f"    '{arg}' -> float({as_float})")
        except ValueError:
            print(f"    '{arg}' -> remains a string (can't convert)")

# =============================================================================
# SECTION 5: ARGUMENT COUNT
# =============================================================================
print("\n" + "=" * 60)
print("  ARGUMENT COUNT")
print("=" * 60)

arg_count = len(sys.argv) - 1  # Exclude script name
print(f"\n  You passed {arg_count} argument(s)")

if arg_count == 0:
    print("  Hint: Try running with some arguments!")
    print("  Example: python3 01_sys_argv_basics.py apple banana cherry")

print("\n" + "=" * 60)
