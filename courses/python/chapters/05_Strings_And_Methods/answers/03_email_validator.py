"""
Exercise 3 Solution: Email Validator - Mini-Project (Intermediate)
===================================================================
Run: python3 03_email_validator.py

Demonstrates:
- String methods: strip(), count(), split(), startswith(), endswith()
- String membership testing: 'in' operator
- isalpha(), isdigit(), isalnum() validation
- getpass module for password input
- Multi-step validation logic
"""

import getpass


SUPPORTED_DOMAINS = [
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "hotmail.com",
    "icloud.com",
]


def validate_email(email):
    """
    Validate an email address using string methods.

    Checks:
    1. Contains exactly one @ symbol
    2. Username (before @) is not empty, doesn't start/end with dot
    3. Domain (after @) is not empty, contains at least one dot
    4. Domain extension is at least 2 chars and all letters
    5. Domain is in the supported list

    Returns:
        tuple: (is_valid: bool, message: str)
    """
    email = email.strip()

    # Check for empty input
    if not email:
        return False, "Email cannot be empty"

    # Check for exactly one @
    if email.count("@") != 1:
        return False, "Email must contain exactly one @ symbol"

    # Split into username and domain
    username, domain = email.split("@")

    # ── Validate username ────────────────────────────────
    if not username:
        return False, "Username (before @) cannot be empty"

    if username.startswith(".") or username.endswith("."):
        return False, "Username cannot start or end with a dot"

    if ".." in username:
        return False, "Username cannot contain consecutive dots"

    # Check for spaces in username
    if " " in username:
        return False, "Username cannot contain spaces"

    # ── Validate domain ──────────────────────────────────
    if not domain:
        return False, "Domain (after @) cannot be empty"

    if "." not in domain:
        return False, "Domain must contain at least one dot"

    if domain.startswith(".") or domain.endswith("."):
        return False, "Domain cannot start or end with a dot"

    if " " in domain:
        return False, "Domain cannot contain spaces"

    # Check domain extension
    extension = domain.split(".")[-1]
    if len(extension) < 2:
        return False, "Domain extension must be at least 2 characters"

    if not extension.isalpha():
        return False, "Domain extension must contain only letters"

    # ── Check if domain is supported ─────────────────────
    if domain.lower() not in SUPPORTED_DOMAINS:
        supported_list = ", ".join(SUPPORTED_DOMAINS)
        return False, f"Domain '{domain}' not supported. Supported: {supported_list}"

    return True, "Valid email format"


def validate_password(password):
    """
    Basic password validation.

    Returns:
        tuple: (is_valid: bool, message: str)
    """
    if not password:
        return False, "Password cannot be empty"

    if len(password) < 6:
        return False, "Password must be at least 6 characters"

    return True, "Valid password"


def login():
    """
    Email login system with validation.

    Flow:
    1. Get email from user
    2. Validate email format
    3. Check domain support
    4. Get password
    5. Display result
    """
    print("=" * 45)
    print("       EMAIL LOGIN SYSTEM")
    print("=" * 45)
    print(f"  Supported domains: {', '.join(SUPPORTED_DOMAINS)}")

    # Get email input
    email = input("\n  Enter your email: ").strip()

    # Validate email
    is_valid, message = validate_email(email)

    if not is_valid:
        print(f"\n  Login FAILED!")
        print(f"  Reason: {message}")
        return

    print(f"  Email format: Valid")

    # Get password (hidden input)
    try:
        password = getpass.getpass("  Enter your password: ")
    except (EOFError, KeyboardInterrupt):
        print("\n  Login cancelled.")
        return

    # Validate password
    pw_valid, pw_message = validate_password(password)

    if not pw_valid:
        print(f"\n  Login FAILED!")
        print(f"  Reason: {pw_message}")
        return

    # Login successful
    username = email.split("@")[0]
    domain = email.split("@")[1]

    print(f"\n  {'─' * 35}")
    print(f"  Login SUCCESSFUL!")
    print(f"  Welcome, {username}")
    print(f"  Domain: {domain}")
    print(f"  {'─' * 35}")


def run_tests():
    """Run validation tests to demonstrate functionality."""
    print("\n" + "=" * 45)
    print("    EMAIL VALIDATION TESTS")
    print("=" * 45)

    test_cases = [
        ("vikram@gmail.com", True),
        ("user@outlook.com", True),
        ("test.user@yahoo.com", True),
        ("", False),
        ("no-at-sign.com", False),
        ("two@@signs.com", False),
        ("@gmail.com", False),
        ("user@", False),
        (".startdot@gmail.com", False),
        ("enddot.@gmail.com", False),
        ("user@unsupported.com", False),
        ("user@gmail", False),
        ("user @gmail.com", False),
        ("user@.com", False),
        ("user@domain.c", False),
        ("user@domain.123", False),
    ]

    passed = 0
    total = len(test_cases)

    for email, expected_valid in test_cases:
        is_valid, message = validate_email(email)
        status = "PASS" if is_valid == expected_valid else "FAIL"
        if status == "PASS":
            passed += 1

        display_email = email if email else "(empty)"
        icon = "  " if status == "PASS" else "  "
        print(f"  {icon} {display_email:<30} -> {message}")

    print(f"\n  Results: {passed}/{total} tests passed")


# Run the program
if __name__ == "__main__":
    # Run tests first to demonstrate validation
    run_tests()

    # Then run the interactive login
    print()
    login()
