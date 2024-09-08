import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

      
        self.instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=('Arial', 14))
        self.instruction_label.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=('Arial', 14))
        self.result_label.pack(pady=10)

        self.rock_button = tk.Button(root, text="Rock", width=10, height=2, command=lambda: self.play_game("Rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(root, text="Paper", width=10, height=2, command=lambda: self.play_game("Paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(root, text="Scissors", width=10, height=2, command=lambda: self.play_game("Scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

      
        self.score_label = tk.Label(root, text=f"Your Score: {self.user_score}  Computer's Score: {self.computer_score}", font=('Arial', 12))
        self.score_label.pack(pady=10)

    def play_game(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        
        self.result_label.config(text=f"You chose {user_choice}. Computer chose {computer_choice}. {result}")

      
        if "win" in result:
            self.user_score += 1
        elif "lose" in result:
            self.computer_score += 1

       
        self.score_label.config(text=f"Your Score: {self.user_score}  Computer's Score: {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            return "You win!"
        else:
            return "You lose!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
