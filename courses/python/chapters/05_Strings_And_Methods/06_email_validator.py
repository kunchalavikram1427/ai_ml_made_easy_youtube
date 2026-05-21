import getpass

SUPPORTED_DOMAINS = [
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "hotmail.com",
    "icloud.com"
]


def validate_email(email):
    """Basic email validation using string methods."""
    email = email.strip()

    # Check for exactly one @
    if email.count('@') != 1:
        return False, "Must contain @ symbol"

    # Split into username and domain parts
    username, domain = email.split('@')

    # Check username part
    if not username:
        return False, "Username (before @) cannot be empty"
    if username.startswith('.') or username.endswith('.'):
        return False, "Username cannot start or end with a dot"

    # Check domain part
    if not domain:
        return False, "Domain part (after @) cannot be empty"
    if '.' not in domain:
        return False, "Domain must contain at least one dot"
    if domain.startswith('.') or domain.endswith('.'):
        return False, "Domain cannot start or end with a dot"

    # Check domain extension
    extension = domain.split('.')[-1]
    if len(extension) < 2:
        return False, "Domain extension must be at least 2 characters"
    if not extension.isalpha():
        return False, "Domain extension must contain only letters"

    # Check if domain is supported
    if domain.lower() not in SUPPORTED_DOMAINS:
        supported_list = ", ".join(SUPPORTED_DOMAINS)
        return False, f"Domain '{domain}' is not supported. Supported domains: {supported_list}"

    return True, "Valid email format"


def login():
    """Simple login that validates email and accepts any password."""
    print("=" * 40)
    print("       EMAIL LOGIN SYSTEM")
    print("=" * 40)
    # Get email input
    email = input("\nEnter your email: ")

    # Validate email
    is_valid, message = validate_email(email)

    if not is_valid:
        print(f"\n  Login FAILED: {message}")
        return

    # Accept any password (dummy) - hidden input
    password = getpass.getpass("Enter your password: ")

    if not password:
        print("\n  Login FAILED: Password cannot be empty")
        return

    username = email.split('@')[0]
    print(f"\n  Login SUCCESSFUL!")
    print(f"  Welcome, {username}")


if __name__ == "__main__":
    login()
