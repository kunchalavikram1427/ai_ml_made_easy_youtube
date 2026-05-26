"""
Countdown Timer & Number Guessing Game
========================================
Run: python3 countdown_timer.py

This demonstrates control flow concepts:
- while loops with conditions
- for loops with range
- if/elif/else branching
- break and continue statements
- Nested loops
- time.sleep() for timing
- random module for game logic
"""

import time
import random
import sys

# ============================================================
# COUNTDOWN TIMER
# ============================================================

def countdown_timer():
    """
    A visual countdown timer with progress bar.
    Demonstrates: while loop, string formatting, time.sleep()
    """
    print("\n┌──────────────────────────────────────────┐")
    print("│  ⏱️  COUNTDOWN TIMER                      │")
    print("└──────────────────────────────────────────┘")

    try:
        total = int(input("\n  Enter seconds to count down: "))
        if total <= 0:
            print("  ❌ Please enter a positive number!")
            return
    except ValueError:
        print("  ❌ Invalid input!")
        return

    print(f"\n  Starting {total} second countdown...\n")

    remaining = total
    while remaining > 0:
        # Calculate progress
        elapsed = total - remaining
        progress = elapsed / total
        bar_length = 30
        filled = int(bar_length * progress)
        bar = "█" * filled + "░" * (bar_length - filled)

        # Format time display
        mins, secs = divmod(remaining, 60)
        time_str = f"{mins:02d}:{secs:02d}"

        # Print on same line (\r returns cursor to start)
        sys.stdout.write(f"\r  [{bar}] {time_str} remaining ")
        sys.stdout.flush()

        time.sleep(1)
        remaining -= 1

    # Final state
    bar = "█" * bar_length
    sys.stdout.write(f"\r  [{bar}] 00:00 DONE!       \n")
    print("\n  🔔 TIME'S UP! 🔔")
    print("  " + "🎉 " * 10)


# ============================================================
# NUMBER GUESSING GAME
# ============================================================

def guessing_game():
    """
    Number guessing game with difficulty levels and hints.
    Demonstrates: if/elif/else, while loop, break, comparison operators
    """
    print("\n┌──────────────────────────────────────────┐")
    print("│  🎯 NUMBER GUESSING GAME                 │")
    print("└──────────────────────────────────────────┘")

    # Difficulty selection
    print("""
  Choose difficulty:
    [1] Easy   (1-50,   10 guesses)
    [2] Medium (1-100,   7 guesses)
    [3] Hard   (1-500,  10 guesses)
    [4] Expert (1-1000,  10 guesses)
""")

    difficulty = input("  Select (1-4): ").strip()

    settings = {
        '1': (50, 10, "Easy"),
        '2': (100, 7, "Medium"),
        '3': (500, 10, "Hard"),
        '4': (1000, 10, "Expert"),
    }

    if difficulty not in settings:
        print("  Defaulting to Medium.")
        difficulty = '2'

    max_num, max_guesses, level_name = settings[difficulty]
    secret = random.randint(1, max_num)
    guesses_taken = 0
    guess_history = []

    print(f"\n  🎮 {level_name} Mode: Guess a number between 1 and {max_num}")
    print(f"  📝 You have {max_guesses} guesses. Let's go!\n")

    while guesses_taken < max_guesses:
        remaining = max_guesses - guesses_taken
        prompt = f"  Guess #{guesses_taken + 1} ({remaining} left): "

        try:
            guess = int(input(prompt))
        except ValueError:
            print("  ⚠️  Please enter a valid number!")
            continue  # Don't count invalid input

        guesses_taken += 1
        guess_history.append(guess)

        # Check the guess
        if guess == secret:
            print(f"\n  🎉 CORRECT! The number was {secret}!")
            print(f"  🏆 You got it in {guesses_taken} guess{'es' if guesses_taken > 1 else ''}!")

            # Rating based on performance
            if guesses_taken == 1:
                print("  🌟 INCREDIBLE! First try!")
            elif guesses_taken <= max_guesses // 3:
                print("  🌟 AMAZING! You're a natural!")
            elif guesses_taken <= max_guesses // 2:
                print("  👏 Great job!")
            else:
                print("  😅 Close call, but you made it!")
            break

        elif guess < secret:
            diff = secret - guess
            if diff > max_num // 4:
                print("  📈 WAY too low! Go much higher.")
            elif diff > max_num // 10:
                print("  📈 Too low. Go higher.")
            elif diff > 2:
                print("  📈 Getting warm! Go a bit higher.")
            else:
                print("  📈 SO close! Just a tiny bit higher!")
        else:
            diff = guess - secret
            if diff > max_num // 4:
                print("  📉 WAY too high! Go much lower.")
            elif diff > max_num // 10:
                print("  📉 Too high. Go lower.")
            elif diff > 2:
                print("  📉 Getting warm! Go a bit lower.")
            else:
                print("  📉 SO close! Just a tiny bit lower!")

        # Bonus hint every 3 guesses
        if guesses_taken % 3 == 0 and guesses_taken < max_guesses:
            if guess < secret:
                hint_low = max(guess, secret - max_num // 5)
                print(f"  💡 Hint: The number is between {hint_low} and {min(secret + max_num // 10, max_num)}")
            else:
                hint_high = min(guess, secret + max_num // 5)
                print(f"  💡 Hint: The number is between {max(secret - max_num // 10, 1)} and {hint_high}")

    else:
        # while loop exhausted without break (no correct guess)
        print(f"\n  💀 Game Over! The number was {secret}.")
        print(f"  Your guesses: {guess_history}")

    # Play again?
    print()
    again = input("  Play again? (y/n): ").lower()
    if again == 'y':
        guessing_game()


# ============================================================
# FIZZBUZZ CHALLENGE (Bonus)
# ============================================================

def fizzbuzz():
    """
    Classic FizzBuzz - demonstrates if/elif/else with modulo.
    """
    print("\n┌──────────────────────────────────────────┐")
    print("│  🍺 FIZZBUZZ (Classic Interview Question) │")
    print("└──────────────────────────────────────────┘")
    print("\n  Rules: Print numbers 1-50")
    print("    - Divisible by 3? Print 'Fizz'")
    print("    - Divisible by 5? Print 'Buzz'")
    print("    - Divisible by both? Print 'FizzBuzz'\n")

    results = []
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))

    # Print in rows of 10
    for i in range(0, len(results), 10):
        row = results[i:i+10]
        print("  " + " | ".join(f"{item:<8}" for item in row))

    input("\n  Press Enter to return to menu...")


# ============================================================
# PATTERN PRINTER (Nested Loops Demo)
# ============================================================

def pattern_printer():
    """Demonstrate nested loops with visual patterns."""
    print("\n┌──────────────────────────────────────────┐")
    print("│  🔷 PATTERN PRINTER (Nested Loops)       │")
    print("└──────────────────────────────────────────┘")

    try:
        n = int(input("\n  Enter size (3-10): "))
        n = max(3, min(10, n))  # Clamp between 3 and 10
    except ValueError:
        n = 5

    # Triangle
    print(f"\n  --- Right Triangle (size={n}) ---")
    for i in range(1, n + 1):
        print("  " + "* " * i)

    # Pyramid
    print(f"\n  --- Pyramid (size={n}) ---")
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        print(f"  {spaces}{stars}")

    # Diamond
    print(f"\n  --- Diamond (size={n}) ---")
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        print(f"  {spaces}{stars}")
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        stars = "* " * i
        print(f"  {spaces}{stars}")

    # Number pattern
    print(f"\n  --- Number Pattern ---")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    input("\n  Press Enter to return to menu...")


# ============================================================
# MAIN MENU
# ============================================================

def main():
    """Main menu demonstrating control flow concepts."""
    while True:
        print("\n" + "=" * 50)
        print("  🎮 CONTROL FLOW PLAYGROUND")
        print("=" * 50)
        print("""
  [1] ⏱️  Countdown Timer    (while loop)
  [2] 🎯 Number Guessing    (if/else, while, break)
  [3] 🍺 FizzBuzz           (for loop, if/elif/else)
  [4] 🔷 Pattern Printer    (nested loops)
  [0] 👋 Exit
""")
        choice = input("  Choose: ").strip()

        if choice == '1':
            countdown_timer()
        elif choice == '2':
            guessing_game()
        elif choice == '3':
            fizzbuzz()
        elif choice == '4':
            pattern_printer()
        elif choice == '0':
            print("\n  👋 Goodbye! Practice makes perfect!")
            break
        else:
            print("  ❌ Invalid choice. Try 1-4 or 0 to exit.")


if __name__ == "__main__":
    main()
