"""
Exercise 2 Solution: Python Quiz Game (Intermediate)
=====================================================
Run: python3 02_quiz_game.py

Demonstrates:
- if/elif/else for answer checking
- match-case for performance-based messages
- Input validation with conditionals
- Score tracking with conditional logic
- Ternary operators for concise output
"""


def quiz_game():
    """
    Interactive Python quiz game with multiple-choice questions.

    Features:
    - 5 multiple-choice questions
    - if/elif/else for answer validation
    - Score tracking
    - match-case for final performance message
    - Input validation
    - Replay option
    """
    # Quiz data: list of dictionaries
    questions = [
        {
            "question": "What is the output of: print(type(3.14))?",
            "options": ["a) <class 'int'>", "b) <class 'float'>",
                        "c) <class 'str'>", "d) <class 'number'>"],
            "answer": "b",
            "explanation": "3.14 is a floating-point number, so type() returns <class 'float'>."
        },
        {
            "question": "Which keyword is used for pattern matching in Python 3.10+?",
            "options": ["a) switch", "b) case", "c) match", "d) select"],
            "answer": "c",
            "explanation": "Python 3.10 introduced 'match' for structural pattern matching."
        },
        {
            "question": "What does the 'elif' keyword stand for?",
            "options": ["a) else finally", "b) else if",
                        "c) element if", "d) evaluate if"],
            "answer": "b",
            "explanation": "'elif' is short for 'else if' — it checks another condition."
        },
        {
            "question": "What is the ternary operator syntax in Python?",
            "options": ["a) condition ? true : false",
                        "b) true if condition else false",
                        "c) if condition then true else false",
                        "d) condition -> true | false"],
            "answer": "b",
            "explanation": "Python's ternary: value_if_true if condition else value_if_false"
        },
        {
            "question": "What is the wildcard pattern in match-case?",
            "options": ["a) *", "b) ...", "c) _", "d) default"],
            "answer": "c",
            "explanation": "The underscore '_' is the wildcard/catch-all pattern in match-case."
        },
    ]

    print("=" * 50)
    print("         PYTHON QUIZ GAME")
    print("=" * 50)

    while True:  # Replay loop
        score = 0
        total = len(questions)

        print(f"\n  You'll be asked {total} questions.")
        print(f"  Enter a, b, c, or d for your answer.\n")
        print(f"  {'─' * 44}")

        for i, q in enumerate(questions, 1):
            print(f"\n  Question {i}/{total}:")
            print(f"  {q['question']}\n")

            for option in q["options"]:
                print(f"    {option}")

            # Input validation loop
            while True:
                answer = input(f"\n  Your answer (a/b/c/d): ").strip().lower()

                if answer in ("a", "b", "c", "d"):
                    break
                else:
                    print("  Invalid! Please enter a, b, c, or d.")

            # Check answer with if/else
            if answer == q["answer"]:
                print("  Correct!")
                score += 1
            else:
                print(f"  Wrong! The answer was: {q['answer']}")
                print(f"  {q['explanation']}")

        # Calculate percentage
        percentage = (score / total) * 100

        # Display results
        print(f"\n  {'═' * 44}")
        print(f"  RESULTS")
        print(f"  {'─' * 44}")
        print(f"  Score: {score}/{total} ({percentage:.0f}%)")

        # Grade using if/elif/else
        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"

        # Pass/fail with ternary
        result = "PASSED" if percentage >= 60 else "FAILED"
        print(f"  Grade: {grade} | {result}")

        # Performance message using match-case
        match grade:
            case "A":
                message = "Excellent! You really know your Python!"
            case "B":
                message = "Great job! You have a solid understanding."
            case "C":
                message = "Not bad! Review the topics you missed."
            case "D":
                message = "You passed, but there's room to improve."
            case "F":
                message = "Keep studying! Practice makes perfect."

        print(f"  {message}")
        print(f"  {'═' * 44}")

        # Replay option
        play_again = input("\n  Play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("\n  Thanks for playing! Keep learning Python!")
            break


# Run the game
if __name__ == "__main__":
    quiz_game()
