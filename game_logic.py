import random
from word_list import words
from visuals import *
from rich import print

class Game:
    # Initialize the current condition of the game (default)
    def __init__(self):
        self.word = self.get_random_word()
        self.guesses = set()
        self.attempts = 7

    # A pool of random words and function to get a random word for the current game
    def get_random_word(self):
        return random.choice(words)

    # A method to display the word with hidden letters (-)
    def display_word(self):
        display = ""
        for letter in self.word:
            if letter in self.guesses:
                display += letter
            else:
                display += "_"
        return display

    # Check if the guess is correct, if not take one attempt away
    def check_guess(self, guess):
        # If the guess is not one character length or it is not a letter -> let the player know
        if len(guess) != 1 or not guess.isalpha():
            print("[bold red]You can only enter one letter for your guess![/bold red]")
            return
        guess = guess.lower()
        # Check if the letter has already been guessed -> let the player know
        if guess in self.guesses:
            print("[bold red]You already guessed this letter![/bold red]")
            return
        guess = guess.lower()
        self.guesses.add(guess)
        if guess not in self.word:
            self.attempts -= 1

    # A method for checking game over conditions (The number of your attempts is 0 or you guessed the word)
    def is_game_over(self):
        return self.attempts == 0 or set(self.word) == self.guesses or all(letter in self.guesses for letter in self.word)

    # Runs the game loop until the game over function is true
    def run(self):
        # Runs at the beginning of the game
        print("[bold cyan]                    ##########################[/bold cyan]")
        print("[bold cyan]                    # Welcome to the 7 tides #[/bold cyan]")
        print("[bold cyan]                    ##########################[/bold cyan]")
        print("[bold green]" + lore + "[/bold green]")
        # Runs until game over is True
        while not self.is_game_over():
            print()
            if self.attempts in hangman_art:
                print("[bold yellow]" + hangman_art[self.attempts] + "[/bold yellow]")

            print("[bold]Attempts left:[/bold] [blue]" + str(self.attempts) + "[/blue]")
            print()
            print("[bold]Word:[/bold] [green]" + self.display_word() + "[/green]")
            print()
            guess = input("Guess a letter: ")
            print("[bold cyan]###################[/bold cyan]")
            self.check_guess(guess.lower())
        # Informs the player about the end state of the game (in both cases, prints out the word)
        if set(self.word) == self.guesses:
            print("[bold green]Congratulations! You guessed the word:[/bold green] [bold green]" + self.word.capitalize() + "[/bold green]")
            print("[bold green]" + lore_end + "[/bold green]")
        else:
            print("[bold red]Sorry, you ran out of attempts. The word was:[/bold red] [bold red]" + self.word.capitalize() + "[/bold red]")
            print("[bold red]" + hangman_art_0 + "[/bold red]")