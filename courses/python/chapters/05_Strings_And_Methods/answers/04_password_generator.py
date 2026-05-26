"""
Exercise 4 Solution: Password Generator - Mini-Project (Advanced)
==================================================================
Run: python3 04_password_generator.py

Reference: Password Generator Short - https://youtube.com/shorts/BN6IBv6scrY

Demonstrates:
- String module: ascii_uppercase, ascii_lowercase, digits, punctuation
- random module: choice, shuffle, sample
- String iteration and character classification
- Strength checking algorithm (7-point scale)
- List to string conversion with join()
"""

import random
import string


def generate_password(length=12, use_upper=True, use_lower=True,
                      use_digits=True, use_special=True):
    """
    Generate a random password based on specified criteria.

    Args:
        length: Length of password (minimum 4)
        use_upper: Include uppercase letters
        use_lower: Include lowercase letters
        use_digits: Include digits
        use_special: Include special characters

    Returns:
        Generated password string
    """
    # Ensure minimum length
    length = max(length, 4)

    # Build character pool and required characters
    pool = ""
    required = []

    if use_upper:
        pool += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))

    if use_lower:
        pool += string.ascii_lowercase
        required.append(random.choice(string.ascii_lowercase))

    if use_digits:
        pool += string.digits
        required.append(random.choice(string.digits))

    if use_special:
        pool += string.punctuation
        required.append(random.choice(string.punctuation))

    # Must have at least one character type selected
    if not pool:
        pool = string.ascii_lowercase
        required.append(random.choice(string.ascii_lowercase))

    # Fill remaining length with random choices from the pool
    remaining_length = length - len(required)
    password_chars = required + [random.choice(pool) for _ in range(remaining_length)]

    # Shuffle to randomize position of required characters
    random.shuffle(password_chars)

    return "".join(password_chars)


def check_strength(password):
    """
    Check password strength and return rating.

    Criteria (7-point scale):
    - Length >= 8: +1 point
    - Length >= 12: +1 point
    - Has uppercase: +1 point
    - Has lowercase: +1 point
    - Has digits: +1 point
    - Has special chars: +1 point
    - No repeated characters (3+ in a row): +1 point

    Rating: 0-2 Weak, 3-4 Medium, 5-6 Strong, 7 Very Strong

    Returns:
        tuple: (score, max_score, rating, details)
    """
    score = 0
    details = []

    # Check length >= 8
    if len(password) >= 8:
        score += 1
        details.append("  Length >= 8")
    else:
        details.append("  Length < 8")

    # Check length >= 12
    if len(password) >= 12:
        score += 1
        details.append("  Length >= 12")
    else:
        details.append("  Length < 12")

    # Check for uppercase
    has_upper = any(c.isupper() for c in password)
    if has_upper:
        score += 1
        details.append("  Has uppercase")
    else:
        details.append("  No uppercase")

    # Check for lowercase
    has_lower = any(c.islower() for c in password)
    if has_lower:
        score += 1
        details.append("  Has lowercase")
    else:
        details.append("  No lowercase")

    # Check for digits
    has_digit = any(c.isdigit() for c in password)
    if has_digit:
        score += 1
        details.append("  Has digits")
    else:
        details.append("  No digits")

    # Check for special characters
    has_special = any(c in string.punctuation for c in password)
    if has_special:
        score += 1
        details.append("  Has special chars")
    else:
        details.append("  No special chars")

    # Check for repeated characters (3+ consecutive same char)
    has_repeats = False
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            has_repeats = True
            break

    if not has_repeats:
        score += 1
        details.append("  No 3+ repeated chars")
    else:
        details.append("  Has 3+ repeated chars")

    # Determine rating
    if score <= 2:
        rating = "WEAK"
    elif score <= 4:
        rating = "MEDIUM"
    elif score <= 6:
        rating = "STRONG"
    else:
        rating = "VERY STRONG"

    return score, 7, rating, details


def display_strength_bar(score, max_score, rating):
    """Display a visual strength indicator."""
    filled = int((score / max_score) * 12)
    empty = 12 - filled

    # Color-code the bar with different fill chars
    bar = "█" * filled + "░" * empty

    print(f"  Strength: [{bar}] {rating}")


def password_generator_app():
    """Main application loop for the password generator."""
    print("=" * 50)
    print("    SECURE PASSWORD GENERATOR")
    print("=" * 50)

    while True:
        # Get password length
        while True:
            length_input = input("\n  Enter password length (8-50): ").strip()
            if length_input.isdigit():
                length = int(length_input)
                if 8 <= length <= 50:
                    break
                else:
                    print("  Please enter a number between 8 and 50.")
            else:
                print("  Please enter a valid number.")

        # Get character type preferences
        print()
        use_upper = input("  Include uppercase? (y/n): ").strip().lower() != "n"
        use_lower = input("  Include lowercase? (y/n): ").strip().lower() != "n"
        use_digits = input("  Include digits? (y/n): ").strip().lower() != "n"
        use_special = input("  Include special characters? (y/n): ").strip().lower() != "n"

        # Ensure at least one type is selected
        if not any([use_upper, use_lower, use_digits, use_special]):
            print("\n  At least one character type required! Enabling lowercase.")
            use_lower = True

        # Ask how many passwords to generate
        count_input = input("\n  How many passwords to generate? (1-10): ").strip()
        count = int(count_input) if count_input.isdigit() and 1 <= int(count_input) <= 10 else 1

        # Generate and display passwords
        print(f"\n  {'─' * 44}")

        for i in range(count):
            password = generate_password(
                length=length,
                use_upper=use_upper,
                use_lower=use_lower,
                use_digits=use_digits,
                use_special=use_special,
            )

            score, max_score, rating, details = check_strength(password)

            if count > 1:
                print(f"\n  Password {i + 1}: {password}")
            else:
                print(f"\n  Generated Password: {password}")

            display_strength_bar(score, max_score, rating)

        # Show strength breakdown for the last password
        print(f"\n  --- Strength Breakdown (last password) ---")
        print(f"  Score: {score}/{max_score}")
        for detail in details:
            check_mark = "+" if not detail.strip().startswith("No") and not detail.strip().startswith("Has 3") and not detail.strip().startswith("Length <") else "-"
            print(f"    [{check_mark}] {detail.strip()}")

        print(f"  {'─' * 44}")

        # Generate another?
        again = input("\n  Generate another? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Goodbye! Stay secure!")
            break


# Run the app
if __name__ == "__main__":
    password_generator_app()
