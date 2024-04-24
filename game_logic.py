import random  # Importing the random module for generating random numbers or choices.
from word_list import words  # Importing a list of words from an external module.
from visuals import *  # Importing visual assets and variables from an external module.
from rich import print  # Importing the rich print function for colorful console output.


class Game:  # Defining a class called Game to encapsulate the game logic.
    def __init__(self):  # Initializing the game state.
        self.word = self.get_random_word()  # Choosing a random word for the game.
        self.guesses = set()  # Initializing an empty set to store guessed letters.
        self.attempts = 7  # Setting the maximum number of attempts.

    def get_random_word(self):  # Method to get a random word from the imported word list.
        return random.choice(words)

    def display_word(self):  # Method to display the word with hidden letters or guessed letters.
        display = ""
        for letter in self.word:
            if letter in self.guesses:
                display += letter
            else:
                display += "_"
        return display

    def check_guess(self, guess):  # Method to check if the guessed letter is correct.
        if len(guess) != 1 or not guess.isalpha():  # Checking if the guess is valid.
            print("[bold red]You can only enter one letter for your guess![/bold red]")  # Notifying the player about invalid input.
            return
        guess = guess.lower()  # Converting the guess to lowercase for uniformity.
        if guess in self.guesses:  # Checking if the letter has already been guessed.
            print("[bold red]You already guessed this letter![/bold red]")  # Notifying the player about repeated guess.
            return
        guess = guess.lower()
        self.guesses.add(guess)  # Adding the guess to the set of guessed letters.
        if guess not in self.word:  # Deducting an attempt if the guess is incorrect.
            self.attempts -= 1

    def is_game_over(self):  # Method to check if the game is over.
        return self.attempts == 0 or self.is_winner()  # Game over if no attempts left or if the player wins.

    def is_winner(self):  # Method to check if the player has won.
        unique_letters = set(self.word)
        return unique_letters.issubset(self.guesses)  # Player wins if all letters in the word are guessed.

    def run(self):  # Method to start and run the game loop.
        restart_game = True  # Flag to control game restarts.

        while restart_game:  # Main game loop.
            print("[bold cyan]                    ##########################[/bold cyan]")  # Displaying game title.
            print("[bold cyan]                    # Welcome to the 7 tides #[/bold cyan]")
            print("[bold cyan]                    ##########################[/bold cyan]")
            print("[bold green]" + lore + "[/bold green]")  # Displaying game lore.

            while not self.is_game_over():  # Inner loop for playing the game until it's over.
                print()
                if self.attempts in hangman_art:  # Displaying hangman visuals based on remaining attempts.
                    print("[bold yellow]" + hangman_art[self.attempts] + "[/bold yellow]")

                print("[bold]Attempts left:[/bold] [blue]" + str(self.attempts) + "[/blue]")  # Displaying remaining attempts.
                print()
                print("[bold]Word:[/bold] [green]" + self.display_word() + "[/green]")  # Displaying the word with hidden letters.
                print()
                guess = input("Guess a letter: \n")  # Prompting the player to guess a letter.
                print("[bold cyan]###################[/bold cyan]")  # Separating game sections.
                self.check_guess(guess.lower())  # Checking the validity of the guessed letter.

            if self.is_winner():  # Checking if the player has won.
                print("[bold green]Congratulations! You guessed the word:[/bold green] [bold green]" + self.word.capitalize() + "[/bold green]")  # Displaying win message.
                print("[bold green]" + lore_end + "[/bold green]")  # Displaying end game lore.
            else:
                print("[bold red]Sorry, you ran out of attempts. The word was:[/bold red] [bold red]" + self.word.capitalize() + "[/bold red]")  # Displaying loss message.
                print("[bold red]" + hangman_art_0 + "[/bold red]")  # Displaying the full hangman art.

            print()
            restart = input("Press the 'r' key to restart the game or any other key to exit: ")  # Prompting for game restart.
            if restart.lower() != "r":  # Checking if the player wants to restart the game.
                restart_game = False  # Exiting the game loop if not restarting.
            else:
                self.word = self.get_random_word()  # Resetting the word for a new game.
                self.guesses = set()  # Resetting guessed letters.
                self.attempts = 7  # Resetting the number of attempts.     