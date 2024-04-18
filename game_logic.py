class Game:
    #Initialize the current condition of the game (default)
    def __init__(self):
        self.word = ""
        self.guesses = set()
        self.attempts = 6
    #A pool of random words and function to get a random word for the current game
    def get_random_word(self):
    #A method to display the word with hidden letters (-)
    def display_word(self):
    #Check if the guess is correct, if not take one attempt away
    def check_guess(self, guess):
    #A method for checking game over conditions (The number of your attemps are 0 or you guessed the word)
    def is_game_over(self):
    #Runs the game loop till the gameover function is true
    def run(self):
    print("Welcome to Hangman!")