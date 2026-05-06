# Setting Up the Development Environment

## Overview

In this chapter, we'll set up everything
you need to write, run, and experiment with Python code. We'll cover installing Python itself,
choosing and configuring a code editor (VS Code), and most importantly, we'll dive deep into
**Jupyter Notebooks** and **Google Colab** - two incredibly powerful tools for interactive
Python development that you'll use throughout this course and your Python journey.

By the end of this chapter, you'll have a fully functional Python development environment
ready on your computer, and you'll be comfortable using Jupyter Notebooks both locally
and in the cloud with Google Colab.

---

## Learning Objectives

After completing this chapter, you will be able to:

1. Install Python on Windows, macOS, or Linux
2. Verify your Python and pip installation
3. Set up VS Code with essential Python extensions
4. Install and launch Jupyter Notebook and JupyterLab
5. Create, edit, and run Jupyter Notebooks with confidence
6. Master Jupyter keyboard shortcuts (Command Mode and Edit Mode)
7. Use Markdown cells to document your code
8. Understand and use Magic Commands
9. Work with Google Colab for cloud-based Python development
10. Mount Google Drive, use GPUs, and share notebooks in Colab
11. Run your first Python program in multiple environments
12. Understand what virtual environments are (covered in the Virtual Environments & Packages chapter)

---

## Prerequisites

- Introduction to Python - Understanding what Python is and why we're learning it
- A computer (Windows 10+, macOS 10.14+, or Linux)
- An internet connection (for downloads and Google Colab)
- A Google account (for Google Colab)

---

## 1. Installing Python

### 1.1 Download from python.org

Visit [https://www.python.org/downloads/](https://www.python.org/downloads/) and download
the latest stable version of Python 3 (3.11+ recommended).

#### Windows Installation

1. Download the Windows installer (.exe) from python.org
2. **IMPORTANT**: Check the box "Add Python to PATH" at the bottom of the installer
3. Click "Install Now" (or "Customize installation" for advanced options)
4. Wait for installation to complete
5. Click "Disable path length limit" if prompted (recommended)
6. Click "Close"

```
# After installation, open Command Prompt or PowerShell:
python --version        # Should show Python 3.x.x
pip --version           # Should show pip version
```

#### macOS Installation

**Option A: From python.org**
1. Download the macOS universal installer (.pkg)
2. Double-click the .pkg file
3. Follow the installation wizard
4. Python will be installed as `python3`

**Option B: Using Homebrew (Recommended)**
```bash
# Install Homebrew first (if not installed):
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then install Python:
brew install python

# Verify:
python3 --version
pip3 --version
```

#### Linux Installation (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip python3-venv

# Verify installation
python3 --version
pip3 --version
```

### 1.2 Verifying Installation

Open your terminal (Command Prompt on Windows, Terminal on macOS/Linux):

```bash
# Check Python version
python3 --version
# Expected output: Python 3.11.x (or newer)

# Check pip version
pip3 --version
# Expected output: pip 23.x.x from /path/to/pip (python 3.11)

# Start Python interactive shell
python3
# You should see >>> prompt
# Type exit() or Ctrl+D to quit
```

### 1.3 PATH Configuration

The PATH is an environment variable that tells your operating system where to find executable programs.

**Why PATH matters:**
- Without Python in PATH, you'd have to type the full path every time
- Example: `/usr/local/bin/python3` instead of just `python3`

**Windows PATH Fix (if needed):**
1. Search "Environment Variables" in Windows Settings
2. Click "Environment Variables"
3. Under "System Variables", find "Path" and click "Edit"
4. Add the Python installation directory (e.g., `C:\Python311\` and `C:\Python311\Scripts\`)

**macOS/Linux PATH Fix (if needed):**
```bash
# Add to ~/.bashrc or ~/.zshrc:
export PATH="/usr/local/bin/python3:$PATH"

# Reload:
source ~/.bashrc  # or source ~/.zshrc
```

### 1.4 Multiple Python Versions (pyenv)

If you need multiple Python versions on the same machine, use **pyenv**:

```bash
# Install pyenv (macOS with Homebrew):
brew install pyenv

# Install a specific Python version:
pyenv install 3.11.6
pyenv install 3.12.0

# Set global version:
pyenv global 3.11.6

# Set local version (per project):
pyenv local 3.12.0
```

> **Note**: For this course, one Python 3.11+ installation is sufficient. We'll revisit
> version management in later chapters.

---

## 2. IDE/Editor Setup

### 2.1 Visual Studio Code (VS Code) - Recommended

VS Code is a free, lightweight, yet powerful code editor by Microsoft. It's the most
popular editor for Python development.

#### Installation

1. Visit [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Download for your operating system
3. Install following the default prompts
4. Launch VS Code

#### Essential Extensions

Open the Extensions panel (Ctrl+Shift+X / Cmd+Shift+X) and install:

| Extension | Publisher | Purpose |
|-----------|-----------|---------|
| **Python** | Microsoft | Python language support, IntelliSense, debugging |
| **Pylance** | Microsoft | Fast, feature-rich language server for Python |
| **Jupyter** | Microsoft | Jupyter Notebook support directly in VS Code |
| **Code Runner** | Jun Han | Run code snippets with one click |
| **GitLens** | GitKraken | Git supercharged - blame, history, etc. |
| **Python Indent** | Kevin Rose | Correct Python indentation |
| **autoDocstring** | Nils Werner | Generate Python docstrings |

#### VS Code Python Settings

Open Settings (Ctrl+, / Cmd+,) and configure:

```json
{
    "python.defaultInterpreterPath": "python3",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "editor.formatOnSave": true,
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "jupyter.askForKernelRestart": false
}
```

#### Running Python in VS Code

1. **Run Button**: Click the play button (top-right) with a .py file open
2. **Terminal**: Open terminal (Ctrl+`) and type `python3 filename.py`
3. **Right-click**: Right-click in editor → "Run Python File in Terminal"
4. **Jupyter**: Create a .ipynb file for notebook experience

### 2.2 PyCharm (Brief Mention)

PyCharm by JetBrains is a full-featured Python IDE. It comes in two versions:
- **Community Edition** (free) - Good for general Python development
- **Professional Edition** (paid) - Adds web development, database tools, Jupyter support

For this course, VS Code is recommended as it's free, lightweight, and has excellent
Jupyter integration.

### 2.3 Terminal/Command Line Basics

```bash
# Navigate to a directory
cd ~/Documents/python_course

# List files
ls          # macOS/Linux
dir         # Windows

# Create a directory
mkdir my_project

# Create a file
touch hello.py       # macOS/Linux
echo. > hello.py     # Windows

# Run a Python file
python3 hello.py
```

---

## 3. Jupyter Notebooks

### 3.1 What are Jupyter Notebooks?

#### History and Background

Jupyter Notebooks evolved from the **IPython** project, created by Fernando Perez in 2001.
IPython (Interactive Python) was an enhanced interactive Python shell. In 2014, the
notebook component was split into its own project called **Jupyter**.

**The name "Jupyter"** is a combination of three core programming languages:
- **Ju** - Julia
- **Py** - Python
- **teR** - R

This reflects Jupyter's language-agnostic design - while we'll use Python, Jupyter
supports over 100 programming languages through different "kernels."

#### The .ipynb File Format

Jupyter notebooks are saved as `.ipynb` files, which are actually **JSON** (JavaScript
Object Notation) files. Each notebook contains:

```json
{
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.11.0"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5,
  "cells": [
    {
      "cell_type": "code",
      "source": ["print('Hello World')"],
      "outputs": [...],
      "execution_count": 1
    },
    {
      "cell_type": "markdown",
      "source": ["# My Heading"]
    }
  ]
}
```

#### When to Use Notebooks vs .py Files

| Use Jupyter Notebooks (.ipynb) | Use Python Scripts (.py) |
|-------------------------------|--------------------------|
| Data exploration & analysis | Production applications |
| Learning & experimentation | Web servers/APIs |
| Visualization & plotting | Command-line tools |
| Documentation with code | Large software projects |
| Sharing results/reports | Automated scripts |
| Teaching & presentations | Library/package code |
| Prototyping | CI/CD pipelines |

### 3.2 Installation

```bash
# Install classic Jupyter Notebook
pip3 install jupyter

# Install JupyterLab (modern interface - RECOMMENDED)
pip3 install jupyterlab

# Install both (they share the same kernel):
pip3 install jupyter jupyterlab

# Verify installation:
jupyter --version
jupyter notebook --version
jupyter lab --version
```

### 3.3 Starting Jupyter

#### Classic Jupyter Notebook

```bash
# Start Jupyter Notebook server
jupyter notebook

# This will:
# 1. Start a local server (usually http://localhost:8888)
# 2. Open your default web browser
# 3. Show the file browser/dashboard
```

#### JupyterLab (Modern - Recommended)

```bash
# Start JupyterLab
jupyter lab

# JupyterLab advantages over classic:
# - Multiple notebooks in tabs
# - File browser sidebar
# - Terminal integration
# - Extension system
# - Dark mode
# - Drag and drop cells between notebooks
```

#### Specifying Options

```bash
# Start on a specific port
jupyter lab --port 9999

# Start without opening browser
jupyter lab --no-browser

# Start in a specific directory
jupyter lab --notebook-dir=~/my_project

# Start and allow remote connections
jupyter lab --ip 0.0.0.0
```

#### Understanding the Dashboard

When Jupyter starts, you'll see a file browser showing your current directory.
From here you can:
- Navigate through folders
- Create new notebooks (New → Python 3)
- Open existing .ipynb files
- Create new text files, terminals, or folders
- Upload files from your computer

#### Creating New Notebooks

1. Click the **"+"** button or **File → New → Notebook**
2. Select kernel (Python 3)
3. A new untitled notebook opens
4. Click "Untitled" at the top to rename it
5. **Always save with descriptive names** (e.g., `02_variables_practice.ipynb`)

#### Saving Notebooks

- **Ctrl+S / Cmd+S**: Save notebook
- **File → Save Notebook**: Manual save
- **Autosave**: Jupyter autosaves every 2 minutes (configurable)
- **File → Save and Checkpoint**: Create a checkpoint you can revert to
- **File → Save and Export Notebook As**: Export to .py, .html, .pdf, etc.

---

### 3.4 Cell Types

Jupyter Notebooks are composed of **cells**. Each cell is an independent block that can
contain code, formatted text, or raw content.

#### Code Cells

Code cells are where you write and execute Python code. They are the heart of Jupyter.

**Writing and Running Code:**

```python
# This is a code cell
x = 10
y = 20
print(f"The sum is: {x + y}")
```

**Running Cells - Keyboard Shortcuts:**

| Shortcut | Action |
|----------|--------|
| **Shift+Enter** | Run cell and move to next cell (creates new if at end) |
| **Ctrl+Enter** | Run cell and stay on same cell |
| **Alt+Enter** | Run cell and insert new cell below |

**Cell Execution Order:**

Each code cell has an execution counter shown as `In [n]:` where n is the order
in which the cell was executed. This is CRITICAL to understand:

```
In [1]: x = 5           # Executed first
In [2]: y = x + 10      # Executed second  → y = 15
In [3]: x = 100         # Executed third   → x changed!
In [4]: print(y)        # Executed fourth  → Still prints 15!
                        # (y was calculated when x was 5)
```

> **WARNING**: Cells don't have to be run in order! Running cells out of order is
> the #1 source of confusion for beginners. Always run cells top-to-bottom.

**Cell Execution Indicators:**
- `In [ ]:` - Cell has never been executed
- `In [5]:` - Cell was the 5th to be executed
- `In [*]:` - Cell is currently running (waiting for completion)

**Output Display:**

Code cells display output in several ways:

```python
# 1. Print statements (stdout)
print("This always shows")

# 2. Last expression value (return value display)
x = 42
x  # This will display 42 below the cell

# 3. Rich display (images, HTML, DataFrames)
import pandas as pd
df = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]})
df  # Displays as a formatted HTML table

# 4. Multiple outputs (need display() function)
from IPython.display import display
display(x)
display(df)
```

**Multi-line Output Scrolling:**

If a cell produces very long output, Jupyter will add a scrollbar. You can:
- Single-click the output area to toggle scrolling
- Double-click to collapse/expand the output

---

#### Markdown Cells

Markdown cells allow you to write formatted text, documentation, and explanations
between your code cells. They use **Markdown** syntax.

**To create a Markdown cell:**
1. Select a cell
2. Change the dropdown from "Code" to "Markdown" (in toolbar)
3. Or press **M** in Command Mode
4. Type your markdown
5. Press **Shift+Enter** to render it

**Headers:**
```markdown
# Heading 1 (Largest)
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6 (Smallest)
```

**Text Formatting:**
```markdown
**Bold text** or __Bold text__
*Italic text* or _Italic text_
***Bold and italic***
~~Strikethrough text~~
`Inline code`
```

**Lists:**

```markdown
Unordered list:
- Item 1
- Item 2
  - Sub-item 2a
  - Sub-item 2b
- Item 3

Ordered list:
1. First item
2. Second item
3. Third item
   1. Sub-item 3a
   2. Sub-item 3b
```

**Links and Images:**
```markdown
[Link Text](https://www.python.org)
[Link with title](https://www.python.org "Python Website")

![Alt text](path/to/image.png)
![Alt text](https://example.com/image.jpg "Optional title")
```

**Code Blocks:**

````markdown
Inline code: Use `print()` to display output.

Fenced code block:
```python
def hello():
    print("Hello, World!")
```

```bash
pip install numpy
```
````

**Tables:**
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | Data     |
| Row 2    | Data     | Data     |
| Row 3    | Data     | Data     |

Alignment:
| Left     | Center   | Right    |
|:---------|:--------:|---------:|
| left     | center   | right    |
```

**LaTeX/Math Equations:**
```markdown
Inline math: The formula is $E = mc^2$

Display math (centered):
$$
\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

More examples:
$$\sum_{i=1}^{n} x_i = x_1 + x_2 + ... + x_n$$

$$\int_0^\infty e^{-x} dx = 1$$

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}$$
```

**Blockquotes:**
```markdown
> This is a blockquote.
> It can span multiple lines.
>
> > Nested blockquote.
```

**Horizontal Rules:**
```markdown
---
***
___
```

**HTML in Markdown Cells:**

You can use raw HTML for more complex formatting:

```html
<div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
    <h3 style="color: #333;">Important Note</h3>
    <p style="color: #666;">This is styled with HTML/CSS</p>
</div>

<details>
<summary>Click to expand</summary>
Hidden content goes here!
</details>

<font color="red">Red text</font>

<center>Centered text</center>
```

**Task Lists (Checkboxes):**
```markdown
- [x] Task 1 (completed)
- [x] Task 2 (completed)
- [ ] Task 3 (incomplete)
- [ ] Task 4 (incomplete)
```

---

#### Raw Cells

Raw cells are passed through as-is without any processing. They're used in specific
scenarios:

- **NBConvert**: When converting notebooks to other formats (LaTeX, HTML, reStructuredText)
- **Custom formatting**: Content that shouldn't be interpreted as code or markdown
- **LaTeX source**: Raw LaTeX for PDF conversion

To create: Change cell type to "Raw" in the toolbar or press **R** in Command Mode.

```
\begin{equation}
  E = mc^2
\end{equation}
```

---

### 3.5 Command Mode vs Edit Mode

Jupyter has two distinct keyboard modes, similar to Vi/Vim editor. Understanding these
is essential for efficient notebook usage.

#### Edit Mode (Green Border)

When you're **inside** a cell and typing content, you're in Edit Mode.
The cell will have a **green left border** (classic) or **blue cursor** (Lab).

**Entering Edit Mode:**
- Press **Enter** on a selected cell
- Click inside a cell
- Double-click a rendered markdown cell

**Edit Mode Keyboard Shortcuts:**

| Shortcut | Action |
|----------|--------|
| **Esc** | Switch to Command Mode |
| **Tab** | Code completion / indent |
| **Shift+Tab** | Tooltip/documentation popup |
| **Ctrl+Shift+-** | Split cell at cursor position |
| **Ctrl+]** | Indent selection |
| **Ctrl+[** | Dedent selection |
| **Ctrl+A** | Select all text in cell |
| **Ctrl+Z** | Undo (within cell) |
| **Ctrl+Shift+Z** | Redo (within cell) |
| **Ctrl+Home** | Go to cell start |
| **Ctrl+End** | Go to cell end |
| **Ctrl+/** | Toggle comment |
| **Ctrl+D** | Delete line (JupyterLab) |
| **Ctrl+Backspace** | Delete word before |
| **Ctrl+Delete** | Delete word after |

**Code Completion (Tab):**
```python
# Type partial variable/function name, then press Tab:
import nu|  # Press Tab → shows numpy, numbers, etc.

# After import:
import numpy as np
np.ar|     # Press Tab → shows np.array, np.arange, etc.
```

**Documentation Popup (Shift+Tab):**
```python
# Place cursor inside function parentheses, press Shift+Tab:
print(|)   # Shows: print(*args, sep=' ', end='\n', ...)

# Press Shift+Tab multiple times for more detail:
# 1x: Brief tooltip
# 2x: Expanded documentation
# 4x: Open in pager (bottom panel)
```

---

#### Command Mode (Blue Border)

When you're operating at the **cell level** (not typing inside), you're in Command Mode.
The cell will have a **blue left border**.

**Entering Command Mode:**
- Press **Esc** while in Edit Mode
- Click in the margin area (left of a cell)

**Command Mode Keyboard Shortcuts - Navigation:**

| Shortcut | Action |
|----------|--------|
| **Up / K** | Select cell above |
| **Down / J** | Select cell below |
| **Ctrl+Home** | Jump to first cell |
| **Ctrl+End** | Jump to last cell |
| **Shift+Up** | Extend selection above |
| **Shift+Down** | Extend selection below |

**Command Mode Keyboard Shortcuts - Cell Operations:**

| Shortcut | Action |
|----------|--------|
| **A** | Insert cell **A**bove |
| **B** | Insert cell **B**elow |
| **DD** | **D**elete cell (press D twice) |
| **Z** | Undo cell deletion |
| **C** | **C**opy cell |
| **X** | Cut cell |
| **V** | Paste cell below |
| **Shift+V** | Paste cell above |
| **Shift+M** | **M**erge selected cells |

**Command Mode Keyboard Shortcuts - Cell Type:**

| Shortcut | Action |
|----------|--------|
| **Y** | Convert cell to Code |
| **M** | Convert cell to **M**arkdown |
| **R** | Convert cell to **R**aw |
| **1** | Convert to Heading 1 (markdown) |
| **2** | Convert to Heading 2 (markdown) |
| **3** | Convert to Heading 3 (markdown) |
| **4** | Convert to Heading 4 (markdown) |
| **5** | Convert to Heading 5 (markdown) |
| **6** | Convert to Heading 6 (markdown) |

**Command Mode Keyboard Shortcuts - View & Misc:**

| Shortcut | Action |
|----------|--------|
| **L** | Toggle **L**ine numbers |
| **O** | Toggle **O**utput visibility |
| **Shift+O** | Toggle output scrolling |
| **S** | **S**ave notebook |
| **H** | Show keyboard shortcuts **H**elp |
| **I, I** | **I**nterrupt kernel (press I twice) |
| **0, 0** | Restart kernel (press 0 twice) |
| **Space** | Scroll down |
| **Shift+Space** | Scroll up |
| **F** | **F**ind and replace |

---

### 3.6 Kernel Operations

#### What is a Kernel?

The **kernel** is the computational engine that executes the code in your notebook.
When you run a Python notebook, a separate Python process (the kernel) starts and
maintains state (variables, imports, functions) across all cells.

Think of it like this:
- The **notebook interface** = the paper you write on
- The **kernel** = the brain that processes your code
- **Variables** live in the kernel's memory, not in the notebook file

#### Kernel States

| State | Indicator | Meaning |
|-------|-----------|---------|
| **Idle** | Empty circle (○) | Ready for execution |
| **Busy** | Filled circle (●) | Currently executing code |
| **Dead/Disconnected** | ✕ or warning | Kernel crashed or disconnected |
| **Starting** | Hourglass | Kernel is initializing |

#### Kernel Menu Operations

| Action | What it Does |
|--------|-------------|
| **Interrupt** | Stops currently running code (like Ctrl+C in terminal). Use for infinite loops! |
| **Restart** | Kills kernel and starts fresh. ALL variables are lost! |
| **Restart & Clear Output** | Restart + remove all cell outputs |
| **Restart & Run All** | Restart + execute all cells top to bottom |
| **Shutdown** | Completely stops the kernel |
| **Change Kernel** | Switch to different kernel (Python 2, R, Julia, etc.) |

#### When to Restart the Kernel

You should restart the kernel when:
1. You're stuck in an infinite loop (Interrupt first, Restart if needed)
2. Memory is getting too high (large datasets loaded)
3. You want a clean slate to verify your notebook runs correctly
4. You've modified external modules that you imported
5. Strange errors that shouldn't be happening (stale state)

#### Kernel Troubleshooting

```python
# Common issues:

# 1. "Kernel Dead" - Usually means out of memory
# Solution: Restart kernel, reduce data size, use del to free memory

# 2. "Kernel not found"
# Solution: Install kernel - python3 -m ipykernel install --user

# 3. Variables undefined after restart
# Solution: Run all cells from top (Kernel → Restart & Run All)

# 4. Import errors after pip install
# Solution: Restart kernel to pick up newly installed packages
```

#### Memory Management

```python
# Check memory usage of variables
import sys

x = [1] * 1000000
print(f"Size of x: {sys.getsizeof(x) / 1024 / 1024:.2f} MB")

# Delete variables to free memory
del x

# Check all variables in memory
%whos

# Force garbage collection
import gc
gc.collect()
```

---

### 3.7 Magic Commands

Magic commands are special commands unique to IPython/Jupyter that provide useful
shortcuts. They are NOT valid Python - they only work in Jupyter/IPython.

#### Line Magics (% prefix) - Apply to a single line

```python
# %time - Time a single statement execution
%time result = sum(range(1000000))
# Output: CPU times: user 45 ms, sys: 2 ms, total: 47 ms
#         Wall time: 47.5 ms

# %timeit - Time repeated execution (more accurate)
%timeit sum(range(1000000))
# Output: 41.2 ms +/- 1.3 ms per loop (mean +/- std. dev. of 7 runs, 10 loops each)

# %who - List all variables of a given type
x = 10
name = "Python"
my_list = [1, 2, 3]
%whos           # Detailed variable listing (with types and values)
%who int       # Lists only int variables
%who str       # Lists only string variables
%who list      # Lists only list variables

# %run - Run a .py file
%run my_script.py
%run ./scripts/data_loader.py

# %load - Load file contents into a cell
%load my_script.py
# The file contents will replace this command in the cell

# %pwd - Print working directory
%pwd
# Output: '/Users/username/notebooks'

# %cd - Change directory
%cd ~/Documents/python_course
%cd ..  # Go up one level

# %ls - List directory contents
%ls
%ls *.py  # List only Python files

# %env - View or set environment variables
%env                    # Show all environment variables
%env MY_VAR=hello      # Set an environment variable

# %pip - Install packages (preferred over !pip in notebooks)
%pip install numpy
%pip install pandas matplotlib seaborn

# %matplotlib - Configure matplotlib backend
%matplotlib inline     # Display plots inline (most common)
%matplotlib widget     # Interactive plots (requires ipympl)

# %history - Show input history
%history              # All history
%history -n 1-10     # Lines 1-10 with line numbers

# %reset - Remove all variables (careful!)
%reset               # Asks confirmation
%reset -f            # Force reset without confirmation

# %quickref - Quick reference card for magic commands
%quickref

# %lsmagic - List all available magic commands
%lsmagic
```

#### Cell Magics (%% prefix) - Apply to the entire cell

```python
%%time
# Time the entire cell execution
result = 0
for i in range(1000000):
    result += i
print(result)
# Shows total time for the whole cell

%%timeit
# Time the entire cell repeatedly
total = 0
for i in range(100):
    total += i ** 2

%%bash
# Run bash commands in the cell
echo "Current directory:"
pwd
echo "Python version:"
python3 --version
ls -la *.py

%%html
<!-- Render HTML in output -->
<h2 style="color: blue;">Hello from HTML!</h2>
<p>This is rendered as <strong>HTML</strong></p>
<button onclick="alert('Hi!')">Click Me</button>

%%javascript
// Run JavaScript
alert("Hello from JavaScript in Jupyter!");
element.text("Modified by JS");

%%writefile my_script.py
# Write cell contents to a file
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))

%%capture captured_output
# Capture all output (stdout, stderr) into a variable
print("This won't display")
print("But it's captured")
# Later: print(captured_output.stdout)
```

---

### 3.8 Shell Commands in Jupyter

You can run shell/terminal commands directly from Jupyter using the `!` prefix:

```python
# List files
!ls -la

# Check Python version
!python3 --version

# Install a package
!pip install requests

# Git commands
!git status
!git log --oneline -5

# System information
!uname -a      # macOS/Linux
!whoami

# Download files
!wget https://example.com/data.csv
!curl -O https://example.com/file.json

# Capture shell output into Python variable
files = !ls *.py
print(files)         # IPython SList object
print(files.l)       # Regular Python list

# Use Python variables in shell commands
filename = "test.py"
!cat {filename}

directory = "/home/user"
!ls {directory}
```

---

### 3.9 Notebook Best Practices

1. **Run cells in order (top to bottom)**
   - Avoid jumping around. It leads to hidden state bugs.
   - If you need to re-run, consider "Restart & Run All"

2. **Restart & Run All before sharing**
   - Ensures the notebook works from a clean state
   - Catches dependency on cell execution order

3. **Clear output before committing to git**
   - Outputs (especially images) make .ipynb files huge
   - Use: Cell → All Output → Clear (or "Edit → Clear All Outputs" in Lab)

4. **Use descriptive markdown between code cells**
   - Explain what the next code does and why
   - Add section headers to create a narrative

5. **Keep cells focused**
   - One concept or operation per cell
   - Easier to debug and understand

6. **Name your notebooks descriptively**
   - Bad: `Untitled1.ipynb`, `test.ipynb`
   - Good: `02_data_cleaning_customer_records.ipynb`

7. **Put imports at the top**
   - First cell should contain all import statements
   - Makes dependencies clear

8. **Use consistent cell structure:**
   ```
   [Markdown: Section Title]
   [Markdown: Explanation of what we're doing]
   [Code: Implementation]
   [Code: Verification/testing]
   [Markdown: Interpretation of results]
   ```

---

## 4. Google Colab

### 4.1 What is Google Colab?

**Google Colaboratory** (Colab) is a free, cloud-based Jupyter Notebook environment
provided by Google. It runs entirely in your browser and requires no local setup.

**Key Features:**
- Free access to GPUs (NVIDIA T4) and TPUs
- No installation required - works in any browser
- Pre-installed libraries (NumPy, Pandas, TensorFlow, PyTorch, etc.)
- Google Drive integration for file storage
- Easy sharing (like Google Docs)
- Up to 12 hours of continuous runtime (free tier)

### 4.2 Accessing Google Colab

1. Go to [https://colab.research.google.com/](https://colab.research.google.com/)
2. Sign in with your Google account
3. Create a new notebook or open an existing one

**Opening notebooks:**
- **New Notebook**: File → New Notebook
- **From Google Drive**: File → Open Notebook → Google Drive tab
- **From GitHub**: File → Open Notebook → GitHub tab (paste repo URL)
- **Upload**: File → Open Notebook → Upload tab

### 4.3 Colab vs Local Jupyter

| Feature | Google Colab | Local Jupyter |
|---------|-------------|---------------|
| **Setup** | None (browser-based) | Install Python + Jupyter |
| **Cost** | Free (with limits) | Free (uses your hardware) |
| **GPU/TPU** | Free GPU access | Need your own GPU |
| **Persistence** | Session-based (resets) | Persistent local files |
| **Storage** | Google Drive (15GB free) | Your hard drive |
| **Memory** | ~12GB RAM (free) | Your machine's RAM |
| **Packages** | Many pre-installed | Install yourself |
| **Collaboration** | Real-time sharing | Manual sharing |
| **Internet** | Required always | Only for install |
| **Runtime** | Max ~12 hours | Unlimited |
| **File Access** | Via Drive mount | Direct file system |
| **Custom Envs** | Limited | Full control |

### 4.4 Google Drive Integration

One of Colab's most powerful features is seamless Google Drive integration:

```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# After mounting, your Drive is accessible at:
# /content/drive/MyDrive/

# Read a file from Drive
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/data/my_dataset.csv')

# Save a file to Drive
df.to_csv('/content/drive/MyDrive/output/results.csv', index=False)

# List files in Drive
import os
os.listdir('/content/drive/MyDrive/')
```

### 4.5 Installing Packages in Colab

```python
# Install packages (Colab has many pre-installed)
!pip install transformers
!pip install plotly
!pip install scikit-learn --upgrade

# Install specific version
!pip install numpy==1.24.0

# Install from GitHub
!pip install git+https://github.com/user/repo.git

# Check if package is installed
!pip show pandas

# List all installed packages
!pip list
```

### 4.6 Uploading and Downloading Files

```python
# Upload files from your computer
from google.colab import files

uploaded = files.upload()  # Opens file picker dialog
# Returns dict: {'filename.csv': b'file_contents...'}

# Access uploaded file
import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['data.csv']))

# Download files to your computer
files.download('output.csv')
files.download('/content/my_model.pkl')

# Download from URL
!wget https://example.com/dataset.csv
!curl -O https://example.com/large_file.zip

# Unzip files
!unzip file.zip -d /content/extracted/
```

### 4.7 Free vs Pro vs Pro+ Tiers

| Feature | Free | Pro ($9.99/mo) | Pro+ ($49.99/mo) |
|---------|------|----------------|-------------------|
| **GPU** | T4 (limited) | T4, V100, A100 | A100 (priority) |
| **RAM** | ~12 GB | Up to 32 GB | Up to 52 GB |
| **Runtime** | ~12 hours | 24 hours | 24 hours |
| **Background** | No | Yes | Yes |
| **Terminal** | No | Yes | Yes |
| **Idle Timeout** | ~90 min | Longer | Longest |
| **Priority** | Low | High | Highest |

### 4.8 Colab-Specific Features

#### Code Snippets Library

Colab has a built-in code snippets panel:
- Click the **`< >`** icon in the left sidebar
- Search for common operations (plotting, file upload, camera capture)
- Click "Insert" to add the snippet to your notebook

#### Table of Contents

- Click the **bullet list icon** in the left sidebar
- Auto-generated from markdown headings
- Click any heading to jump to that section
- Essential for long notebooks

#### Forms for Interactive Inputs

```python
#@title Enter Your Parameters { run: "auto" }
name = "World"  #@param {type:"string"}
age = 25  #@param {type:"integer"}
learning_rate = 0.001  #@param {type:"number"}
optimizer = "Adam"  #@param ["Adam", "SGD", "RMSprop"]
use_gpu = True  #@param {type:"boolean"}
date = "2024-01-01"  #@param {type:"date"}

print(f"Hello {name}, age {age}!")
```

#### Sharing Notebooks

1. **Share button** (top-right): Like Google Docs sharing
   - View only, Comment, or Edit access
   - Share with specific people or get a link
2. **Save to GitHub**: File → Save a copy in GitHub
3. **Download**: File → Download → .ipynb or .py
4. **Save to Drive**: File → Save a copy in Drive

#### Version History

- File → Revision History (or Ctrl+Alt+H)
- See all changes over time
- Restore previous versions
- Name specific versions for reference

#### Secrets Management

```python
# Store API keys securely (don't hardcode them!)
# Left sidebar → 🔑 Secrets

# Access secrets in code:
from google.colab import userdata
api_key = userdata.get('MY_API_KEY')

# This keeps your keys out of the notebook!
```

#### Runtime Disconnection

**Important things to know:**
- **Idle timeout**: ~90 minutes of inactivity (free tier)
- **Max lifetime**: ~12 hours (free tier)
- **Browser tab closed**: Runtime may persist briefly, then disconnects
- **All variables are lost** on disconnect!
- **Downloaded packages are lost** on disconnect!

**Tips to avoid losing work:**
```python
# Save checkpoints to Drive
torch.save(model.state_dict(), '/content/drive/MyDrive/model_checkpoint.pth')

# Save intermediate results
df.to_csv('/content/drive/MyDrive/intermediate_results.csv')

# Install a keepalive (unreliable, not recommended)
# Better: save your work frequently!
```

#### Colab AI Assistant

- Colab now includes an AI coding assistant
- Click the sparkle/star icon to activate
- Can generate code, explain code, and fix errors
- Available in Pro and Pro+ tiers

### 4.9 Colab Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **Ctrl+M B** | Insert cell below |
| **Ctrl+M A** | Insert cell above |
| **Ctrl+M D** | Delete cell |
| **Ctrl+M Y** | Convert to code cell |
| **Ctrl+M M** | Convert to markdown cell |
| **Ctrl+M Z** | Undo cell operation |
| **Ctrl+M H** | Show keyboard shortcuts |
| **Ctrl+M L** | Toggle line numbers |
| **Ctrl+M I** | Interrupt execution |
| **Ctrl+M .** | Restart runtime |
| **Ctrl+Shift+H** | Open command palette |
| **Shift+Enter** | Run cell, move to next |
| **Ctrl+Enter** | Run cell, stay |
| **Alt+Enter** | Run cell, insert below |
| **Ctrl+F9** | Run all cells |
| **Ctrl+Shift+F9** | Run cells before current |
| **Ctrl+/** | Toggle comment |
| **Ctrl+]** | Indent |
| **Ctrl+[** | Dedent |
| **Ctrl+Shift+P** | Command palette |

### 4.10 When to Use Colab vs Local Jupyter

**Use Google Colab when:**
- You need GPU/TPU for machine learning
- You're on a computer without Python installed
- You want to share/collaborate easily
- You're working on a temporary/classroom machine
- You need more RAM than your machine has
- You want pre-installed ML libraries

**Use Local Jupyter when:**
- You need persistent environment (packages stay installed)
- You're working with large local files
- You need more than 12 hours of runtime
- You need custom system dependencies
- You're working offline
- You need full control over the environment
- Privacy-sensitive data (don't upload to cloud)

---

## 5. Running Your First Python Program

### 5.1 In the Terminal

```bash
# Create a file called hello.py
echo 'print("Hello, Python World!")' > hello.py

# Run it
python3 hello.py
# Output: Hello, Python World!
```

### 5.2 In Jupyter Notebook

1. Open Jupyter: `jupyter lab`
2. Click "+" to create a new notebook
3. In the first cell, type:
```python
print("Hello from Jupyter!")
print("Welcome to Python Programming!")
2 + 2  # The last expression's value is displayed
```
4. Press **Shift+Enter** to run

### 5.3 In VS Code

1. Open VS Code
2. Create a new file: `hello.py`
3. Type:
```python
print("Hello from VS Code!")
name = input("What's your name? ")
print(f"Welcome, {name}!")
```
4. Click the Run button (▶) or press F5
5. View output in the integrated terminal

### 5.4 In VS Code Jupyter

1. Create a new file with `.ipynb` extension
2. Or use the Command Palette: "Create: New Jupyter Notebook"
3. Add cells and run just like regular Jupyter
4. VS Code provides IntelliSense even in notebook cells!

### 5.5 In Google Colab

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Click "New Notebook"
3. In the first cell:
```python
print("Hello from Google Colab!")
print("I'm running in the cloud! ☁️")
import sys
print(f"Python version: {sys.version}")
```
4. Press Shift+Enter or click the Play button

---

## 6. Virtual Environments (Brief Preview)

### Why Virtual Environments Matter

Different Python projects may need different package versions. Virtual environments
keep projects isolated from each other.

```bash
# Create a virtual environment
python3 -m venv myenv

# Activate it
source myenv/bin/activate        # macOS/Linux
myenv\Scripts\activate           # Windows

# Your prompt changes to show (myenv)
# Now pip install only affects this environment

# Install packages in this environment
pip install numpy pandas jupyter

# Deactivate when done
deactivate
```

> **Note**: We'll cover virtual environments in detail in the Virtual Environments & Packages chapter. For now,
> installing packages globally with pip is fine for learning.

---

## Jupyter Notebook Quick Reference Card

### Complete Keyboard Shortcut Reference

#### Command Mode (Press Esc first)

| Category | Shortcut | Action |
|----------|----------|--------|
| **Navigation** | ↑ / K | Select cell above |
| | ↓ / J | Select cell below |
| | Ctrl+Home | First cell |
| | Ctrl+End | Last cell |
| **Insert** | A | New cell above |
| | B | New cell below |
| **Edit** | DD | Delete cell |
| | Z | Undo delete |
| | X | Cut cell |
| | C | Copy cell |
| | V | Paste below |
| | Shift+V | Paste above |
| | Shift+M | Merge cells |
| **Type** | Y | Code cell |
| | M | Markdown cell |
| | R | Raw cell |
| | 1-6 | Heading 1-6 |
| **View** | L | Line numbers |
| | O | Toggle output |
| | Shift+O | Scroll output |
| **Execute** | Shift+Enter | Run + next |
| | Ctrl+Enter | Run + stay |
| | Alt+Enter | Run + new below |
| **Kernel** | I, I | Interrupt |
| | 0, 0 | Restart |
| **Other** | S | Save |
| | H | Help |
| | F | Find/Replace |
| | Shift+↑/↓ | Multi-select |

#### Edit Mode (Press Enter first)

| Category | Shortcut | Action |
|----------|----------|--------|
| **Exit** | Esc | Command mode |
| **Complete** | Tab | Autocomplete |
| | Shift+Tab | Tooltip |
| **Edit** | Ctrl+/ | Comment |
| | Ctrl+] | Indent |
| | Ctrl+[ | Dedent |
| | Ctrl+Z | Undo |
| | Ctrl+Y | Redo |
| | Ctrl+A | Select all |
| **Cell** | Ctrl+Shift+- | Split cell |
| | Shift+Enter | Run + next |
| | Ctrl+Enter | Run + stay |
| | Alt+Enter | Run + new below |

---

## Code Examples

### Example 1: First Notebook Workflow

```python
# Cell 1 - Imports (always first!)
import sys
import platform
from datetime import datetime

# Cell 2 - Basic Information
print(f"Python version: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Current time: {datetime.now()}")

# Cell 3 - Simple calculation
radius = 5
pi = 3.14159
area = pi * radius ** 2
print(f"Area of circle with radius {radius}: {area:.2f}")

# Cell 4 - Working with lists
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"Number of fruits: {len(fruits)}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
```

### Example 2: Using Magic Commands

```python
# Cell 1 - Timing code
%time sum(range(1_000_000))

# Cell 2 - Detailed timing
%timeit sum(range(1_000_000))

# Cell 3 - Variable inspection
x = 42
name = "Python"
data = [1, 2, 3, 4, 5]
%whos

# Cell 4 - System information
%pwd
%env HOME
```

### Example 3: Markdown Documentation

```markdown
# My First Data Analysis

## Overview
This notebook explores basic Python operations.

## Key Findings
- Python is **awesome**
- Jupyter makes it *interactive*
- Math works: $E = mc^2$

## Next Steps
1. Learn more data types
2. Practice with exercises
3. Build a project
```

---

## Exercises

### Exercise 1: Environment Verification (Beginner)

**Objective**: Confirm your Python environment is properly set up.

1. Open a terminal and verify Python 3 is installed (`python3 --version`)
2. Verify pip is installed (`pip3 --version`)
3. Install Jupyter (`pip3 install jupyterlab`)
4. Launch JupyterLab (`jupyter lab`)
5. Create a new notebook called `setup_test.ipynb`
6. In the first cell, run:
   ```python
   import sys
   print(f"Success! Python {sys.version} is working!")
   ```
7. Create a markdown cell above with a title: "# Setup Verification"
8. Save the notebook

**Success Criteria**: You see the Python version printed without errors.

---

### Exercise 2: Jupyter Notebook Mastery (Intermediate)

**Objective**: Practice all cell types and keyboard shortcuts.

1. Create a new notebook called `jupyter_practice.ipynb`
2. Create the following structure using ONLY keyboard shortcuts (no mouse!):
   - Markdown cell: `# Jupyter Practice` (Hint: type, then Esc → M → Enter)
   - Code cell: `x = 10; print(x)`
   - Markdown cell: `## Math Operations`
   - Code cell: `print(x * 5)`
   - Code cell: `print(x ** 2)`
3. Run all cells with Shift+Enter
4. Delete the last cell (Esc → DD)
5. Undo the deletion (Z)
6. Insert a new cell above the current one (A)
7. Add a markdown cell with a bulleted list of 3 things you learned
8. Use `%whos` to list all variables
9. Add a cell with a LaTeX equation: `$f(x) = x^2 + 2x + 1$`
10. Restart kernel and Run All to verify everything works

**Success Criteria**: All cells run without error after "Restart & Run All"

---

### Exercise 3: Google Colab Exploration (Advanced)

**Objective**: Use Google Colab's unique features.

1. Open Google Colab and create a new notebook
2. Mount your Google Drive:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
3. Check GPU availability:
   PyTorch is a popular open-source machine learning framework used primarily for developing and training deep learning models. Originally developed by Meta (formerly Facebook), it has become a leading tool for AI researchers and developers due to its flexibility and ease of use.
   ```python
   import torch
   print(f"GPU available: {torch.cuda.is_available()}")
   !nvidia-smi
   ```
4. Install a package that's not pre-installed:
   ```python
   !pip install emoji
   import emoji
   print(emoji.emojize("Python is :thumbs_up:"))
   ```
5. Upload a file from your computer:
   ```python
   from google.colab import files
   uploaded = files.upload()
   ```
6. Create a form-based cell:
   ```python
   #@title Configuration
   name = "Student"  #@param {type:"string"}
   learning_rate = 0.001  #@param {type:"number"}
   print(f"Hello {name}, LR={learning_rate}")
   ```
7. Use the Table of Contents feature (add 3+ markdown headings)
8. Check Colab's revision history (Ctrl+Alt+H)
9. Share the notebook with "Anyone with the link" (view only)
10. Download as .py file (File → Download → Download .py)

**Success Criteria**: All operations complete successfully. Shared link works.

---

### Exercise 4: Shell Commands and Magic (Intermediate)

**Objective**: Master shell commands and magic commands in Jupyter.

1. Create a new notebook
2. Use shell commands to:
   ```python
   !pwd
   !ls
   !echo "Hello from shell" > test_file.txt
   !cat test_file.txt
   ```
3. Capture shell output:
   ```python
   result = !ls
   print(type(result))
   print(result)
   ```
4. Use magic commands:
   ```python
   %time import time; time.sleep(1)
   %timeit [x**2 for x in range(100)]
   %who
   ```
5. Write a file using cell magic:
   ```python
   %%writefile greeting.py
   def greet(name):
       return f"Hello, {name}!"
   
   print(greet("Jupyter"))
   ```
6. Run the file you just wrote:
   ```python
   %run greeting.py
   ```

**Success Criteria**: All magic commands produce expected output.

---

### Exercise 5: Complete Notebook Project (Advanced)

**Objective**: Create a well-structured, documented notebook.

Create a notebook called `my_first_analysis.ipynb` with:

1. **Title cell** (Markdown): "My First Python Analysis"
2. **Introduction** (Markdown): Explain what the notebook does
3. **Setup cell** (Code): Import sys, math, datetime
4. **System Info section** (Markdown + Code): Display system information
5. **Math section** (Markdown + Code): 
   - Calculate area of circles with radii 1-10
   - Use a for loop
   - Include the formula in LaTeX: $A = \pi r^2$
6. **Summary section** (Markdown): Bulleted list of results
7. **Performance section** (Code): Use `%timeit` to compare list comprehension vs for loop
8. Ensure the notebook passes "Restart & Run All" without errors

**Bonus**: Export the notebook as HTML (File → Export as → HTML)

---

## Resources & References

### Official Documentation
- Python Downloads: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Jupyter Documentation: [https://jupyter.org/documentation](https://jupyter.org/documentation)
- JupyterLab Docs: [https://jupyterlab.readthedocs.io/](https://jupyterlab.readthedocs.io/)
- Google Colab: [https://colab.research.google.com/](https://colab.research.google.com/)
- VS Code Python: [https://code.visualstudio.com/docs/python/](https://code.visualstudio.com/docs/python/)

### Tutorials & Guides
- Jupyter Notebook Tutorial: [https://realpython.com/jupyter-notebook-introduction/](https://realpython.com/jupyter-notebook-introduction/)
- Google Colab Guide: [https://colab.research.google.com/notebooks/basic_features_overview.ipynb](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
- Markdown Cheatsheet: [https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/)
- VS Code Tips: [https://code.visualstudio.com/docs/getstarted/tips-and-tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

### Tools
- pyenv (Python Version Manager): [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)
- Homebrew (macOS package manager): [https://brew.sh/](https://brew.sh/)
- VS Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- PyCharm: [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)

### Keyboard Shortcut References
- Jupyter Shortcuts: Help → Keyboard Shortcuts (or press H in Command Mode)
- Colab Shortcuts: Tools → Keyboard Shortcuts
- VS Code Shortcuts: [https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)

---

## Summary

In this chapter, we covered:

1. **Python Installation** - Downloaded and verified Python 3 on your system
2. **VS Code Setup** - Installed VS Code with essential Python extensions
3. **Jupyter Notebooks** - Deep dive into cells, modes, kernels, and magic commands
4. **Google Colab** - Cloud-based notebooks with free GPU access
5. **First Program** - Ran Python in terminal, Jupyter, VS Code, and Colab
6. **Virtual Environments** - Brief preview of project isolation

**Key Takeaway**: Jupyter Notebooks (locally or via Colab) will be our primary tool
for learning Python in this course. Master the keyboard shortcuts now - they'll save
you hours over the coming chapters!

---

