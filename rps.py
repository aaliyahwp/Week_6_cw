import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.computer_choice = None
        self.player_choice = None

    def get_computer_choice(self):
        self.computer_choice = random.choice(self.choices)

    def get_player_choice(self):
        valid_choice = False
        while not valid_choice:
            self.player_choice = input("Choose rock, paper, or scissors: ")
            if self.player_choice in self.choices:
                valid_choice = True
            else:
                print("Invalid choice. Try again.")

    def determine_winner(self):

        if self.player_choice == self.computer_choice:
            print(f'You have both selected {self.player_choice}. You are tied!')
        elif self.computer_choice == 'Rock' and self.player_choice == 'Scissors':
            print('Rock smashes Scissors, You lose!')
        elif self.computer_choice == 'Scissors' and self.player_choice == 'Paper':
            print('Scissors cut paper! You lose!')
        elif self.computer_choice == 'Paper' and self.player_choice == 'Rock':
            print('Paper wraps rock. You lose!')
        else:
            print('You have won!')

    def play(self):
        self.get_computer_choice()
        self.get_player_choice()
        print("You chose", self.player_choice)
        print("Computer chose", self.computer_choice)
        self.determine_winner()

if __name__ == "__main__":

    game = RockPaperScissors()
    game.play()
