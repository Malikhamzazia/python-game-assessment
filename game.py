import random


def get_player_name():
    """Ask the player for their name."""
    name = input("What is your name? ")
    if not name.strip():
        return "Player"
    return name.strip()


def ask_for_guess():
    """Ask the player for a guess and ensure it's a valid integer."""
    while True:
        guess_text = input("Enter your guess (1–100): ")
        if not guess_text.strip():
            print("Please enter a number.")
            continue

        if not guess_text.strip().isdigit():
            print("That doesn't look like a whole number. Try again.")
            continue

        guess = int(guess_text)
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.")
            continue

        return guess


def play_round(secret_number, max_attempts=10):
    """Play a single round of the guessing game.

    Returns True if the player wins, False otherwise.
    """
    attempts_used = 0

    while attempts_used < max_attempts:
        print(f"\nAttempt {attempts_used + 1} of {max_attempts}")
        guess = ask_for_guess()
        attempts_used += 1

        if guess == secret_number:
            print("Correct! You guessed the number!")
            return True
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

    print("\n Out of attempts! Better luck next time.")
    print(f"The secret number was: {secret_number}")
    return False


def want_to_play_again():
    """Ask the player if they want to play another round."""
    while True:
        answer = input("\nDo you want to play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")


def main():
    print("===================================")
    print("  Welcome to the Number Guessing Game!")
    print("===================================\n")

    player_name = get_player_name()
    print(f"\nHello, {player_name}! I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it correctly.\n")

    while True:
        secret_number = random.randint(1, 100)
        won = play_round(secret_number)

        if won:
            print(f"Great job, {player_name}!")
        else:
            print(f"Nice try, {player_name}! You'll get it next time.")

        if not want_to_play_again():
            print("\nThanks for playing! Goodbye")
            break


if __name__ == "__main__":
    main()