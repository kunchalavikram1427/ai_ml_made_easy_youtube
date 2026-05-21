"""
Password Generator & Strength Checker
=======================================
Run: python3 password_generator.py

Features:
- Generate passwords with customizable character sets
- Adjustable length
- Password strength analysis
- Generate multiple passwords at once
- Copy-friendly output
- Uses only standard library (string, random, secrets)
"""

import string
import secrets

# ============================================================
# PASSWORD GENERATION
# ============================================================

# Character pools
LOWERCASE = string.ascii_lowercase    # abcdefghijklmnopqrstuvwxyz
UPPERCASE = string.ascii_uppercase    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
DIGITS = string.digits                # 0123456789
SPECIAL = string.punctuation          # !@#$%^&*()_+-=[]{}|;':",.<>?/`~


def generate_password(length=16, use_upper=True, use_lower=True,
                      use_digits=True, use_special=True):
    """
    Generate a cryptographically secure random password.

    Uses secrets module (not random!) for security.
    Ensures at least one character from each selected category.
    """
    # Build character pool
    pool = ""
    required_chars = []

    if use_lower:
        pool += LOWERCASE
        required_chars.append(secrets.choice(LOWERCASE))
    if use_upper:
        pool += UPPERCASE
        required_chars.append(secrets.choice(UPPERCASE))
    if use_digits:
        pool += DIGITS
        required_chars.append(secrets.choice(DIGITS))
    if use_special:
        pool += SPECIAL
        required_chars.append(secrets.choice(SPECIAL))

    if not pool:
        return "Error: Must select at least one character type!"

    if length < len(required_chars):
        length = len(required_chars)

    # Fill remaining length with random choices from pool
    remaining = length - len(required_chars)
    password_chars = required_chars + [secrets.choice(pool) for _ in range(remaining)]

    # Shuffle to avoid predictable positions
    # Convert to list, shuffle using Fisher-Yates via secrets
    password_list = list(password_chars)
    for i in range(len(password_list) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_list[i], password_list[j] = password_list[j], password_list[i]

    return "".join(password_list)


# ============================================================
# PASSWORD STRENGTH CHECKER
# ============================================================

def check_strength(password):
    """
    Analyze password strength and return a score with feedback.

    Scoring:
    - Length points (up to 4)
    - Character variety (up to 4)
    - Bonus for no common patterns (up to 2)
    """
    score = 0
    feedback = []

    # Length scoring
    length = len(password)
    if length >= 16:
        score += 4
        feedback.append("✅ Excellent length (16+)")
    elif length >= 12:
        score += 3
        feedback.append("✅ Good length (12+)")
    elif length >= 8:
        score += 2
        feedback.append("⚠️  Acceptable length (8+)")
    else:
        score += 1
        feedback.append("❌ Too short (< 8 characters)")

    # Character variety
    has_lower = any(c in LOWERCASE for c in password)
    has_upper = any(c in UPPERCASE for c in password)
    has_digit = any(c in DIGITS for c in password)
    has_special = any(c in SPECIAL for c in password)

    variety = sum([has_lower, has_upper, has_digit, has_special])
    score += variety

    if variety == 4:
        feedback.append("✅ Uses all character types")
    elif variety == 3:
        feedback.append("⚠️  Missing one character type")
    else:
        feedback.append("❌ Low character variety")

    # Pattern checks
    common_patterns = ["123", "abc", "qwerty", "password", "111", "aaa"]
    has_pattern = any(p in password.lower() for p in common_patterns)
    if not has_pattern:
        score += 1
        feedback.append("✅ No common patterns detected")
    else:
        feedback.append("❌ Contains common patterns")

    # Repeated characters
    max_repeat = max(password.count(c) for c in set(password))
    if max_repeat <= 2:
        score += 1
        feedback.append("✅ Good character distribution")
    else:
        feedback.append("⚠️  Some characters repeat often")

    # Determine strength label
    if score >= 9:
        strength = "🟢 VERY STRONG"
    elif score >= 7:
        strength = "🟢 STRONG"
    elif score >= 5:
        strength = "🟡 MODERATE"
    elif score >= 3:
        strength = "🟠 WEAK"
    else:
        strength = "🔴 VERY WEAK"

    return score, strength, feedback


def display_strength(password):
    """Display a visual strength analysis."""
    score, strength, feedback = check_strength(password)

    print(f"\n  Password: {password}")
    print(f"  Length:   {len(password)} characters")
    print(f"  Strength: {strength} ({score}/10)")
    print(f"  {'─' * 40}")

    # Visual bar
    filled = int((score / 10) * 20)
    bar = "█" * filled + "░" * (20 - filled)
    print(f"  [{bar}] {score}/10")

    print(f"\n  Analysis:")
    for item in feedback:
        print(f"    {item}")


# ============================================================
# INTERACTIVE MENU
# ============================================================

def generate_menu():
    """Interactive password generation with options."""
    print("\n┌──────────────────────────────────────────┐")
    print("│  🔐 GENERATE PASSWORD                    │")
    print("└──────────────────────────────────────────┘")

    try:
        length = int(input("\n  Length (default 16): ") or "16")
        count = int(input("  How many passwords? (default 1): ") or "1")

        print("\n  Include character types (y/n):")
        use_upper = input("    Uppercase [A-Z]? (y/n, default y): ").lower() != 'n'
        use_lower = input("    Lowercase [a-z]? (y/n, default y): ").lower() != 'n'
        use_digits = input("    Digits [0-9]? (y/n, default y): ").lower() != 'n'
        use_special = input("    Special [!@#$...]? (y/n, default y): ").lower() != 'n'

        print(f"\n  {'─' * 45}")
        print(f"  Generated Password{'s' if count > 1 else ''}:\n")

        for i in range(count):
            pw = generate_password(length, use_upper, use_lower, use_digits, use_special)
            score, strength, _ = check_strength(pw)
            print(f"    {i+1}. {pw}  {strength}")

        print(f"\n  {'─' * 45}")
        print(f"  💡 Tip: Use secrets module (not random) for security!")

    except ValueError:
        print("  ❌ Invalid input! Please enter numbers.")


def check_menu():
    """Check strength of a user-provided password."""
    print("\n┌──────────────────────────────────────────┐")
    print("│  🔍 CHECK PASSWORD STRENGTH              │")
    print("└──────────────────────────────────────────┘")

    password = input("\n  Enter password to check: ")
    if password:
        display_strength(password)


def quick_generate():
    """Generate a password instantly with defaults."""
    pw = generate_password(length=20)
    print(f"\n  🎲 Quick password: {pw}")
    display_strength(pw)


def main():
    """Main application loop."""
    print("\n" + "=" * 50)
    print("  🔐 PASSWORD GENERATOR & STRENGTH CHECKER")
    print("=" * 50)
    print("  Using Python's string module + secrets module")

    while True:
        print(f"""
  ┌────────────────────────────────┐
  │  [1] Generate Password(s)     │
  │  [2] Check Password Strength  │
  │  [3] Quick Generate (20 char) │
  │  [0] Exit                     │
  └────────────────────────────────┘""")

        choice = input("\n  Choose: ").strip()

        if choice == '1':
            generate_menu()
        elif choice == '2':
            check_menu()
        elif choice == '3':
            quick_generate()
        elif choice == '0':
            print("\n  👋 Stay secure! Never reuse passwords!")
            break
        else:
            print("  ❌ Invalid choice.")


if __name__ == "__main__":
    main()
