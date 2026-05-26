"""
Exercise 2 Solution: Number Guessing Game (Intermediate)
=========================================================
Run: python3 02_number_guessing_game.py

Demonstrates:
- while loop for game rounds
- for loop with range for attempt tracking
- break for early exit on correct guess
- continue for invalid input handling
- enumerate for attempt counting
- Infinite loop with break for replay
"""

import random


def number_guessing_game():
    """
    Number guessing game with difficulty levels and scoring.

    Features:
    - Multiple difficulty levels
    - Hint system (higher/lower + proximity hints)
    - Score tracking
    - High score persistence (within session)
    - Input validation
    - Play again option
    """
    high_scores = {"easy": None, "medium": None, "hard": None}

    print("=" * 50)
    print("       NUMBER GUESSING GAME")
    print("=" * 50)

    while True:  # Replay loop
        # Difficulty selection
        print("\n  Select difficulty:")
        print("    1. Easy   (15 attempts, range 1-50)")
        print("    2. Medium (10 attempts, range 1-100)")
        print("    3. Hard   (5 attempts,  range 1-200)")

        # Validate difficulty choice
        while True:
            diff_choice = input("  Choice (1/2/3): ").strip()
            if diff_choice in ("1", "2", "3"):
                break
            print("  Invalid! Enter 1, 2, or 3.")

        # Set parameters based on difficulty
        if diff_choice == "1":
            max_attempts = 15
            max_number = 50
            difficulty = "easy"
        elif diff_choice == "2":
            max_attempts = 10
            max_number = 100
            difficulty = "medium"
        else:
            max_attempts = 5
            max_number = 200
            difficulty = "hard"

        # Generate secret number
        secret = random.randint(1, max_number)

        print(f"\n  I'm thinking of a number between 1 and {max_number}...")
        print(f"  You have {max_attempts} attempts.")
        print(f"  {'─' * 44}")

        # Game loop
        won = False
        for attempt in range(1, max_attempts + 1):
            # Get and validate guess
            while True:
                guess_input = input(f"\n  Attempt {attempt}/{max_attempts} - Your guess: ").strip()

                # Validate it's a number
                if not guess_input.isdigit():
                    print(f"  Please enter a number between 1 and {max_number}.")
                    continue

                guess = int(guess_input)

                # Validate range
                if guess < 1 or guess > max_number:
                    print(f"  Out of range! Enter a number between 1 and {max_number}.")
                    continue

                break  # Valid guess

            # Check guess
            if guess == secret:
                won = True
                print(f"\n  Correct! The number was {secret}!")
                break
            elif guess < secret:
                difference = secret - guess
                # Proximity hints
                if difference <= 5:
                    print("  Very close! Just a tiny bit higher!")
                elif difference <= 15:
                    print("  Too low! Try higher.")
                else:
                    print("  Way too low! Go much higher.")
            else:
                difference = guess - secret
                if difference <= 5:
                    print("  Very close! Just a tiny bit lower!")
                elif difference <= 15:
                    print("  Too high! Try lower.")
                else:
                    print("  Way too high! Go much lower.")

            # Show remaining attempts
            remaining = max_attempts - attempt
            if remaining > 0 and not won:
                print(f"  ({remaining} {'attempt' if remaining == 1 else 'attempts'} remaining)")

        # Game over
        print(f"\n  {'═' * 44}")

        if won:
            # Calculate score: more points for fewer attempts
            score = max_attempts - attempt + 1
            max_score = max_attempts
            percentage = (score / max_score) * 100

            print(f"  YOU WIN!")
            print(f"  Score: {score}/{max_score} | Attempts used: {attempt}")

            # Rating based on performance
            if attempt == 1:
                print("  Incredible luck! First try!")
            elif attempt <= max_attempts // 3:
                print("  Excellent guessing strategy!")
            elif attempt <= max_attempts // 2:
                print("  Good job! Solid approach.")
            else:
                print("  Close call, but you got it!")

            # Update high score
            current_high = high_scores[difficulty]
            if current_high is None or score > current_high:
                high_scores[difficulty] = score
                print(f"  NEW HIGH SCORE for {difficulty.title()} difficulty!")
            elif score == current_high:
                print(f"  Tied your high score!")

        else:
            print(f"  GAME OVER!")
            print(f"  The number was: {secret}")
            print(f"  Better luck next time!")

        # Show high scores
        print(f"\n  --- High Scores ---")
        for diff, hs in high_scores.items():
            score_display = str(hs) if hs is not None else "-"
            print(f"    {diff.title():8s}: {score_display}")

        print(f"  {'═' * 44}")

        # Play again?
        again = input("\n  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye!")
            break


# Run the game
if __name__ == "__main__":
    number_guessing_game()
