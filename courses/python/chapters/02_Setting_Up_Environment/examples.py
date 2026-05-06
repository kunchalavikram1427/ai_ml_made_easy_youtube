"""
Video 02: Setting Up the Development Environment
=================================================
This file contains TWO parts:

Part 1: Your First Python Programs (hands-on coding!)
Part 2: Environment Verification Script (checks your setup)

Run it with:
    python3 examples.py

Or run individual sections in the Python REPL (interactive mode):
    python3
    >>> print("Hello, World!")
"""

import sys
import os
import platform
import subprocess
import importlib
from datetime import datetime


# ############################################################
# PART 1: YOUR FIRST PYTHON PROGRAMS
# ############################################################
# Now that your environment is set up, let's write some code!

# ============================================================
# SECTION 1: Hello, World!
# ============================================================
# Every programming journey begins with "Hello, World!"
# In Python, it's just ONE line:

print("Hello, World!")
print()  # Print a blank line for spacing

# ============================================================
# SECTION 2: Basic Arithmetic in Python
# ============================================================
# Python can be used as a powerful calculator right out of the box

print("=" * 50)
print("BASIC ARITHMETIC")
print("=" * 50)

print(f"Addition:        2 + 3 = {2 + 3}")
print(f"Subtraction:     10 - 4 = {10 - 4}")
print(f"Multiplication:  5 * 6 = {5 * 6}")
print(f"Division:        15 / 4 = {15 / 4}")        # True division (float)
print(f"Floor Division:  15 // 4 = {15 // 4}")      # Integer division
print(f"Modulus:         15 % 4 = {15 % 4}")        # Remainder
print(f"Exponent:        2 ** 10 = {2 ** 10}")      # 2 to the power of 10
print(f"Big numbers:     2 ** 100 = {2 ** 100}")    # Python handles huge numbers!
print()

# ============================================================
# SECTION 3: Python Version & System Info
# ============================================================
# Let's check what version of Python we're running

print("=" * 50)
print("SYSTEM INFORMATION")
print("=" * 50)

print(f"Python Version: {sys.version}")
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")
print()

# ============================================================
# SECTION 4: The Zen of Python
# ============================================================
# Uncomment the line below to see Python's guiding philosophy
# (It prints a lot of text, so we keep it commented by default)

# import this

# Instead, here are the first few principles:
print("=" * 50)
print("THE ZEN OF PYTHON (selected)")
print("=" * 50)
print("Beautiful is better than ugly.")
print("Explicit is better than implicit.")
print("Simple is better than complex.")
print("Readability counts.")
print("(Run 'import this' in the REPL to see all 19 principles!)")
print()

# ============================================================
# SECTION 5: A Taste of Python's Readability & Power
# ============================================================
# These examples show WHY Python is loved for its elegance

print("=" * 50)
print("PYTHON'S POWER & READABILITY")
print("=" * 50)

# List comprehension: squares of even numbers from 1 to 20
even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(f"Squares of even numbers (1-20): {even_squares}")

# Swap two variables — no temp variable needed!
a, b = 1, 2
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")

# String multiplication
print("Python! " * 3)

# Multi-line strings with triple quotes
poem = """
    Roses are red,
    Violets are blue,
    Python is awesome,
    And so are you!
"""
print(poem)

# Check if something is in a list (reads like English!)
fruits = ["apple", "banana", "cherry", "mango"]
print(f"Is 'mango' in our fruits? {'mango' in fruits}")
print(f"Is 'grape' in our fruits? {'grape' in fruits}")

print()
print("=" * 50)
print("Great! Your first programs are working!")
print("Now let's verify your full environment setup below...")
print("=" * 50)
print()


# ############################################################
# PART 2: ENVIRONMENT VERIFICATION
# ############################################################
# This section checks that your development environment is
# properly configured for the rest of the course.


def print_header(title):
    """Print a formatted section header."""
    print()
    print("=" * 60)
    print(f"  {title}")
    print("=" * 60)


def print_check(label, status, detail=""):
    """Print a formatted check result."""
    icon = "✅" if status else "❌"
    msg = f"  {icon} {label}"
    if detail:
        msg += f" → {detail}"
    print(msg)


def check_python_version():
    """Check Python version is 3.8 or higher."""
    print_header("Python Version Check")
    version = sys.version
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro

    is_valid = major == 3 and minor >= 8
    print_check(
        "Python version",
        is_valid,
        f"{major}.{minor}.{micro} {'(Good!)' if is_valid else '(Need 3.8+)'}"
    )
    print(f"  Full version string: {version}")
    return is_valid


def check_pip_version():
    """Check that pip is installed and accessible."""
    print_header("Pip Version Check")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            pip_info = result.stdout.strip()
            print_check("pip installed", True, pip_info.split("(")[0].strip())
            return True
        else:
            print_check("pip installed", False, "pip not found")
            return False
    except Exception as e:
        print_check("pip installed", False, str(e))
        return False


def check_jupyter():
    """Check if Jupyter is installed."""
    print_header("Jupyter Installation Check")
    jupyter_packages = {
        "jupyter": "Jupyter (meta-package)",
        "jupyterlab": "JupyterLab (modern interface)",
        "notebook": "Jupyter Notebook (classic)",
        "ipykernel": "IPython Kernel",
    }

    any_installed = False
    for package, description in jupyter_packages.items():
        try:
            importlib.import_module(package.replace("-", "_"))
            print_check(description, True, "installed")
            any_installed = True
        except ImportError:
            print_check(description, False, "not installed")

    if not any_installed:
        print()
        print("  💡 To install Jupyter, run:")
        print("     pip3 install jupyterlab")

    return any_installed


def check_common_packages():
    """Check if commonly used packages are available."""
    print_header("Common Package Check")

    packages = {
        "numpy": "NumPy (numerical computing)",
        "pandas": "Pandas (data manipulation)",
        "matplotlib": "Matplotlib (plotting)",
        "requests": "Requests (HTTP library)",
        "scipy": "SciPy (scientific computing)",
        "sklearn": "Scikit-learn (machine learning)",
        "seaborn": "Seaborn (statistical visualization)",
        "PIL": "Pillow (image processing)",
    }

    installed_count = 0
    for module_name, description in packages.items():
        try:
            mod = importlib.import_module(module_name)
            version = getattr(mod, "__version__", "version unknown")
            print_check(description, True, f"v{version}")
            installed_count += 1
        except ImportError:
            print_check(description, False, "not installed (optional)")

    print()
    print(f"  📦 {installed_count}/{len(packages)} optional packages installed")
    if installed_count < len(packages):
        print("  💡 Install missing packages with: pip3 install numpy pandas matplotlib")

    return True  # These are optional, so always pass


def check_os_and_platform():
    """Check OS and platform information."""
    print_header("System Information")

    info = {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor() or "Unknown",
        "Platform": platform.platform(),
        "Hostname": platform.node(),
        "Python Implementation": platform.python_implementation(),
        "Python Compiler": platform.python_compiler(),
    }

    for label, value in info.items():
        print(f"  📋 {label}: {value}")

    return True


def check_environment_info():
    """Print environment information."""
    print_header("Environment Information")

    print(f"  📂 Current Directory: {os.getcwd()}")
    print(f"  🏠 Home Directory: {os.path.expanduser('~')}")
    print(f"  🐍 Python Executable: {sys.executable}")
    print(f"  📅 Current Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  💻 Python Path Entries: {len(sys.path)}")

    # Show virtual environment status
    venv = os.environ.get("VIRTUAL_ENV")
    conda = os.environ.get("CONDA_DEFAULT_ENV")

    if venv:
        print(f"  🔒 Virtual Environment: {venv}")
    elif conda:
        print(f"  🔒 Conda Environment: {conda}")
    else:
        print("  🌐 Environment: System Python (no virtual env active)")

    return True


def check_path_setup():
    """Verify PATH includes Python-related directories."""
    print_header("PATH Configuration Check")

    path_dirs = os.environ.get("PATH", "").split(os.pathsep)
    python_dir = os.path.dirname(sys.executable)

    # Check if Python's directory is in PATH
    python_in_path = any(
        os.path.normpath(d) == os.path.normpath(python_dir)
        for d in path_dirs
    )
    print_check(
        "Python directory in PATH",
        python_in_path,
        python_dir
    )

    # Check for common tool directories
    home = os.path.expanduser("~")
    important_paths = {
        "Local bin": os.path.join(home, ".local", "bin"),
        "User Scripts": os.path.join(home, "Library", "Python", "3.11", "bin"),
    }

    for label, path in important_paths.items():
        if os.path.exists(path):
            in_path = any(
                os.path.normpath(d) == os.path.normpath(path)
                for d in path_dirs
            )
            if in_path:
                print_check(f"{label} in PATH", True, path)

    print(f"\n  📂 Total directories in PATH: {len(path_dirs)}")
    return python_in_path


def list_installed_packages():
    """List a summary of installed packages."""
    print_header("Installed Packages Summary")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--format=columns"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            lines = result.stdout.strip().split("\n")
            # Skip header lines (Package, Version, ----, -----)
            packages = [l for l in lines[2:] if l.strip()]
            print(f"  📦 Total installed packages: {len(packages)}")
            print()
            print("  Top packages (first 15):")
            for pkg in packages[:15]:
                print(f"    • {pkg.strip()}")
            if len(packages) > 15:
                print(f"    ... and {len(packages) - 15} more")
        else:
            print("  ⚠️  Could not retrieve package list")
    except Exception as e:
        print(f"  ⚠️  Error listing packages: {e}")

    return True


def try_importing_key_packages():
    """Try importing key packages and report their status."""
    print_header("Key Package Import Test")

    key_packages = [
        ("json", "JSON (built-in)"),
        ("os", "OS interface (built-in)"),
        ("sys", "System (built-in)"),
        ("math", "Math (built-in)"),
        ("datetime", "DateTime (built-in)"),
        ("pathlib", "Pathlib (built-in)"),
        ("collections", "Collections (built-in)"),
        ("itertools", "Itertools (built-in)"),
        ("re", "Regex (built-in)"),
        ("typing", "Typing (built-in)"),
    ]

    all_passed = True
    for module_name, description in key_packages:
        try:
            importlib.import_module(module_name)
            print_check(description, True)
        except ImportError:
            print_check(description, False, "MISSING - this shouldn't happen!")
            all_passed = False

    return all_passed


def run_verification():
    """Run all environment checks."""
    print()
    print("🐍" * 30)
    print()
    print("   PYTHON ENVIRONMENT VERIFICATION SCRIPT")
    print("   Video 02: Setting Up the Development Environment")
    print()
    print("🐍" * 30)

    # Run all checks
    results = {
        "Python Version": check_python_version(),
        "Pip Installation": check_pip_version(),
        "Jupyter Installation": check_jupyter(),
        "Common Packages": check_common_packages(),
        "OS & Platform": check_os_and_platform(),
        "Environment Info": check_environment_info(),
        "PATH Setup": check_path_setup(),
        "Key Imports": try_importing_key_packages(),
    }

    # List installed packages
    list_installed_packages()

    # Final summary
    print_header("FINAL RESULTS")
    all_passed = True
    for check_name, passed in results.items():
        print_check(check_name, passed)
        if not passed and check_name in ("Python Version", "Pip Installation"):
            all_passed = False

    print()
    if all_passed:
        print("  🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        print()
        print("  🎊 CONGRATULATIONS! Your Python setup is working! 🎊")
        print()
        print("  Your development environment is ready for the course.")
        print("  You can now proceed to Video 03: Variables & Data Types!")
        print()
        print("  🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
    else:
        print("  ⚠️  Some critical checks failed. Please review the issues above.")
        print("  Refer to Video 02 README.md for installation instructions.")

    print()
    print(f"  Script completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()


if __name__ == "__main__":
    run_verification()
