import random
import tkinter as tk
from tkinter import messagebox


class GuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10

        # Title label
        tk.Label(
            master,
            text="Guess the number between 1 and 100!",
            font=("Arial", 14)
        ).pack(pady=10)

        # Entry box
        self.entry = tk.Entry(master, font=("Arial", 12))
        self.entry.pack(pady=10)

        # Guess button
        tk.Button(
            master,
            text="Guess",
            font=("Arial", 12),
            command=self.check_guess
        ).pack(pady=5)

        # Feedback label
        self.feedback = tk.Label(master, text="", font=("Arial", 12))
        self.feedback.pack(pady=10)

        # Reset button
        tk.Button(
            master,
            text="New Game",
            font=("Arial", 12),
            command=self.reset_game
        ).pack(pady=5)

    def check_guess(self):
        guess_text = self.entry.get().strip()

        if not guess_text.isdigit():
            self.feedback.config(text="Please enter a valid whole number.")
            return

        guess = int(guess_text)
        self.attempts += 1

        if guess == self.secret_number:
            messagebox.showinfo("Correct!", "You guessed the number!")
            self.reset_game()
        elif self.attempts >= self.max_attempts:
            messagebox.showinfo(
                "Out of attempts",
                f"The number was {self.secret_number}."
            )
            self.reset_game()
        elif guess < self.secret_number:
            self.feedback.config(text="Too low!")
        else:
            self.feedback.config(text="Too high!")

        self.entry.delete(0, tk.END)

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback.config(text="")
        self.entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = GuessingGameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
