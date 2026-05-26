"""
Exercise 1 Solution: Countdown Timer (Beginner)
=================================================
Run: python3 01_countdown_timer.py

Demonstrates:
- while loop for countdown
- time.sleep() for timing
- divmod() for MM:SS formatting
- Input validation loop
- Carriage return (\r) for overwriting output
"""

import time


def countdown_timer():
    """
    A functional countdown timer.

    Features:
    - Accept time in seconds
    - Display in MM:SS format
    - Clear previous line for clean display (use \r)
    - Show progress bar
    - Show visual alert when done
    - Ask to repeat
    """
    print("=" * 45)
    print("       COUNTDOWN TIMER")
    print("=" * 45)

    while True:  # Repeat loop
        # Get and validate input
        while True:
            user_input = input("\n  Enter countdown time in seconds: ").strip()

            if user_input.isdigit() and int(user_input) > 0:
                total_seconds = int(user_input)
                break
            else:
                print("  Invalid! Please enter a positive integer.")

        # Display initial time
        mins, secs = divmod(total_seconds, 60)
        print(f"\n  Starting countdown from {mins:02d}:{secs:02d}...")
        print()

        # Progress bar settings
        bar_width = 30
        remaining = total_seconds

        # Countdown loop
        while remaining >= 0:
            # Calculate MM:SS
            mins, secs = divmod(remaining, 60)

            # Calculate progress bar
            elapsed = total_seconds - remaining
            if total_seconds > 0:
                progress = elapsed / total_seconds
            else:
                progress = 1.0

            filled = int(bar_width * progress)
            bar = "█" * filled + "░" * (bar_width - filled)

            # Display with carriage return (overwrites previous line)
            print(f"\r  {mins:02d}:{secs:02d}  [{bar}]  {progress * 100:.0f}%", end="")

            if remaining > 0:
                time.sleep(1)
            remaining -= 1

        # Timer complete!
        print()  # New line after the timer
        print()
        print("  ╔══════════════════════════════════╗")
        print("  ║      TIME'S UP!                  ║")
        print("  ╚══════════════════════════════════╝")
        print()

        # Ask to repeat
        again = input("  Set another timer? (y/n): ").strip().lower()
        if again != "y":
            print("  Goodbye!")
            break


# Run the timer
if __name__ == "__main__":
    countdown_timer()
