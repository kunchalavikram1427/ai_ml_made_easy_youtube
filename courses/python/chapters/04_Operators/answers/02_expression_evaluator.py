"""
Exercise 2 Solution: Expression Evaluator with Precedence (Intermediate)
=========================================================================
Run: python3 02_expression_evaluator.py

Demonstrates:
- Operator precedence rules
- eval() for expression evaluation (educational only)
- Quiz-style interactive learning
- String formatting for step-by-step explanations
"""

import random


def expression_evaluator():
    """
    A program that demonstrates and teaches operator precedence
    through an interactive quiz format.
    """
    # Define expressions with explanations
    expressions = [
        {
            "expr": "2 + 3 * 4",
            "result": 14,
            "naive": 20,
            "parenthesized": "2 + (3 * 4)",
            "explanation": "* has higher precedence than +",
            "steps": "3 * 4 = 12, then 2 + 12 = 14",
        },
        {
            "expr": "10 - 2 ** 3",
            "result": 2,
            "naive": 512,
            "parenthesized": "10 - (2 ** 3)",
            "explanation": "** has higher precedence than -",
            "steps": "2 ** 3 = 8, then 10 - 8 = 2",
        },
        {
            "expr": "15 // 4 * 3",
            "result": 9,
            "naive": 9,
            "parenthesized": "(15 // 4) * 3",
            "explanation": "// and * have same precedence, evaluated left-to-right",
            "steps": "15 // 4 = 3, then 3 * 3 = 9",
        },
        {
            "expr": "2 ** 3 ** 2",
            "result": 512,
            "naive": 64,
            "parenthesized": "2 ** (3 ** 2)",
            "explanation": "** is right-associative (evaluated right-to-left)",
            "steps": "3 ** 2 = 9, then 2 ** 9 = 512",
        },
        {
            "expr": "5 + 10 % 3",
            "result": 6,
            "naive": 0,
            "parenthesized": "5 + (10 % 3)",
            "explanation": "% has higher precedence than +",
            "steps": "10 % 3 = 1, then 5 + 1 = 6",
        },
        {
            "expr": "not True or True",
            "result": True,
            "naive": False,
            "parenthesized": "(not True) or True",
            "explanation": "'not' has higher precedence than 'or'",
            "steps": "not True = False, then False or True = True",
        },
        {
            "expr": "True or False and False",
            "result": True,
            "naive": False,
            "parenthesized": "True or (False and False)",
            "explanation": "'and' has higher precedence than 'or'",
            "steps": "False and False = False, then True or False = True",
        },
        {
            "expr": "3 * 2 + 5 * 2",
            "result": 16,
            "naive": 16,
            "parenthesized": "(3 * 2) + (5 * 2)",
            "explanation": "* evaluated before +; same-level left-to-right",
            "steps": "3 * 2 = 6, 5 * 2 = 10, then 6 + 10 = 16",
        },
        {
            "expr": "4 + 6 // 3 - 1",
            "result": 5,
            "naive": 2,
            "parenthesized": "4 + (6 // 3) - 1",
            "explanation": "// has higher precedence than + and -",
            "steps": "6 // 3 = 2, then 4 + 2 = 6, then 6 - 1 = 5",
        },
        {
            "expr": "-2 ** 2",
            "result": -4,
            "naive": 4,
            "parenthesized": "-(2 ** 2)",
            "explanation": "** has higher precedence than unary -",
            "steps": "2 ** 2 = 4, then -4",
        },
        {
            "expr": "8 > 5 and 3 < 1",
            "result": False,
            "naive": False,
            "parenthesized": "(8 > 5) and (3 < 1)",
            "explanation": "Comparison operators before logical 'and'",
            "steps": "8 > 5 = True, 3 < 1 = False, True and False = False",
        },
        {
            "expr": "10 - 3 - 2",
            "result": 5,
            "naive": 5,
            "parenthesized": "(10 - 3) - 2",
            "explanation": "Subtraction is left-associative",
            "steps": "10 - 3 = 7, then 7 - 2 = 5",
        },
    ]

    print("=" * 55)
    print("    OPERATOR PRECEDENCE QUIZ")
    print("=" * 55)

    # Phase 1: Learning mode - show examples
    print("\n  --- LEARNING MODE ---")
    print("  Here are some examples showing how precedence works:\n")

    # Show 3 teaching examples
    for i, item in enumerate(expressions[:3], 1):
        print(f"  Example {i}: {item['expr']}")
        print(f"    Result:        {item['result']}")
        print(f"    Parenthesized: {item['parenthesized']}")
        print(f"    Why: {item['explanation']}")
        print(f"    Steps: {item['steps']}")
        print()

    # Phase 2: Quiz mode
    print(f"  {'─' * 50}")
    print("  --- QUIZ MODE ---")
    print("  Guess the result of each expression.\n")

    # Select 5 random questions (skip the teaching examples)
    quiz_pool = expressions[3:]
    random.shuffle(quiz_pool)
    quiz_questions = quiz_pool[:5]

    score = 0

    for i, item in enumerate(quiz_questions, 1):
        print(f"  Question {i}/5: What is the result of  {item['expr']}  ?")

        # Get user answer
        while True:
            answer_input = input("  Your answer: ").strip()

            # Handle boolean answers
            if answer_input.lower() in ("true", "false"):
                user_answer = answer_input.lower() == "true"
                break

            # Handle numeric answers
            try:
                user_answer = eval(answer_input)
                break
            except (ValueError, SyntaxError, NameError):
                print("  Invalid input. Enter a number or True/False.")

        # Check answer
        correct = user_answer == item["result"]
        if correct:
            score += 1
            print(f"  Correct!")
        else:
            print(f"  Wrong! The answer is {item['result']}")

        # Show explanation either way
        print(f"    Explanation: {item['explanation']}")
        print(f"    Evaluation:  {item['parenthesized']} = {item['result']}")
        print(f"    Steps: {item['steps']}")

        if item["naive"] != item["result"]:
            print(f"    Naive (left-to-right) would give: {item['naive']}")
        print()

    # Final score
    print(f"  {'═' * 50}")
    print(f"  FINAL SCORE: {score}/5")
    print(f"  {'═' * 50}")

    if score == 5:
        print("  Perfect! You've mastered operator precedence!")
    elif score >= 3:
        print("  Good job! Review the ones you missed.")
    else:
        print("  Keep practicing! Remember: PEMDAS + Python-specific rules.")

    # Precedence reference
    print(f"\n  --- PRECEDENCE REFERENCE (highest to lowest) ---")
    precedence_table = [
        ("**", "Exponentiation (right-associative)"),
        ("+x, -x, ~x", "Unary plus, minus, bitwise NOT"),
        ("*, /, //, %", "Multiplication, division, modulo"),
        ("+, -", "Addition, subtraction"),
        ("<<, >>", "Bitwise shifts"),
        ("&", "Bitwise AND"),
        ("^", "Bitwise XOR"),
        ("|", "Bitwise OR"),
        ("==, !=, <, >, <=, >=", "Comparisons"),
        ("not", "Logical NOT"),
        ("and", "Logical AND"),
        ("or", "Logical OR"),
    ]

    for i, (ops, desc) in enumerate(precedence_table, 1):
        print(f"    {i:>2}. {ops:<24} {desc}")


# Run the program
if __name__ == "__main__":
    expression_evaluator()
