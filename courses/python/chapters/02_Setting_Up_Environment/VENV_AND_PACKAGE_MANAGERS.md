# Virtual Environments & Package Managers in Python

> **Video 02: Setting Up the Environment**  
> A comprehensive guide to isolating your Python projects and managing dependencies.

---

## Table of Contents

1. [Why Virtual Environments?](#1-why-virtual-environments)
2. [Python venv (Built-in)](#2-python-venv-built-in)
3. [pip (Package Installer for Python)](#3-pip-package-installer-for-python)
4. [uv (Modern, Ultra-Fast Package Manager)](#4-uv-modern-ultra-fast-package-manager)
5. [conda (Anaconda/Miniconda)](#5-conda-anacondaminiconda)
6. [Other Tools (Brief Mentions)](#6-other-tools-brief-mentions)
7. [Comparison Table](#7-comparison-table)
8. [Best Practices & Recommendations](#8-best-practices--recommendations)
9. [Common Workflows](#9-common-workflows)

---

## 1. Why Virtual Environments?

### The Dependency Hell Problem

Imagine you're working on two projects:

- **Project A** (a web app built last year) requires `requests==2.25.0`
- **Project B** (a new API client) requires `requests==2.31.0`

Without virtual environments, both projects share the same Python installation. Installing `requests` for Project B would **break** Project A. This is called **dependency hell**.

```
System Python
├── requests 2.31.0  ← Project B needs this
│   └── But Project A BREAKS with this version!
└── numpy 1.24.0    ← Maybe Project A needs 1.21.0?
```

### System Python Pollution

Your operating system (especially macOS and Linux) ships with a system Python that the OS itself depends on. Installing packages globally can:

- Break OS tools that depend on specific package versions
- Require `sudo` (root access) which is a security risk
- Create conflicts between OS-managed packages and your packages
- On macOS, `brew` and system tools may fight over Python

```bash
# NEVER DO THIS (installs to system Python)
sudo pip install some-package  # ❌ Dangerous!

# ALWAYS DO THIS (inside a virtual environment)
pip install some-package  # ✅ Safe - isolated to your project
```

### Reproducibility Across Machines

When you share your project with a teammate or deploy to a server:

- They need the **exact same** package versions you used
- "It works on my machine" is not acceptable
- Virtual environments + lock files = reproducible builds
- CI/CD pipelines need to recreate your environment from scratch

### Isolation for Different Projects

Each project gets its own sandbox:

```
~/projects/
├── web-app/
│   └── .venv/          ← Django 4.2, Python 3.11
├── data-science/
│   └── .venv/          ← pandas 2.0, numpy 1.24, Python 3.10
├── automation/
│   └── .venv/          ← selenium 4.8, Python 3.12
└── legacy-app/
    └── .venv/          ← Flask 1.1, Python 3.8
```

Each project can have different Python versions, different packages, and different package versions — completely independent of each other.

---

## 2. Python venv (Built-in)

`venv` is Python's built-in module for creating virtual environments. It ships with Python 3.3+ and requires no additional installation.

### Creating a Virtual Environment

```bash
# Basic creation (recommended name: .venv or venv)
python3 -m venv .venv

# With a custom name
python3 -m venv myproject_env

# With access to system site-packages
python3 -m venv .venv --system-site-packages

# Clear and recreate if it already exists
python3 -m venv .venv --clear

# Without pip (lighter, useful if you'll use uv)
python3 -m venv .venv --without-pip
```

### Activating the Virtual Environment

```bash
# macOS / Linux (bash/zsh)
source .venv/bin/activate

# macOS / Linux (fish shell)
source .venv/bin/activate.fish

# Windows (Command Prompt)
.venv\Scripts\activate.bat

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Git Bash)
source .venv/Scripts/activate
```

After activation, your shell prompt changes:

```bash
(.venv) user@machine ~/project $
```

### Deactivating

```bash
# Simply type:
deactivate
```

### What Happens When You Activate?

When you run `source .venv/bin/activate`, the script:

1. **Prepends** `.venv/bin/` to your `PATH` environment variable
2. Sets `VIRTUAL_ENV` environment variable to the venv path
3. Modifies your shell prompt to show the venv name
4. Stores the original `PATH` so `deactivate` can restore it

```bash
# Before activation
echo $PATH
# /usr/local/bin:/usr/bin:/bin

# After activation
echo $PATH
# /home/user/project/.venv/bin:/usr/local/bin:/usr/bin:/bin

# The venv's Python comes FIRST, so it "wins"
which python
# /home/user/project/.venv/bin/python
```

### Folder Structure of a venv

```
.venv/
├── bin/                    # (Linux/macOS) or Scripts/ (Windows)
│   ├── activate            # Activation script (bash)
│   ├── activate.fish       # Activation script (fish)
│   ├── activate.csh        # Activation script (csh)
│   ├── pip                 # pip executable (isolated)
│   ├── pip3                # pip3 executable
│   ├── python              # Symlink to Python interpreter
│   └── python3             # Symlink to Python interpreter
├── include/                # C headers for compiling extensions
├── lib/
│   └── python3.11/
│       └── site-packages/  # Where installed packages live
├── lib64 -> lib            # Symlink (Linux)
└── pyvenv.cfg              # Configuration file
```

### The pyvenv.cfg File

```ini
home = /usr/local/bin
include-system-site-packages = false
version = 3.11.5
executable = /usr/local/bin/python3.11
command = /usr/local/bin/python3.11 -m venv /home/user/project/.venv
```

This file tells Python that this directory is a virtual environment and where the base Python lives.

### Deleting a Virtual Environment

There's no special command — just delete the folder:

```bash
# macOS/Linux
rm -rf .venv

# Windows (Command Prompt)
rmdir /s /q .venv

# Windows (PowerShell)
Remove-Item -Recurse -Force .venv
```

### The --system-site-packages Flag

```bash
python3 -m venv .venv --system-site-packages
```

This creates a venv that can **also** see packages installed in the system Python. Useful when:
- You have large packages (like PyTorch) installed system-wide
- You don't want to re-download huge packages for every project

Packages you install in the venv still stay isolated; you just get read access to system packages too.

### VS Code Integration

1. Open Command Palette: `Cmd+Shift+P` (macOS) / `Ctrl+Shift+P` (Windows/Linux)
2. Type: "Python: Select Interpreter"
3. Choose the interpreter from your `.venv` folder
4. VS Code will auto-activate the venv in new terminals

**Tip:** If you name your venv `.venv`, VS Code auto-detects it!

---

## 3. pip (Package Installer for Python)

`pip` is the standard package installer for Python. It downloads packages from [PyPI](https://pypi.org) (Python Package Index) — a repository of 500,000+ packages.

### Basic Installation

```bash
# Install a package
pip install requests

# Install a specific version (pinning)
pip install requests==2.31.0

# Install with version constraints
pip install requests>=2.28.0
pip install requests>=2.28.0,<3.0.0
pip install "requests>=2.28,<3"  # Quotes needed for shell special chars

# Install multiple packages
pip install requests flask pandas

# Install from a requirements file
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade requests
pip install -U requests  # Short form

# Upgrade pip itself
pip install --upgrade pip
```

### Version Specifiers

```
==2.31.0      # Exact version
>=2.28.0      # Minimum version
<=3.0.0       # Maximum version
>=2.28,<3.0   # Range
~=2.28.0      # Compatible release (>=2.28.0, <2.29.0)
!=2.29.0      # Exclude a version
```

### Listing and Inspecting Packages

```bash
# List all installed packages
pip list

# List outdated packages
pip list --outdated

# Show details about a package
pip show requests
# Name: requests
# Version: 2.31.0
# Summary: Python HTTP for Humans.
# Requires: certifi, charset-normalizer, idna, urllib3
# Required-by: some-other-package

# Show where packages are installed
pip show -f requests  # Lists all files
```

### Uninstalling Packages

```bash
# Uninstall a single package
pip uninstall requests

# Uninstall without confirmation prompt
pip uninstall -y requests

# Uninstall multiple packages
pip uninstall requests flask pandas
```

### Requirements Files

```bash
# Generate requirements.txt from current environment
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

**requirements.txt** example:

```
# Pinned versions (recommended for deployment)
requests==2.31.0
flask==3.0.0
pandas==2.1.4
numpy==1.26.2

# With extras
fastapi[all]==0.104.1

# From git repository
git+https://github.com/user/repo.git@main#egg=package_name

# From a URL
https://example.com/package-1.0.tar.gz
```

### Best Practices for requirements.txt

```bash
# Split into multiple files:
requirements/
├── base.txt        # Core dependencies
├── dev.txt         # Development tools (pytest, black, mypy)
├── prod.txt        # Production-specific (gunicorn, sentry-sdk)
└── test.txt        # Testing dependencies
```

**dev.txt** can reference base:

```
-r base.txt
pytest==7.4.3
black==23.12.0
mypy==1.7.1
```

### Constraints Files

A constraints file pins versions without installing packages:

```bash
# constraints.txt
numpy==1.26.2
pandas==2.1.4

# Use it:
pip install -c constraints.txt my-package
```

This ensures that if `my-package` depends on numpy, it will use exactly version 1.26.2.

### Editable Installs (Development Mode)

```bash
# Install your own package in development mode
pip install -e .

# Install with optional dependencies
pip install -e ".[dev,test]"
```

This creates a symlink so changes to your source code are immediately reflected without reinstalling.

### pip Cache

```bash
# Show cache info
pip cache info

# List cached packages
pip cache list

# Remove all cached packages
pip cache purge

# Remove cache for specific package
pip cache remove requests
```

### pip Configuration

**pip.conf** (macOS/Linux: `~/.config/pip/pip.conf`) or **pip.ini** (Windows: `%APPDATA%\pip\pip.ini`):

```ini
[global]
timeout = 60
index-url = https://pypi.org/simple
trusted-host = pypi.org

[install]
# Always compile to bytecode
compile = yes
```

### Installing from Git Repositories

```bash
# From a public GitHub repo (latest main branch)
pip install git+https://github.com/user/repo.git

# From a specific branch
pip install git+https://github.com/user/repo.git@develop

# From a specific tag
pip install git+https://github.com/user/repo.git@v1.0.0

# From a specific commit
pip install git+https://github.com/user/repo.git@abc123def
```

### Private PyPI / Custom Index

```bash
# Install from a private index
pip install --index-url https://private.pypi.org/simple/ my-package

# Use an extra index (falls back to PyPI)
pip install --extra-index-url https://private.pypi.org/simple/ my-package
```

---

## 4. uv (Modern, Ultra-Fast Package Manager)

[uv](https://github.com/astral-sh/uv) is a blazing-fast Python package installer and resolver written in Rust by [Astral](https://astral.sh) (the makers of Ruff). It's a drop-in replacement for `pip`, `pip-tools`, `virtualenv`, and more.

### Why uv?

- **10-100x faster** than pip (cold installs)
- **Drop-in compatible** with pip commands
- **Built-in virtual environment** management
- **Dependency resolution** is faster and more reliable
- **Python version management** (like pyenv)
- **Project management** (like poetry)
- **Single binary** — no Python needed to install uv itself

### Installation

```bash
# Official installer (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# macOS (Homebrew)
brew install uv

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip (if you already have Python)
pip install uv

# With pipx
pipx install uv
```

### Creating Virtual Environments with uv

```bash
# Create a venv (much faster than python -m venv)
uv venv

# Create with a specific name
uv venv .venv

# Create with a specific Python version
uv venv --python 3.12

# Create with a specific Python version (downloads it if needed!)
uv venv --python 3.11.5
```

### uv as a pip Replacement

```bash
# Install packages (same syntax as pip, but WAY faster)
uv pip install requests flask pandas

# Install from requirements.txt
uv pip install -r requirements.txt

# Install with version constraints
uv pip install "requests>=2.28,<3"

# Freeze current environment
uv pip freeze > requirements.txt

# List installed packages
uv pip list

# Show package info
uv pip show requests

# Uninstall
uv pip uninstall requests

# Compile requirements (like pip-compile from pip-tools)
uv pip compile requirements.in -o requirements.txt

# Sync environment to match requirements exactly
uv pip sync requirements.txt
```

### uv Project Management

```bash
# Initialize a new project
uv init my-project
cd my-project

# Add dependencies
uv add requests
uv add flask "pandas>=2.0"

# Add development dependencies
uv add --dev pytest black mypy

# Remove dependencies
uv remove requests

# Create/update lockfile
uv lock

# Sync environment from lockfile (installs exact versions)
uv sync

# Run a command in the project environment
uv run python main.py
uv run pytest
uv run flask run
```

### uv run (Script Execution)

```bash
# Run a script — uv handles the environment automatically
uv run script.py

# Run with inline dependencies (no project setup needed!)
uv run --with requests --with rich script.py

# Run a specific Python version
uv run --python 3.12 script.py
```

### uv Python Version Management

```bash
# List available Python versions
uv python list

# Install a specific Python version
uv python install 3.12
uv python install 3.11.5

# Install multiple versions
uv python install 3.10 3.11 3.12

# Pin a Python version for the project
uv python pin 3.11
```

### uv Tool Management (like pipx)

```bash
# Install CLI tools globally (isolated environments)
uv tool install ruff
uv tool install black
uv tool install httpie

# Run a tool without installing
uv tool run cowsay "Hello, uv!"
uvx cowsay "Hello, uv!"  # Short form

# List installed tools
uv tool list

# Upgrade a tool
uv tool upgrade ruff
```

### pyproject.toml with uv

When you run `uv init`, it creates a `pyproject.toml`:

```toml
[project]
name = "my-project"
version = "0.1.0"
description = ""
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.31.0",
    "flask>=3.0.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=7.4.0",
    "black>=23.12.0",
]
```

### Speed Comparison

| Operation | pip | uv | Speedup |
|-----------|-----|-----|---------|
| Install requests (cached) | 1.2s | 0.01s | ~120x |
| Install Django (cold) | 8.5s | 0.8s | ~10x |
| Resolve 100 deps | 12s | 0.5s | ~24x |
| Create venv | 3.0s | 0.1s | ~30x |

*(Times are approximate and vary by system)*

### When to Use uv vs pip

| Use **uv** when... | Use **pip** when... |
|---|---|
| Starting a new project | Working on legacy projects with pip workflows |
| Speed matters (CI/CD) | uv isn't available on the system |
| Managing Python versions | You need maximum compatibility |
| You want modern project management | Simple one-off installs |
| Lock files are important | Teaching absolute beginners |

---

## 5. conda (Anaconda/Miniconda)

`conda` is both a **package manager** AND an **environment manager**. Unlike pip, it can manage non-Python packages (C libraries, CUDA, R, etc.).

### Anaconda vs Miniconda vs Miniforge

| | Anaconda | Miniconda | Miniforge |
|---|---|---|---|
| Size | ~3 GB | ~400 MB | ~400 MB |
| Includes | 1500+ packages | Minimal (conda + Python) | Minimal + conda-forge |
| Default channel | defaults (Anaconda) | defaults (Anaconda) | conda-forge |
| License | Commercial restrictions | Commercial restrictions | Fully open source |
| **Recommended** | ❌ Too bloated | ✅ Good starting point | ✅ Best for open source |

**Recommendation:** Install **Miniforge** for open-source use, or **Miniconda** if you're in an enterprise with Anaconda licenses.

### Installing Miniconda

```bash
# macOS (Apple Silicon)
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
bash Miniconda3-latest-MacOSX-arm64.sh

# macOS (Intel)
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh

# Linux
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Windows: Download and run the .exe installer from
# https://docs.conda.io/en/latest/miniconda.html
```

### Creating and Managing Environments

```bash
# Create a new environment with a specific Python version
conda create -n myproject python=3.11

# Create with specific packages
conda create -n datascience python=3.11 pandas numpy matplotlib jupyter

# Activate the environment
conda activate myproject

# Deactivate
conda deactivate

# List all environments
conda env list
conda info --envs

# Remove an environment
conda env remove -n myproject

# Clone an environment
conda create --clone myproject -n myproject_backup
```

### Installing Packages

```bash
# Install from default channel
conda install numpy

# Install a specific version
conda install numpy=1.26.2

# Install from conda-forge channel (usually more up-to-date)
conda install -c conda-forge polars

# Install multiple packages
conda install pandas scikit-learn matplotlib

# Update a package
conda update numpy

# Update all packages in environment
conda update --all

# Remove a package
conda remove numpy

# List installed packages
conda list

# Search for a package
conda search tensorflow
```

### Exporting and Reproducing Environments

```bash
# Export environment (cross-platform, recommended)
conda env export --from-history > environment.yml

# Export with exact versions (platform-specific)
conda env export > environment.yml

# Create environment from YAML file
conda env create -f environment.yml

# Update environment from YAML file
conda env update -f environment.yml
```

**environment.yml** example:

```yaml
name: datascience
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - pandas>=2.0
  - numpy>=1.24
  - scikit-learn>=1.3
  - matplotlib>=3.7
  - jupyter>=1.0
  - pip:
    - some-pip-only-package==1.0.0
    - another-pip-package>=2.0
```

### Conda Channels

Channels are repositories where conda looks for packages:

```bash
# conda-forge (community-maintained, most up-to-date)
conda install -c conda-forge package_name

# Set conda-forge as default channel
conda config --add channels conda-forge
conda config --set channel_priority strict

# bioconda (bioinformatics packages)
conda install -c bioconda samtools

# nvidia (CUDA and GPU packages)
conda install -c nvidia cuda-toolkit
```

### conda vs pip: When to Use Which

| Use **conda** when... | Use **pip** when... |
|---|---|
| Need non-Python deps (CUDA, MKL, HDF5) | Package is only on PyPI |
| Need specific Python version | Using venv (not conda env) |
| Data science / scientific computing | Web development |
| Need binary compatibility guaranteed | Package has wheels on PyPI |
| Cross-platform reproducibility | Simple Python packages |

### Mixing conda and pip (The Right Way)

**Rule:** Install conda packages FIRST, then pip packages LAST.

```bash
# 1. Create and activate environment
conda create -n myproject python=3.11
conda activate myproject

# 2. Install conda packages FIRST
conda install numpy pandas scikit-learn matplotlib

# 3. Install pip-only packages LAST
pip install some-package-only-on-pypi

# 4. NEVER run conda install after pip install
#    (it can break the pip packages)
```

### conda for Non-Python Packages

One of conda's unique strengths:

```bash
# Install CUDA toolkit (GPU computing)
conda install -c nvidia cuda-toolkit=12.1

# Install ffmpeg (video processing)
conda install -c conda-forge ffmpeg

# Install gcc/g++ (C/C++ compiler)
conda install -c conda-forge gcc_linux-64

# Install Node.js
conda install -c conda-forge nodejs

# Install R
conda install -c conda-forge r-base
```

### mamba (Faster conda)

`mamba` is a drop-in replacement for conda that's significantly faster (written in C++):

```bash
# Install mamba
conda install -c conda-forge mamba

# Use it exactly like conda
mamba install numpy pandas
mamba create -n myenv python=3.11
mamba env update -f environment.yml
```

**Or use Miniforge** which comes with mamba pre-installed.

---

## 6. Other Tools (Brief Mentions)

### pipx — Install CLI Tools Globally

```bash
# Install pipx
pip install --user pipx

# Install CLI tools in isolated environments
pipx install black
pipx install ruff
pipx install httpie
pipx install cookiecutter

# Run without installing
pipx run cowsay "Hello!"
```

### poetry — Dependency Management + Packaging

```bash
# Install
curl -sSL https://install.python-poetry.org | python3 -

# New project
poetry new my-project
poetry init  # In existing project

# Add dependencies
poetry add requests
poetry add --group dev pytest

# Install from lock file
poetry install

# Uses pyproject.toml + poetry.lock
```

### pdm — Modern Python Package Manager

```bash
# PEP 582 support (no venv needed!)
pdm init
pdm add requests
pdm install
pdm run python main.py
```

### pyenv — Python Version Management (Not Packages)

```bash
# Install multiple Python versions
pyenv install 3.11.5
pyenv install 3.12.0

# Set global default
pyenv global 3.11.5

# Set per-project Python version
pyenv local 3.12.0
```

**Note:** uv can now handle Python version management too (`uv python install`).

### virtualenv — The Original (Pre-venv)

```bash
# Faster than venv, more features, but external package
pip install virtualenv
virtualenv myenv
```

`virtualenv` still exists but `venv` (built-in) or `uv venv` are preferred for most use cases.

---

## 7. Comparison Table

| Feature | venv + pip | uv | conda | poetry |
|---------|-----------|-----|-------|--------|
| **Speed** | Slow | ⚡ Ultra-fast | Moderate | Moderate |
| **Lock files** | ❌ (manual freeze) | ✅ uv.lock | ✅ (explicit export) | ✅ poetry.lock |
| **Non-Python deps** | ❌ | ❌ | ✅ | ❌ |
| **Python version mgmt** | ❌ | ✅ | ✅ | ❌ (needs pyenv) |
| **Built-in to Python** | ✅ | ❌ | ❌ | ❌ |
| **Dependency resolution** | Basic | Advanced | Advanced | Advanced |
| **Project management** | ❌ | ✅ | ❌ | ✅ |
| **Packaging/publishing** | Manual | ✅ (uv publish) | ❌ | ✅ |
| **Learning curve** | Low | Low | Medium | Medium |
| **Ecosystem maturity** | High | Growing fast | High | High |
| **CI/CD friendly** | ✅ | ✅✅ | ⚠️ Slow | ✅ |
| **Data science** | ⚠️ | ⚠️ | ✅✅ | ⚠️ |
| **Best for** | Learning | Modern projects | Data science | Libraries |

---

## 8. Best Practices & Recommendations

### Golden Rules

1. **ALWAYS use a virtual environment** — never `pip install` into system Python
2. **One venv per project** — don't share environments between projects
3. **Pin your dependencies** — use exact versions in production
4. **Use lock files** — for reproducible builds
5. **.gitignore your venv folder** — never commit it to git

### .gitignore Entry

```gitignore
# Virtual Environments
.venv/
venv/
env/
ENV/

# Distribution / packaging
*.egg-info/
dist/
build/

# pip
pip-log.txt

# uv
.python-version
```

### Recommendations by Use Case

| Scenario | Recommended Tool |
|----------|-----------------|
| **Complete beginner** | `venv` + `pip` (learn fundamentals) |
| **Speed matters** | `uv` (fastest option) |
| **New Python project** | `uv` (modern, fast, full-featured) |
| **Data science / ML** | `conda` or `mamba` (handles CUDA, etc.) |
| **Publishing a library** | `uv` or `poetry` (build + publish) |
| **Enterprise / team** | `uv` or `poetry` (lock files, reproducibility) |
| **CI/CD pipelines** | `uv` (speed saves money on CI minutes) |
| **Legacy project** | Whatever it already uses (don't fix what works) |

### requirements.txt vs pyproject.toml

**requirements.txt** — Simple flat file, widely supported:

```
requests==2.31.0
flask==3.0.0
```

**pyproject.toml** — Modern standard (PEP 621), rich metadata:

```toml
[project]
name = "my-project"
version = "0.1.0"
dependencies = [
    "requests>=2.31.0",
    "flask>=3.0.0",
]

[project.optional-dependencies]
dev = ["pytest>=7.4", "black>=23.12"]
```

**Recommendation:** Use `pyproject.toml` for new projects. It's the modern standard and works with `uv`, `poetry`, `pdm`, and `pip`.

---

## 9. Common Workflows

### Starting a New Project (with uv)

```bash
# Create project directory
mkdir my-project && cd my-project

# Initialize with uv
uv init

# Add dependencies
uv add requests flask

# Add dev dependencies
uv add --dev pytest black ruff

# Start coding!
uv run python main.py
```

### Starting a New Project (with venv + pip)

```bash
# Create project directory
mkdir my-project && cd my-project

# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install packages
pip install requests flask

# Save dependencies
pip freeze > requirements.txt

# Start coding!
python main.py
```

### Cloning and Setting Up Someone Else's Project

```bash
# Clone the repo
git clone https://github.com/user/project.git
cd project

# Option A: If they use uv (has pyproject.toml + uv.lock)
uv sync

# Option B: If they use pip (has requirements.txt)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Option C: If they use conda (has environment.yml)
conda env create -f environment.yml
conda activate project-name

# Option D: If they use poetry (has pyproject.toml + poetry.lock)
poetry install
```

### Adding a New Dependency

```bash
# With uv
uv add new-package

# With pip (don't forget to update requirements.txt!)
pip install new-package
pip freeze > requirements.txt  # Or manually add it

# With conda
conda install new-package

# With poetry
poetry add new-package
```

### Upgrading Dependencies Safely

```bash
# With uv
uv lock --upgrade           # Upgrade all
uv lock --upgrade-package requests  # Upgrade one

# With pip
pip list --outdated                  # See what's outdated
pip install --upgrade requests       # Upgrade one
pip freeze > requirements.txt        # Update requirements

# With conda
conda update --all                   # Update all
conda update requests                # Update one
```

### Reproducing an Environment on Another Machine

```bash
# On Machine A (developer's machine):
pip freeze > requirements.txt
# OR
uv lock
# OR
conda env export --from-history > environment.yml

# On Machine B (server/colleague):
pip install -r requirements.txt
# OR
uv sync
# OR
conda env create -f environment.yml
```

---

## Quick Reference Card

```bash
# ===== venv =====
python3 -m venv .venv           # Create
source .venv/bin/activate       # Activate (macOS/Linux)
deactivate                      # Deactivate
rm -rf .venv                    # Delete

# ===== pip =====
pip install package             # Install
pip install -r requirements.txt # Install from file
pip freeze > requirements.txt   # Export
pip list --outdated             # Check updates
pip uninstall package           # Remove

# ===== uv =====
uv init                         # New project
uv add package                  # Add dependency
uv remove package               # Remove dependency
uv sync                         # Install from lockfile
uv run python script.py         # Run in environment
uv python install 3.12          # Install Python version

# ===== conda =====
conda create -n env python=3.11 # Create
conda activate env              # Activate
conda install package           # Install
conda env export > env.yml      # Export
conda env create -f env.yml     # Recreate
conda deactivate                # Deactivate
```

---

> **Next Video:** We'll use these tools to set up our actual development environment and install the packages we'll use throughout the course!
