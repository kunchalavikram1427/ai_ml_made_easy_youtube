"""
Virtual Environments & Package Managers - Interactive Guide
===========================================================
Run: python3 venv_and_package_managers.py

This script checks your current environment and available tools,
then provides personalized recommendations and commands.
"""

import sys
import os
import platform
import subprocess
import shutil
import sysconfig
from pathlib import Path


# ============================================================
# ANSI Colors for terminal output
# ============================================================
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def colored(text, color):
    """Apply color to text (disable on Windows without ANSI support)."""
    if os.name == "nt" and not os.environ.get("WT_SESSION"):
        return text
    return f"{color}{text}{Colors.END}"


def header(title):
    """Print a section header."""
    width = 60
    print("\n" + colored("=" * width, Colors.CYAN))
    print(colored(f"  {title}", Colors.BOLD + Colors.CYAN))
    print(colored("=" * width, Colors.CYAN))


def subheader(title):
    """Print a sub-section header."""
    print(f"\n{colored('▶', Colors.GREEN)} {colored(title, Colors.BOLD)}")
    print(colored("-" * 40, Colors.GREEN))


def info(label, value):
    """Print a key-value info line."""
    print(f"  {colored(label + ':', Colors.YELLOW):40s} {value}")


def success(msg):
    """Print a success message."""
    print(f"  {colored('✓', Colors.GREEN)} {msg}")


def warning(msg):
    """Print a warning message."""
    print(f"  {colored('⚠', Colors.YELLOW)} {msg}")


def error(msg):
    """Print an error message."""
    print(f"  {colored('✗', Colors.RED)} {msg}")


# ============================================================
# Section 1: Virtual Environment Detection
# ============================================================
def check_virtual_environment():
    """Check if we're running inside a virtual environment."""
    header("Virtual Environment Detection")

    subheader("Method 1: sys.prefix vs sys.base_prefix")
    info("sys.prefix", sys.prefix)
    info("sys.base_prefix", sys.base_prefix)

    in_venv = sys.prefix != sys.base_prefix
    if in_venv:
        success("You ARE inside a virtual environment!")
        info("venv location", sys.prefix)
    else:
        warning("You are NOT inside a virtual environment.")
        print(f"\n  {colored('Recommendation:', Colors.BOLD)} Create one with:")
        print(f"    python3 -m venv .venv")
        print(f"    source .venv/bin/activate  # macOS/Linux")
        print(f"    .venv\\Scripts\\activate     # Windows")

    subheader("Method 2: VIRTUAL_ENV environment variable")
    virtual_env = os.environ.get("VIRTUAL_ENV")
    if virtual_env:
        info("VIRTUAL_ENV", virtual_env)
        success("VIRTUAL_ENV is set.")
    else:
        info("VIRTUAL_ENV", "(not set)")
        warning("VIRTUAL_ENV environment variable is not set.")

    subheader("Method 3: Check for CONDA environment")
    conda_env = os.environ.get("CONDA_DEFAULT_ENV")
    conda_prefix = os.environ.get("CONDA_PREFIX")
    if conda_env:
        info("CONDA_DEFAULT_ENV", conda_env)
        info("CONDA_PREFIX", conda_prefix or "(not set)")
        success("You are inside a conda environment!")
    else:
        info("CONDA_DEFAULT_ENV", "(not set)")

    return in_venv


# ============================================================
# Section 2: Python Information
# ============================================================
def show_python_info():
    """Display current Python path and version info."""
    header("Python Information")

    subheader("Interpreter Details")
    info("Python version", platform.python_version())
    info("Python executable", sys.executable)
    info("Python path (prefix)", sys.prefix)
    info("Platform", platform.platform())
    info("Architecture", platform.machine())
    info("Implementation", platform.python_implementation())

    subheader("Important Paths")
    info("Site-packages", sysconfig.get_path("purelib"))
    info("Scripts/bin dir", sysconfig.get_path("scripts"))
    info("Include dir", sysconfig.get_path("include"))

    subheader("sys.path (Module Search Paths)")
    for i, p in enumerate(sys.path[:10]):
        print(f"    [{i}] {p}")
    if len(sys.path) > 10:
        print(f"    ... and {len(sys.path) - 10} more")


# ============================================================
# Section 3: Installed Packages
# ============================================================
def list_installed_packages():
    """List installed packages programmatically."""
    header("Installed Packages")

    try:
        from importlib.metadata import distributions

        packages = sorted(
            [(d.metadata["Name"], d.metadata["Version"]) for d in distributions()],
            key=lambda x: x[0].lower(),
        )

        subheader(f"Found {len(packages)} installed packages")
        # Show first 20
        display_count = min(20, len(packages))
        for name, version in packages[:display_count]:
            print(f"    {name:30s} {colored(version, Colors.CYAN)}")
        if len(packages) > display_count:
            print(
                f"\n    ... and {len(packages) - display_count} more. "
                f"Run 'pip list' to see all."
            )
    except ImportError:
        warning("importlib.metadata not available (Python < 3.8)")
        print("    Falling back to pip list...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list"],
            capture_output=True,
            text=True,
        )
        print(result.stdout[:2000])


# ============================================================
# Section 4: Check Available Tools
# ============================================================
def check_tool_available(tool_name):
    """Check if a command-line tool is available."""
    return shutil.which(tool_name) is not None


def get_tool_version(tool_name, version_flag="--version"):
    """Get the version string of a tool."""
    try:
        result = subprocess.run(
            [tool_name, version_flag],
            capture_output=True,
            text=True,
            timeout=10,
        )
        output = result.stdout.strip() or result.stderr.strip()
        # Return first line only
        return output.split("\n")[0] if output else "(unknown version)"
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return None


def check_available_tools():
    """Check which package management tools are available."""
    header("Available Tools Check")

    tools = {
        "pip": {"cmd": "pip", "desc": "Standard Python package installer"},
        "pip3": {"cmd": "pip3", "desc": "pip for Python 3 (alias)"},
        "uv": {"cmd": "uv", "desc": "Ultra-fast package manager (Rust-based)"},
        "conda": {"cmd": "conda", "desc": "Package & environment manager"},
        "mamba": {"cmd": "mamba", "desc": "Fast conda replacement (C++)"},
        "poetry": {"cmd": "poetry", "desc": "Dependency management & packaging"},
        "pdm": {"cmd": "pdm", "desc": "Modern Python package manager"},
        "pipx": {"cmd": "pipx", "desc": "Install CLI tools in isolation"},
        "pyenv": {"cmd": "pyenv", "desc": "Python version management"},
        "virtualenv": {"cmd": "virtualenv", "desc": "Virtual environment creator"},
    }

    available = {}

    subheader("Checking installed tools")
    for name, details in tools.items():
        is_available = check_tool_available(details["cmd"])
        if is_available:
            version = get_tool_version(details["cmd"])
            version_str = f" ({version})" if version else ""
            success(f"{name:12s} - {details['desc']}{version_str}")
            available[name] = version
        else:
            error(f"{name:12s} - {details['desc']} [NOT INSTALLED]")

    return available


# ============================================================
# Section 5: pip Configuration
# ============================================================
def show_pip_configuration():
    """Show current pip configuration."""
    header("pip Configuration")

    subheader("pip config locations")
    # Common pip config file locations
    if platform.system() == "Darwin":  # macOS
        config_paths = [
            Path.home() / ".config" / "pip" / "pip.conf",
            Path.home() / "Library" / "Application Support" / "pip" / "pip.conf",
            Path("/etc/pip.conf"),
        ]
    elif platform.system() == "Linux":
        config_paths = [
            Path.home() / ".config" / "pip" / "pip.conf",
            Path.home() / ".pip" / "pip.conf",
            Path("/etc/pip.conf"),
        ]
    else:  # Windows
        config_paths = [
            Path(os.environ.get("APPDATA", "")) / "pip" / "pip.ini",
            Path(os.environ.get("USERPROFILE", "")) / "pip" / "pip.ini",
        ]

    found_config = False
    for config_path in config_paths:
        if config_path.exists():
            success(f"Found config: {config_path}")
            found_config = True
            try:
                content = config_path.read_text()
                print(f"    Content:\n")
                for line in content.strip().split("\n"):
                    print(f"      {line}")
            except PermissionError:
                warning(f"Cannot read {config_path} (permission denied)")
        else:
            info(f"Not found", str(config_path))

    if not found_config:
        info("Status", "No pip configuration file found (using defaults)")

    subheader("pip cache location")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "cache", "info"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            for line in result.stdout.strip().split("\n"):
                print(f"    {line}")
        else:
            warning("Could not retrieve pip cache info.")
    except (subprocess.TimeoutExpired, FileNotFoundError):
        warning("pip cache command not available.")


# ============================================================
# Section 6: Create venv Programmatically (Demo)
# ============================================================
def demo_create_venv():
    """Demonstrate creating a virtual environment programmatically."""
    header("Demo: Creating a venv Programmatically")

    demo_path = Path.cwd() / ".demo_venv_temp"

    print(f"\n  This demo will create a temporary venv at:")
    print(f"    {demo_path}")
    print(f"\n  Command: python3 -m venv {demo_path}")

    # Ask permission (non-interactive mode: just show how)
    print(f"\n  {colored('Code to create a venv programmatically:', Colors.BOLD)}")
    print(
        """
    import subprocess, sys

    # Method 1: Using subprocess
    subprocess.run([sys.executable, "-m", "venv", ".venv"])

    # Method 2: Using the venv module directly
    import venv
    builder = venv.EnvBuilder(with_pip=True, clear=True)
    builder.create(".venv")

    # Method 3: Using uv (if available, much faster!)
    subprocess.run(["uv", "venv", ".venv"])
    """
    )

    # Actually create a temporary one to demonstrate
    print(f"\n  {colored('Creating temporary demo venv...', Colors.YELLOW)}")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "venv", str(demo_path)],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            success(f"Created successfully at: {demo_path}")

            # Show structure
            subheader("venv folder structure")
            for item in sorted(demo_path.iterdir()):
                icon = "📁" if item.is_dir() else "📄"
                print(f"    {icon} {item.name}/")
                if item.is_dir():
                    for subitem in sorted(item.iterdir())[:5]:
                        print(f"        {'📁' if subitem.is_dir() else '📄'} {subitem.name}")

            # Show pyvenv.cfg
            cfg_file = demo_path / "pyvenv.cfg"
            if cfg_file.exists():
                subheader("pyvenv.cfg contents")
                for line in cfg_file.read_text().strip().split("\n"):
                    print(f"    {line}")

            # Clean up
            print(f"\n  {colored('Cleaning up demo venv...', Colors.YELLOW)}")
            shutil.rmtree(demo_path)
            success("Demo venv removed.")
        else:
            error(f"Failed to create venv: {result.stderr}")
    except subprocess.TimeoutExpired:
        error("Timed out creating venv.")
    except Exception as e:
        error(f"Error: {e}")


# ============================================================
# Section 7: Check for Outdated Packages
# ============================================================
def check_outdated_packages():
    """Check for outdated packages in the current environment."""
    header("Outdated Packages Check")

    print(f"\n  Running: pip list --outdated --format=columns")
    print(f"  (This may take a moment...)\n")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--outdated", "--format=columns"],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0 and result.stdout.strip():
            lines = result.stdout.strip().split("\n")
            for line in lines[:15]:
                print(f"    {line}")
            if len(lines) > 15:
                print(f"\n    ... and {len(lines) - 15} more outdated packages.")
            print(f"\n  {colored('To upgrade all:', Colors.BOLD)}")
            print(f"    pip install --upgrade <package_name>")
        else:
            success("All packages are up to date! 🎉")
    except subprocess.TimeoutExpired:
        warning("Check timed out (network may be slow).")
    except Exception as e:
        warning(f"Could not check: {e}")


# ============================================================
# Section 8: Generate requirements.txt
# ============================================================
def generate_requirements():
    """Generate a requirements.txt from the current environment."""
    header("Generate requirements.txt")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "freeze"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            packages = result.stdout.strip()
            if packages:
                lines = packages.split("\n")
                subheader(f"Current environment ({len(lines)} packages)")
                for line in lines[:15]:
                    print(f"    {line}")
                if len(lines) > 15:
                    print(f"    ... and {len(lines) - 15} more.")

                print(f"\n  {colored('To save to file, run:', Colors.BOLD)}")
                print(f"    pip freeze > requirements.txt")
                print(f"\n  {colored('Better practice (exclude editables):', Colors.BOLD)}")
                print(f"    pip freeze --exclude-editable > requirements.txt")
            else:
                info("Status", "No packages installed (clean environment)")
    except Exception as e:
        warning(f"Could not generate: {e}")


# ============================================================
# Section 9: OS-Specific Commands Guide
# ============================================================
def print_os_commands():
    """Print helpful commands based on the user's OS/platform."""
    header("Quick Reference Commands for Your System")

    system = platform.system()
    subheader(f"Detected OS: {system} ({platform.platform()})")

    if system == "Darwin":
        os_name = "macOS"
        activate_cmd = "source .venv/bin/activate"
        deactivate_cmd = "deactivate"
        rm_cmd = "rm -rf .venv"
        python_cmd = "python3"
    elif system == "Linux":
        os_name = "Linux"
        activate_cmd = "source .venv/bin/activate"
        deactivate_cmd = "deactivate"
        rm_cmd = "rm -rf .venv"
        python_cmd = "python3"
    else:
        os_name = "Windows"
        activate_cmd = ".venv\\Scripts\\activate"
        deactivate_cmd = "deactivate"
        rm_cmd = "rmdir /s /q .venv"
        python_cmd = "python"

    print(f"""
  {colored(f'Commands for {os_name}:', Colors.BOLD)}

  {colored('--- Virtual Environment (venv) ---', Colors.CYAN)}
  Create:      {python_cmd} -m venv .venv
  Activate:    {activate_cmd}
  Deactivate:  {deactivate_cmd}
  Delete:      {rm_cmd}

  {colored('--- pip ---', Colors.CYAN)}
  Install:     pip install package_name
  Pin version: pip install package==1.0.0
  From file:   pip install -r requirements.txt
  Freeze:      pip freeze > requirements.txt
  Upgrade:     pip install --upgrade package_name
  List:        pip list
  Outdated:    pip list --outdated
  Uninstall:   pip uninstall package_name

  {colored('--- uv (if installed) ---', Colors.CYAN)}
  New project: uv init my-project
  Add dep:     uv add requests
  Install:     uv sync
  Run:         uv run python main.py
  Lock:        uv lock
  Venv:        uv venv .venv

  {colored('--- conda (if installed) ---', Colors.CYAN)}
  Create:      conda create -n myenv python=3.11
  Activate:    conda activate myenv
  Install:     conda install package_name
  Export:      conda env export > environment.yml
  Import:      conda env create -f environment.yml
  Deactivate:  conda deactivate
  Remove env:  conda env remove -n myenv
    """)


# ============================================================
# Section 10: Recommendations
# ============================================================
def print_recommendations(available_tools, in_venv):
    """Print personalized recommendations based on available tools."""
    header("Personalized Recommendations")

    has_uv = "uv" in available_tools
    has_conda = "conda" in available_tools
    has_poetry = "poetry" in available_tools

    subheader("Based on your available tools")

    if has_uv:
        print(f"""
  {colored('★ RECOMMENDED: Use uv (you have it installed!)', Colors.GREEN)}

  uv is the fastest and most modern option. Here's your workflow:

    # Start a new project
    uv init my-project && cd my-project

    # Add dependencies
    uv add requests pandas flask

    # Run your code
    uv run python main.py

    # Share with others (they just need uv)
    # Your pyproject.toml + uv.lock are committed to git
        """)

    if has_conda:
        print(f"""
  {colored('★ For Data Science: Use conda', Colors.GREEN)}

  conda excels at managing scientific packages with C/CUDA dependencies:

    # Create environment for data science
    conda create -n ds python=3.11 pandas numpy scikit-learn jupyter

    # Activate
    conda activate ds

    # Add more packages
    conda install -c conda-forge matplotlib seaborn
        """)

    if not has_uv and not has_conda:
        print(f"""
  {colored('★ RECOMMENDED: Install uv for the best experience', Colors.YELLOW)}

    # Install uv (one command):
    curl -LsSf https://astral.sh/uv/install.sh | sh

  {colored('★ In the meantime, use venv + pip:', Colors.GREEN)}

    python3 -m venv .venv
    source .venv/bin/activate
    pip install <packages>
    pip freeze > requirements.txt
        """)

    if not in_venv:
        print(f"""
  {colored('⚠  You are NOT in a virtual environment right now!', Colors.YELLOW)}

  Before installing any packages, create and activate a venv:

    python3 -m venv .venv
    source .venv/bin/activate  # macOS/Linux
        """)

    subheader("General Best Practices")
    print("""
  1. Always use a virtual environment (never install to system Python)
  2. Pin versions in production (package==1.2.3)
  3. Use lock files for reproducibility (uv.lock, poetry.lock)
  4. Add .venv/ to .gitignore
  5. Document setup in README.md
  6. Separate dev and production dependencies
  7. Regularly check for outdated packages (security!)
    """)


# ============================================================
# Main Execution
# ============================================================
def main():
    """Run all checks and display the interactive guide."""
    print(colored("""
╔══════════════════════════════════════════════════════════════╗
║   Virtual Environments & Package Managers - Python Guide    ║
║                    Interactive Checker                       ║
╚══════════════════════════════════════════════════════════════╝
    """, Colors.BOLD + Colors.CYAN))

    # Run all sections
    in_venv = check_virtual_environment()
    show_python_info()
    list_installed_packages()
    available_tools = check_available_tools()
    show_pip_configuration()
    demo_create_venv()
    check_outdated_packages()
    generate_requirements()
    print_os_commands()
    print_recommendations(available_tools, in_venv)

    # Final summary
    header("Summary")
    print(f"""
  Python:       {platform.python_version()} at {sys.executable}
  In venv:      {'✓ Yes' if in_venv else '✗ No'}
  OS:           {platform.system()} {platform.machine()}
  Tools found:  {', '.join(available_tools.keys()) if available_tools else 'pip only'}

  {colored('Happy coding! 🐍', Colors.GREEN + Colors.BOLD)}
    """)


if __name__ == "__main__":
    main()
