import random
from word_list import words
from visuals import *

class Game:
    #Initialize the current condition of the game (default)
    def __init__(self):
        self.word = self.get_random_word()
        self.guesses = set()
        self.attempts = 7
    #A pool of random words and function to get a random word for the current game
    def get_random_word(self):
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
        #If the guess in not one character length or it is not a letter -> let the player know
        if len(guess) != 1 or not guess.isalpha():
            print("You can only enter one letter for your guess!")
            return
        guess = guess.lower()
        self.guesses.add(guess)
        if guess not in self.word:
            self.attempts -= 1

    #A method for checking game over conditions (The number of your attemps are 0 or you guessed the word)
    def is_game_over(self):
        return self.attempts == 0 or set(self.word) == self.guesses
    #Runs the game loop till the gameover function is true
    def run(self):
        #Runs at the beginning of the game
        print("##########################")
        print("# Welcome to the 7 tides #")
        print("##########################")
        print(lore)
        #Runs till game over is True
        while not self.is_game_over():
            print()
            if self.attempts in hangman_art:
                print(hangman_art[self.attempts])

            print("Attempts left:", self.attempts)
            print()
            print("Word:", self.display_word())
            print()
            guess = input("Guess a letter: ")
            print("###################")
            self.check_guess(guess.lower())
        #Informs the player about the end state of the game (in both case prints out the word)    
        if set(self.word) == self.guesses:
            print("Congratulations! You guessed the word:", self.word.capitalize)
        else:
            print("Sorry, you ran out of attempts. The word was:", self.word.capitalize)
            print(hangman_art_0)      