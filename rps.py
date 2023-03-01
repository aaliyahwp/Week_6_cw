import random

class RockPaperScissors: # created a class called rockpaperscissors for the game

    # Def is a method that acts as a function inside the class.

    def __init__(self): # the __init__ function initialises
        self.choices = ["rock", "paper", "scissors"] # These are attributes to the class.
        self.computer_choice = None
        self.player_choice = None

    # Function to allow the computer to choose a random choice from the choices list using the random module
    def get_computer_choice(self):
        self.computer_choice = random.choice(self.choices)

 # player choice using input to select from the list. if something not in the list is inputted it will return an error

    def get_player_choice(self):
        valid_choice = False
        while not valid_choice:
            self.player_choice = input("Choose rock, paper, or scissors: ")
            if self.player_choice in self.choices:
                valid_choice = True
            else:
                print("Invalid choice. Try again.")

    # This is the rules of the game using conditional statements.
    def determine_winner(self):

        if self.player_choice == self.computer_choice:
            print(f'You have both selected {self.player_choice}. You are tied!')
        elif self.computer_choice == 'rock' and self.player_choice == 'scissors':
            print('Rock smashes Scissors, You lose!') # unsure how to print this.
        elif self.computer_choice == 'scissors' and self.player_choice == 'paper':
            print('Scissors cut paper! You lose!')
        elif self.computer_choice == 'paper' and self.player_choice == 'rock':
            print('Paper wraps rock. You lose!')

        else:
            print('You have won!')


    # This allows us to output the two chosen weapons and uses determine winner to play the game
    def play(self):
        self.get_computer_choice()
        self.get_player_choice()
        print("You chose", self.player_choice)
        print("Computer chose", self.computer_choice)
        self.determine_winner()

if __name__ == "__main__": # This is the main trick.

    game = RockPaperScissors()
    game.play()
