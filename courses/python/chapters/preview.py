"""
=============================================================================
PREVIEW: Why You Need to Learn Python - A Complete Demo
=============================================================================

This single file demonstrates WHY you need to learn variables, functions,
loops, classes, APIs, file handling, and more. It's a real-world application
that fetches data from an API, processes it, and generates a report.

Run: python3 preview.py

This program:
1. Uses VARIABLES to store configuration
2. Uses FUNCTIONS to organize reusable logic
3. Uses LOOPS to process multiple items
4. Uses CONDITIONALS to make decisions
5. Uses CLASSES to model real-world objects
6. Uses EXCEPTION HANDLING to handle errors gracefully
7. Uses FILE HANDLING to save results
8. Uses JSON to parse API responses
9. Uses the REQUESTS library to call APIs
10. Uses LIST COMPREHENSIONS for clean data processing
11. Uses F-STRINGS for readable output
12. Uses DECORATORS for timing functions
13. Uses ARGS/KWARGS for flexible functions

After watching all videos in this course, you'll understand every line here!
=============================================================================
"""

import json
import time
import os
from datetime import datetime
from functools import wraps

# Try to import requests - show graceful error handling
try:
    import requests
except ImportError:
    print("Installing 'requests' library...")
    os.system("pip install requests")
    import requests


# =============================================================================
# CONCEPT 1: VARIABLES & DATA TYPES
# =============================================================================
# Variables store data - numbers, text, lists, and more

APP_NAME = "Python Course Preview"        # String (constant convention)
VERSION = 1.0                             # Float
MAX_RESULTS = 5                           # Integer
SHOW_DETAILS = True                       # Boolean
API_URL = "https://api.github.com"        # String (API endpoint)
SEARCH_TOPICS = ["python", "machine-learning", "fastapi"]  # List


# =============================================================================
# CONCEPT 2: DECORATORS (Advanced Functions)
# =============================================================================
# A decorator adds functionality to existing functions without modifying them

def timer(func):
    """Decorator that measures how long a function takes to run."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"    [{func.__name__}] completed in {elapsed:.2f}s")
        return result
    return wrapper


def retry(max_attempts=3, delay=1):
    """Decorator that retries a function if it fails."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"    Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator


# =============================================================================
# CONCEPT 3: CLASSES (Object-Oriented Programming)
# =============================================================================
# Classes model real-world things with attributes and behaviors

class Repository:
    """Represents a GitHub repository - a real-world object modeled in code."""

    def __init__(self, name: str, stars: int, language: str, description: str, url: str):
        """Constructor - called when creating a new Repository object."""
        self.name = name
        self.stars = stars
        self.language = language or "Unknown"
        self.description = description or "No description"
        self.url = url
        self.created_at = datetime.now()

    def __str__(self):
        """String representation - what happens when you print() this object."""
        return f"{self.name} ({self.language}) - {self.stars} stars"

    def __repr__(self):
        """Developer representation - for debugging."""
        return f"Repository(name='{self.name}', stars={self.stars})"

    def __lt__(self, other):
        """Less than comparison - allows sorting repositories by stars."""
        return self.stars < other.stars

    @property
    def popularity(self):
        """Property decorator - access like an attribute, computed like a method."""
        if self.stars > 50000:
            return "Very Popular"
        elif self.stars > 10000:
            return "Popular"
        elif self.stars > 1000:
            return "Growing"
        else:
            return "New"

    def to_dict(self):
        """Convert to dictionary - useful for JSON serialization."""
        return {
            "name": self.name,
            "stars": self.stars,
            "language": self.language,
            "description": self.description,
            "url": self.url,
            "popularity": self.popularity
        }


class GitHubExplorer:
    """A class that interacts with the GitHub API to find trending repos."""

    def __init__(self, base_url: str = API_URL):
        """Initialize with API configuration."""
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "PythonCoursePreview/1.0"
        })
        self.repositories = []

    @timer
    @retry(max_attempts=3, delay=2)
    def search_repos(self, topic: str, max_results: int = MAX_RESULTS) -> list:
        """
        Search GitHub for repositories by topic.

        Demonstrates:
        - API calls with requests
        - JSON parsing
        - List comprehensions
        - Error handling
        """
        # CONCEPT: API Call with parameters
        params = {
            "q": f"topic:{topic}",
            "sort": "stars",
            "order": "desc",
            "per_page": max_results
        }

        # CONCEPT: Making HTTP requests
        response = self.session.get(
            f"{self.base_url}/search/repositories",
            params=params,
            timeout=10
        )

        # CONCEPT: Exception handling for HTTP errors
        response.raise_for_status()

        # CONCEPT: JSON parsing
        data = response.json()

        # CONCEPT: List comprehension to create objects from API data
        repos = [
            Repository(
                name=item["full_name"],
                stars=item["stargazers_count"],
                language=item.get("language"),
                description=item.get("description"),
                url=item["html_url"]
            )
            for item in data.get("items", [])
        ]

        self.repositories.extend(repos)
        return repos

    def get_top_repos(self, n: int = 10) -> list:
        """Get top N repositories sorted by stars (uses __lt__ dunder method)."""
        # CONCEPT: sorted() uses our __lt__ method defined in Repository class
        return sorted(self.repositories, reverse=True)[:n]

    def get_language_stats(self) -> dict:
        """
        Get statistics about programming languages.

        Demonstrates: Dictionary comprehension, Counter pattern
        """
        # CONCEPT: Dictionary building with loops
        language_count = {}
        for repo in self.repositories:
            language_count[repo.language] = language_count.get(repo.language, 0) + 1

        # CONCEPT: Sorting dictionary by values
        return dict(sorted(language_count.items(), key=lambda x: x[1], reverse=True))


# =============================================================================
# CONCEPT 4: FUNCTIONS with *args, **kwargs
# =============================================================================

def generate_report(*sections, title: str = "Report", **metadata):
    """
    Generate a formatted report.

    Demonstrates:
    - *args for variable positional arguments
    - **kwargs for variable keyword arguments
    - String formatting
    - Loops and conditionals
    """
    # CONCEPT: f-strings and string multiplication
    separator = "=" * 60
    report_lines = [
        separator,
        f"  {title}",
        separator,
        ""
    ]

    # CONCEPT: Processing **kwargs
    if metadata:
        report_lines.append("  Metadata:")
        for key, value in metadata.items():
            report_lines.append(f"    {key}: {value}")
        report_lines.append("")

    # CONCEPT: Processing *args with enumerate
    for i, section in enumerate(sections, 1):
        report_lines.append(f"  Section {i}:")
        report_lines.append(f"  {section}")
        report_lines.append("")

    report_lines.append(separator)
    return "\n".join(report_lines)


def format_number(n: int) -> str:
    """Format large numbers for readability (e.g., 1000 -> 1K)."""
    # CONCEPT: Conditionals for data transformation
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n/1_000:.1f}K"
    return str(n)


# =============================================================================
# CONCEPT 5: FILE HANDLING
# =============================================================================

@timer
def save_results(repos: list, filename: str = "github_trending.json"):
    """
    Save results to a JSON file.

    Demonstrates:
    - File handling with context managers (with statement)
    - JSON serialization
    - List comprehension
    """
    # CONCEPT: Context manager ensures file is properly closed
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    data = {
        "generated_at": datetime.now().isoformat(),
        "total_repos": len(repos),
        "repositories": [repo.to_dict() for repo in repos]
    }

    # CONCEPT: Writing JSON to file
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"    Results saved to: {filepath}")
    return filepath


# =============================================================================
# MAIN PROGRAM - Putting it all together!
# =============================================================================

def main():
    """
    Main function - the entry point of our program.

    This ties everything together:
    Variables + Functions + Loops + Classes + APIs + Files + Error Handling
    """
    print(f"\n{'*' * 60}")
    print(f"  {APP_NAME} v{VERSION}")
    print(f"  Demonstrating ALL Python concepts in one program!")
    print(f"{'*' * 60}\n")

    # CONCEPT: Object instantiation
    explorer = GitHubExplorer()

    print("[1] Searching GitHub for trending repositories...\n")

    # CONCEPT: Loop through topics
    for topic in SEARCH_TOPICS:
        print(f"  Searching for: '{topic}'...")
        try:
            repos = explorer.search_repos(topic)
            print(f"    Found {len(repos)} repositories\n")
        except requests.exceptions.RequestException as e:
            # CONCEPT: Exception handling
            print(f"    Error searching '{topic}': {e}\n")
            continue

    # CONCEPT: Using class methods
    print(f"\n[2] Analyzing {len(explorer.repositories)} repositories...\n")

    # Get top repos (uses sorting with __lt__)
    top_repos = explorer.get_top_repos(10)

    # CONCEPT: Formatted output with f-strings
    print("  Top Repositories by Stars:")
    print("  " + "-" * 56)
    print(f"  {'#':<3} {'Repository':<30} {'Stars':<10} {'Status'}")
    print("  " + "-" * 56)

    # CONCEPT: enumerate() in loops
    for i, repo in enumerate(top_repos, 1):
        stars_formatted = format_number(repo.stars)
        print(f"  {i:<3} {repo.name:<30} {stars_formatted:<10} {repo.popularity}")

    # CONCEPT: Dictionary operations
    print(f"\n\n[3] Language Statistics:\n")
    lang_stats = explorer.get_language_stats()

    for language, count in lang_stats.items():
        bar = "#" * (count * 3)  # Simple visualization
        print(f"  {language:<15} {bar} ({count})")

    # CONCEPT: Generating report with *args and **kwargs
    print(f"\n\n[4] Generating Report...\n")

    section1 = f"Found {len(explorer.repositories)} repos across {len(SEARCH_TOPICS)} topics"
    section2 = f"Top repo: {top_repos[0].name} with {format_number(top_repos[0].stars)} stars"
    section3 = f"Most common language: {list(lang_stats.keys())[0]}"

    report = generate_report(
        section1, section2, section3,
        title="GitHub Trending Report",
        author="Python Course Student",
        date=datetime.now().strftime("%Y-%m-%d %H:%M"),
        version=VERSION
    )
    print(report)

    # CONCEPT: File handling
    print("\n[5] Saving results to file...\n")
    save_results(top_repos)

    # Final summary
    print(f"\n{'*' * 60}")
    print("  CONCEPTS USED IN THIS PROGRAM:")
    print(f"{'*' * 60}")

    concepts = [
        ("Variables & Data Types", "Strings, ints, floats, lists, booleans"),
        ("Operators", "Comparison, membership, arithmetic"),
        ("Strings & F-strings", "Formatting, methods, concatenation"),
        ("Control Flow", "if/elif/else, for loops, continue"),
        ("Data Structures", "Lists, dictionaries, comprehensions"),
        ("Functions", "def, return, default params, *args, **kwargs"),
        ("Decorators", "@timer, @retry with arguments"),
        ("Classes & OOP", "Classes, __init__, properties, dunder methods"),
        ("Exception Handling", "try/except, raise, custom handling"),
        ("File Handling", "open(), with statement, JSON write"),
        ("JSON", "json.dumps(), json.load(), serialization"),
        ("Requests & APIs", "HTTP GET, headers, response parsing"),
        ("Modules & Imports", "os, json, time, datetime, requests"),
    ]

    for concept, usage in concepts:
        print(f"  {concept:<25} -> {usage}")

    print(f"\n{'*' * 60}")
    print("  Learn all these concepts in our Python course!")
    print("  Each video builds on the previous one.")
    print("  By the end, you'll write programs like this easily!")
    print(f"{'*' * 60}\n")


# CONCEPT: The main guard - standard Python pattern
if __name__ == "__main__":
    main()
