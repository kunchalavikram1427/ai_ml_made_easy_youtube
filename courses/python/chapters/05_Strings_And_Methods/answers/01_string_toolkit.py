"""
Exercise 1 Solution: String Manipulation Toolkit (Beginner)
============================================================
Run: python3 01_string_toolkit.py

Demonstrates:
- String methods: upper(), lower(), count(), replace()
- String slicing and indexing
- Iteration over characters
- Palindrome checking
"""


def string_toolkit(text):
    """
    Perform various string operations and display results.

    Operations:
    1. Print in all uppercase
    2. Print in all lowercase
    3. Print reversed
    4. Count vowels
    5. Replace spaces with underscores
    6. Print first and last character
    7. Check if palindrome
    """
    print(f"\nOriginal string: '{text}'")
    print(f"{'-' * 40}")

    # 1. Uppercase
    print(f"Uppercase: {text.upper()}")

    # 2. Lowercase
    print(f"Lowercase: {text.lower()}")

    # 3. Reversed
    reversed_text = text[::-1]
    print(f"Reversed: {reversed_text}")

    # 4. Count vowels
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    print(f"Vowel count: {vowel_count}")

    # 5. Replace spaces with underscores
    underscored = text.replace(" ", "_")
    print(f"With underscores: {underscored}")

    # 6. First and last character
    if text:
        print(f"First char: {text[0]}, Last char: {text[-1]}")
    else:
        print("First char: (empty), Last char: (empty)")

    # 7. Palindrome check
    # Compare the lowercase, space-stripped version
    cleaned = text.lower().replace(" ", "")
    is_palindrome = cleaned == cleaned[::-1]
    print(f"Is palindrome: {is_palindrome}")

    print()


# Test with various strings
if __name__ == "__main__":
    print("=" * 45)
    print("    STRING MANIPULATION TOOLKIT")
    print("=" * 45)

    string_toolkit("Hello World")
    string_toolkit("racecar")
    string_toolkit("Python Programming")
    string_toolkit("A man a plan a canal Panama")
    string_toolkit("")
