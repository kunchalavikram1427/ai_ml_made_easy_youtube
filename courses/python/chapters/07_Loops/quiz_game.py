"""
Python Quiz Game - Interactive Multiple Choice Trivia
=====================================================

A fun, interactive quiz game that tests your Python knowledge with 10
multiple-choice questions. Features score tracking, a timer for each
question, grade calculation, and a replay option.

How to Run:
    python quiz_game.py

Concepts Demonstrated:
    - Lists of dictionaries (data structures)
    - For/while loops
    - Conditional statements (if/elif/else)
    - Input validation
    - Score calculation
    - Time tracking
    - String formatting

Author: Python YouTube Course
"""

import time
import random


# ─────────────────────────────────────────────────────────────────────────────
# QUIZ DATA - 10 Python Trivia Questions
# ─────────────────────────────────────────────────────────────────────────────

QUESTIONS = [
    {
        "question": "What is the output of: print(type([]) is list)?",
        "options": {"A": "True", "B": "False", "C": "Error", "D": "None"},
        "answer": "A",
        "explanation": "type([]) returns <class 'list'>, which is indeed 'list'."
    },
    {
        "question": "Which keyword is used to create a generator function in Python?",
        "options": {"A": "return", "B": "generate", "C": "yield", "D": "next"},
        "answer": "C",
        "explanation": "The 'yield' keyword turns a function into a generator function."
    },
    {
        "question": "What does 'PEP' stand for in Python?",
        "options": {"A": "Python Enhancement Proposal", "B": "Python Execution Plan",
                    "C": "Python Extension Package", "D": "Python Evaluation Protocol"},
        "answer": "A",
        "explanation": "PEP stands for Python Enhancement Proposal - design documents for Python."
    },
    {
        "question": "What is the result of: 3 * '2' + '1'?",
        "options": {"A": "7", "B": "'221'", "C": "'2221'", "D": "Error"},
        "answer": "C",
        "explanation": "3 * '2' repeats the string to get '222', then + '1' gives '2221'."
    },
    {
        "question": "Which data structure uses key-value pairs?",
        "options": {"A": "List", "B": "Tuple", "C": "Set", "D": "Dictionary"},
        "answer": "D",
        "explanation": "Dictionaries store data as key-value pairs using curly braces {}."
    },
    {
        "question": "What does the 'pass' statement do?",
        "options": {"A": "Exits the loop", "B": "Skips current iteration",
                    "C": "Does nothing (placeholder)", "D": "Passes a value"},
        "answer": "C",
        "explanation": "'pass' is a null operation - a placeholder when syntax requires a statement."
    },
    {
        "question": "Which method removes AND returns the last item from a list?",
        "options": {"A": "remove()", "B": "pop()", "C": "del()", "D": "discard()"},
        "answer": "B",
        "explanation": "pop() removes and returns the last element (or element at given index)."
    },
    {
        "question": "What is a decorator in Python?",
        "options": {"A": "A type of comment", "B": "A function that modifies another function",
                    "C": "A class attribute", "D": "A loop structure"},
        "answer": "B",
        "explanation": "Decorators wrap a function to extend its behavior using @decorator syntax."
    },
    {
        "question": "What will bool('False') return?",
        "options": {"A": "False", "B": "True", "C": "Error", "D": "None"},
        "answer": "B",
        "explanation": "Any non-empty string is truthy, so bool('False') returns True!"
    },
    {
        "question": "Which built-in function creates a sequence of numbers?",
        "options": {"A": "sequence()", "B": "count()", "C": "range()", "D": "numbers()"},
        "answer": "C",
        "explanation": "range() generates a sequence of numbers, commonly used in for loops."
    },
]

# Time limit per question (seconds)
TIME_LIMIT = 15


# ─────────────────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def display_header():
    """Display the game title and instructions."""
    print("\n" + "=" * 60)
    print("        🐍  PYTHON QUIZ GAME  🐍")
    print("=" * 60)
    print(f"\n  📋 {len(QUESTIONS)} questions | Multiple choice (A/B/C/D)")
    print(f"  ⏱️  {TIME_LIMIT} seconds per question")
    print("  💡 Correct answers shown for wrong guesses")
    print("\n" + "=" * 60)


def calculate_grade(percentage):
    """Return letter grade based on percentage score."""
    if percentage >= 90:
        return "A", "🌟 Excellent! You're a Python master!"
    elif percentage >= 80:
        return "B", "👏 Great job! Strong Python knowledge!"
    elif percentage >= 70:
        return "C", "👍 Good effort! Keep studying!"
    elif percentage >= 60:
        return "D", "📚 Passing, but review the material."
    else:
        return "F", "💪 Don't give up! Practice makes perfect!"


def ask_question(question_data, question_number):
    """
    Display a question and get the player's answer.
    Returns: (is_correct, time_taken, user_answer)
    """
    print(f"\n{'─' * 60}")
    print(f"  Question {question_number}/{len(QUESTIONS)}")
    print(f"{'─' * 60}")
    print(f"\n  {question_data['question']}\n")

    # Display options
    for letter, text in question_data["options"].items():
        print(f"    {letter}) {text}")

    print(f"\n  ⏱️  You have {TIME_LIMIT} seconds!")

    # Get answer with timing
    start_time = time.time()

    while True:
        user_answer = input("\n  Your answer (A/B/C/D): ").strip().upper()
        elapsed = time.time() - start_time

        if elapsed > TIME_LIMIT:
            print(f"\n  ⏰ Time's up! ({elapsed:.1f}s)")
            return False, elapsed, "TIMEOUT"

        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("  ❌ Invalid! Please enter A, B, C, or D.")

    time_taken = time.time() - start_time
    is_correct = user_answer == question_data["answer"]

    # Show result
    if is_correct:
        print(f"\n  ✅ Correct! ({time_taken:.1f}s)")
    else:
        correct = question_data["answer"]
        correct_text = question_data["options"][correct]
        print(f"\n  ❌ Wrong! The correct answer was: {correct}) {correct_text}")
        print(f"  💡 {question_data['explanation']}")

    return is_correct, time_taken, user_answer


def show_results(score, total, times, wrong_questions):
    """Display the final results and grade."""
    percentage = (score / total) * 100
    grade, message = calculate_grade(percentage)
    avg_time = sum(times) / len(times) if times else 0

    print("\n" + "=" * 60)
    print("        📊  FINAL RESULTS  📊")
    print("=" * 60)
    print(f"\n  Score:      {score}/{total} ({percentage:.0f}%)")
    print(f"  Grade:      {grade}")
    print(f"  Avg Time:   {avg_time:.1f}s per question")
    print(f"  Total Time: {sum(times):.1f}s")
    print(f"\n  {message}")

    # Show questions that were answered incorrectly
    if wrong_questions:
        print(f"\n{'─' * 60}")
        print("  📝 Review - Questions you missed:")
        print(f"{'─' * 60}")
        for q in wrong_questions:
            correct = q["answer"]
            print(f"\n  Q: {q['question']}")
            print(f"  ✅ Answer: {correct}) {q['options'][correct]}")
            print(f"  💡 {q['explanation']}")

    print("\n" + "=" * 60)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN GAME LOOP
# ─────────────────────────────────────────────────────────────────────────────

def play_quiz():
    """Run one round of the quiz game."""
    display_header()

    input("\n  Press Enter to start the quiz...")

    # Shuffle questions for variety on replay
    shuffled_questions = random.sample(QUESTIONS, len(QUESTIONS))

    score = 0
    times = []
    wrong_questions = []

    for i, question in enumerate(shuffled_questions, 1):
        is_correct, time_taken, user_answer = ask_question(question, i)

        times.append(time_taken)
        if is_correct:
            score += 1
        else:
            wrong_questions.append(question)

    show_results(score, len(QUESTIONS), times, wrong_questions)


def main():
    """Main entry point with replay loop."""
    print("\n  Welcome to the Python Quiz Game!")

    while True:
        play_quiz()

        # Ask to replay
        print("\n  Would you like to play again?")
        replay = input("  Enter 'y' for yes, anything else to quit: ").strip().lower()

        if replay != 'y':
            print("\n  Thanks for playing! Keep learning Python! 🐍\n")
            break


if __name__ == "__main__":
    main()
