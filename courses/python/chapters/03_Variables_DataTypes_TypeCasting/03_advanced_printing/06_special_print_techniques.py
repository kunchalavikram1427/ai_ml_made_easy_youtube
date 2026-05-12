"""
Special Print Techniques — Colors, Tables, Progress Bars
==========================================================
Run: python3 06_special_print_techniques.py

Demonstrates:
- ANSI color codes for terminal output
- Formatted tabular output
- Pretty printing with pprint
- Progress bar in terminal
- Logging-style output
"""

import sys
from datetime import datetime
from pprint import pprint

# =============================================================================
# ANSI COLOR CODES
# =============================================================================
print("=" * 70)
print("  SPECIAL PRINT TECHNIQUES")
print("=" * 70)

print("\n--- ANSI Color Codes ---")
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

print(f"  {RED}Red text{RESET}")
print(f"  {GREEN}Green text{RESET}")
print(f"  {YELLOW}Yellow text{RESET}")
print(f"  {BLUE}Blue text{RESET}")
print(f"  {MAGENTA}Magenta text{RESET}")
print(f"  {CYAN}Cyan text{RESET}")
print(f"  {BOLD}Bold text{RESET}")
print(f"  {DIM}Dim text{RESET}")
print(f"  {UNDERLINE}Underlined text{RESET}")
print(f"  {BOLD}{BLUE}Bold Blue{RESET}")

# Practical usage
print(f"\n--- Practical Color Usage ---")
print(f"  {GREEN}[PASS]{RESET} Test 1: User authentication")
print(f"  {GREEN}[PASS]{RESET} Test 2: Database connection")
print(f"  {RED}[FAIL]{RESET} Test 3: API rate limiting")
print(f"  {YELLOW}[WARN]{RESET} Test 4: Deprecation warning")
print(f"  {BOLD}{BLUE}[INFO]{RESET} All tests complete: 2 passed, 1 failed, 1 warning")

# =============================================================================
# TABULAR OUTPUT
# =============================================================================
print(f"\n--- Tabular Output ---")
header = f"{'Name':<15}{'Age':>5}{'City':<15}{'GPA':>6}"
print(header)
print("-" * len(header))

data = [
    ("Vikram", 25, "Hyderabad", 3.85),
    ("Alice", 22, "Bangalore", 3.92),
    ("Bob", 28, "Mumbai", 3.45),
    ("Charlie", 24, "Delhi", 3.78),
]
for name, age, city, gpa in data:
    print(f"{name:<15}{age:>5}{city:<15}{gpa:>6.2f}")

# Another table style with borders
print(f"\n--- Bordered Table ---")
print(f"+{'-'*14}+{'-'*7}+{'-'*14}+{'-'*8}+")
print(f"| {'Name':<12} | {'Age':>5} | {'City':<12} | {'GPA':>6} |")
print(f"+{'='*14}+{'='*7}+{'='*14}+{'='*8}+")
for name, age, city, gpa in data:
    print(f"| {name:<12} | {age:>5} | {city:<12} | {gpa:>6.2f} |")
print(f"+{'-'*14}+{'-'*7}+{'-'*14}+{'-'*8}+")

# =============================================================================
# PRETTY PRINTING (pprint)
# =============================================================================

# pprint is a built-in module used to display complex data structures (like dictionaries, lists, JSON-like objects) in a more readable, well-formatted way.

print(f"\n--- Pretty Printing (pprint) ---")
complex_data = {
    "name": "Vikram",
    "skills": ["Python", "JavaScript", "Rust", "Go"],
    "experience": {
        "company": "Tech Corp",
        "years": 3,
        "projects": ["API Gateway", "ML Pipeline", "CLI Tools"]
    }
}

print("Regular print:")
print(f"  {complex_data}")
print("\nPretty print:")
pprint(complex_data, width=50, indent=2)

# =============================================================================
# PROGRESS BAR
# =============================================================================
from time import sleep
print(f"\n--- Progress Bar Demo ---")
total = 30
for i in range(total + 1):
    percent = (i / total) * 100
    filled = int(i * 30 / total)
    bar = "█" * filled + "░" * (30 - filled)
    sleep(0.1)
    print(f"\r  [{bar}] {percent:5.1f}%", end="", flush=True)
print()  # Final newline

# Simple hash-style progress bar
print("  Simple style:")
total = 20
for i in range(total + 1):
    percent = (i / total) * 100
    bar = "#" * i + "." * (total - i)
    sleep(0.1)
    print(f"\r  [{bar}] {percent:.0f}%", end="", flush=True)
print()

# =============================================================================
# LOGGING-STYLE OUTPUT
# =============================================================================
print(f"\n--- Logging-style Output ---")


def log(level, message):
    """Simple colored logging function."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    colors = {"INFO": GREEN, "WARN": YELLOW, "ERROR": RED, "DEBUG": CYAN}
    color = colors.get(level, RESET)
    print(f"  {DIM}{timestamp}{RESET} {color}[{level:>5}]{RESET} {message}")


log("INFO", "Application started")
log("INFO", "Connected to database")
log("WARN", "Memory usage at 80%")
log("ERROR", "Connection timeout after 30s")
log("DEBUG", "Request payload: {user_id: 42}")

# =============================================================================
# sys.stdout.write() — Low-level alternative
# =============================================================================
print(f"\n--- sys.stdout.write() ---")
sys.stdout.write("  This uses sys.stdout.write()")
sys.stdout.write(" — no newline added!\n")
sys.stdout.write(f"  Character count returned: {sys.stdout.write('')}\n")

print("\n" + "=" * 70)
