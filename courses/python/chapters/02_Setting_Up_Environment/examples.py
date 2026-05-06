"""
Video 02: Setting Up the Development Environment
=================================================
Verify Your Setup Script

Run this script to check that your Python development environment
is properly configured. It checks Python version, pip, Jupyter,
common packages, OS info, and PATH setup.

Usage:
    python3 examples.py

Expected: All checks pass with a congratulations message at the end.
"""

import sys
import os
import platform
import subprocess
import importlib
from datetime import datetime


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


def main():
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
    main()
