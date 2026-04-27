"""Simple Rock Paper Scissors GUI using Tkinter."""

import random
import tkinter as tk


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    if (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    return "Computer wins!"


class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.resizable(False, False)

        self.player_wins = 0
        self.computer_wins = 0
        self.tie_count = 0
        self.round_count = 0

        self.title_label = tk.Label(
            root,
            text="Rock Paper Scissors",
            font=("Segoe UI", 16, "bold"),
            pady=10,
        )
        self.title_label.pack()

        self.score_label = tk.Label(
            root,
            text="Round: 0 | Player Wins: 0 | Computer Wins: 0 | Ties: 0",
            font=("Segoe UI", 12),
            pady=5,
        )
        self.score_label.pack()

        self.result_label = tk.Label(
            root,
            text="Choose your move to start playing.",
            font=("Segoe UI", 11),
            pady=10,
        )
        self.result_label.pack()

        self.choice_frame = tk.Frame(root, pady=10)
        self.choice_frame.pack()

        tk.Button(
            self.choice_frame,
            text="Rock",
            width=10,
            command=lambda: self.play_round("rock"),
        ).grid(row=0, column=0, padx=6)

        tk.Button(
            self.choice_frame,
            text="Paper",
            width=10,
            command=lambda: self.play_round("paper"),
        ).grid(row=0, column=1, padx=6)

        tk.Button(
            self.choice_frame,
            text="Scissors",
            width=10,
            command=lambda: self.play_round("scissors"),
        ).grid(row=0, column=2, padx=6)

        self.quit_button = tk.Button(root, text="Quit", width=10, command=root.destroy)
        self.quit_button.pack(pady=12)

    def play_round(self, player_choice):
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        self.round_count += 1

        if result == "You win!":
            self.player_wins += 1
        elif result == "Computer wins!":
            self.computer_wins += 1
        else:
            self.tie_count += 1

        self.score_label.config(
            text=(
                f"Round: {self.round_count} | "
                f"Player Wins: {self.player_wins} | "
                f"Computer Wins: {self.computer_wins} | "
                f"Ties: {self.tie_count}"
            )
        )
        self.result_label.config(
            text=(
                f"You chose {player_choice}. Computer chose {computer_choice}. "
                f"{result}"
            )
        )


def main():
    root = tk.Tk()
    RockPaperScissorsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
