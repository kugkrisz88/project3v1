import random

class Game:
    #Initialize the current condition of the game (default)
    def __init__(self):
        self.word = ""
        self.guesses = set()
        self.attempts = 6
    #A pool of random words and function to get a random word for the current game
    def get_random_word(self):
        words = ["apple", "banana", "orange", "grape"]
        return random.choice(words)
    #A method to display the word with hidden letters (-)
    def display_word(self):
        display = ""
        for letter in self.word:
            if letter in self.guesses:
                display += letter
            else:
                display += "_"
        return display

    #Check if the guess is correct, if not take one attempt away
    def check_guess(self, guess):
        self.guesses.add(guess)
        if guess not in self.word:
            self.attempts -= 1

    #A method for checking game over conditions (The number of your attemps are 0 or you guessed the word)
    def is_game_over(self):
    #Runs the game loop till the gameover function is true
    def run(self):
    print("Welcome to Hangman!")