"""
Exercise 2 Solution: Text Formatter (Intermediate)
====================================================
Run: python3 02_text_formatter.py

Demonstrates:
- Word wrapping logic
- String alignment: ljust(), rjust(), center()
- String repetition for borders
- split() and join() for word processing
"""


def format_paragraph(text, width=50, align="center", border_char="*"):
    """
    Format text into a bordered, aligned paragraph.

    Args:
        text: The input text string
        width: Maximum width of each line (default 50)
        align: 'left', 'right', or 'center' (default 'center')
        border_char: Character for the border (default '*')
    """
    # Step 1: Word wrap the text
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        # Check if adding this word exceeds the width
        # Account for space between words and border padding (2 chars each side)
        inner_width = width - 4  # 1 border + 1 space on each side

        if current_length + len(word) + (1 if current_line else 0) <= inner_width:
            current_line.append(word)
            current_length += len(word) + (1 if len(current_line) > 1 else 0)
        else:
            # Save current line and start new one
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)

    # Don't forget the last line
    if current_line:
        lines.append(" ".join(current_line))

    # Step 2: Apply alignment to each line
    inner_width = width - 4  # Space inside borders
    aligned_lines = []

    for line in lines:
        if align == "left":
            aligned_lines.append(line.ljust(inner_width))
        elif align == "right":
            aligned_lines.append(line.rjust(inner_width))
        elif align == "center":
            aligned_lines.append(line.center(inner_width))
        else:
            aligned_lines.append(line.ljust(inner_width))

    # Step 3: Add border
    top_bottom = border_char * width
    print(top_bottom)

    for line in aligned_lines:
        print(f"{border_char} {line} {border_char}")

    print(top_bottom)


def demo():
    """Demonstrate the text formatter with various options."""
    sample = (
        "Python is an interpreted, high-level, general-purpose programming language. "
        "Created by Guido van Rossum and first released in 1991, Python's design "
        "philosophy emphasizes code readability."
    )

    print("=" * 55)
    print("    TEXT FORMATTER DEMO")
    print("=" * 55)

    # Center aligned
    print("\n--- Center Aligned (width=40) ---\n")
    format_paragraph(sample, width=40, align="center")

    # Left aligned
    print("\n--- Left Aligned (width=40) ---\n")
    format_paragraph(sample, width=40, align="left")

    # Right aligned
    print("\n--- Right Aligned (width=40) ---\n")
    format_paragraph(sample, width=40, align="right")

    # Different border character
    print("\n--- Custom Border (width=50, border='#') ---\n")
    format_paragraph(sample, width=50, align="center", border_char="#")

    # Wider format
    print("\n--- Wide Format (width=60, border='-') ---\n")
    format_paragraph(sample, width=60, align="left", border_char="-")

    # Short text
    print("\n--- Short Text ---\n")
    format_paragraph("Hello, World!", width=30, align="center")


# Run the demo
if __name__ == "__main__":
    demo()
