"""
Exercise 1 Solution: Grade Classifier (Beginner)
==================================================
Run: python3 01_grade_classifier.py

Demonstrates:
- Input validation with try/except
- if/elif/else for grade assignment
- match-case for personalized feedback
- Ternary operator for pass/fail
"""


def grade_classifier():
    """
    Grade classification system.

    Features:
    - Input validation
    - Letter grade assignment (A, B, C, D, F)
    - Personalized feedback using match-case
    - Pass/fail determination using ternary
    """
    print("=" * 45)
    print("       GRADE CLASSIFIER")
    print("=" * 45)

    # Get and validate input
    while True:
        user_input = input("\n  Enter your score (0-100): ")

        # Validate: is it a number?
        try:
            score = float(user_input)
        except ValueError:
            print("  Invalid input! Please enter a number.")
            continue

        # Validate: is it in range?
        if score < 0 or score > 100:
            print("  Score must be between 0 and 100.")
            continue

        break  # Valid input received

    # Assign letter grade with if/elif/else
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    # Pass/fail using ternary operator
    status = "Pass" if score >= 60 else "Fail"

    # Display results
    print(f"\n  {'─' * 35}")
    print(f"  Score:  {score:.0f}%")
    print(f"  Grade:  {grade}")
    print(f"  Status: {status}")
    print(f"  {'─' * 35}")

    # Personalized feedback using match-case
    match grade:
        case "A":
            feedback = "Outstanding! You've mastered this material. Keep it up!"
        case "B":
            feedback = "Great work! You're above average. Push for that A next time!"
        case "C":
            feedback = "Decent job. Review the material to strengthen your understanding."
        case "D":
            feedback = "You passed, but barely. Consider revisiting the fundamentals."
        case "F":
            feedback = "Don't give up! Review the material and try again. You can do it!"

    print(f"  Feedback: {feedback}")

    # Bonus: additional classification using nested conditionals
    print(f"\n  --- Additional Info ---")
    if score == 100:
        print("  Perfect score! Amazing!")
    elif score >= 95:
        print("  Nearly perfect - exceptional work!")
    elif score >= 90:
        print("  A-level performance. Well done!")

    # Honor roll check with logical operators
    if grade in ("A", "B") and score >= 85:
        print("  You qualify for the Honor Roll!")
    elif grade == "B":
        print("  Close to Honor Roll! Aim for 85+ next time.")


# Run the program
if __name__ == "__main__":
    grade_classifier()
