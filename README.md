# 7 Tides (Hangman Game)

## Lore and Purpose
Welcome to 7 Tides, a Hangman game steeped in pirate lore and mystery. Set sail on a perilous journey as you attempt to decipher the secrets of the seven deadly sins that have ensnared a legendary pirate. Immerse yourself in an immersive narrative that unfolds with each guess, revealing the depths of the pirate's past and the challenges that lie ahead.

Your task is not only to solve the hidden word but also to uncover the sins that have plagued the pirate's life. With each correct guess, you inch closer to redemption, while every misstep brings you closer to the abyss. Can you conquer your own demons and emerge victorious in the face of adversity?

## How to play
To play the game, simply run `main.py` from your terminal. Follow the prompts to guess letters and solve the hidden word. You have 7 attempts to guess the word correctly.

## Features
### Existing Features
- Utilizes an external library `rich` for enhanced terminal printing.
- Random word selection from a predefined word list.
- Visual representation of game state with ASCII art.
- Input validation for single letter guesses.

### Future Features
- Implementing difficulty levels.
- Adding multiplayer functionality.
- Incorporating a scoring system.

## Setting up envirement
### Core steps
1.pip install Pylance , Python , GitPod , rich external library
2.Create core files
3.Connect to GitHub repository
4.Create core logic
5.Create input handling, exceptions
6.Create content and overall design
7.Testing
8.Deployement process

## Data Model
The game consists of a `Game` class with methods for managing game logic, including word selection, displaying the word with hidden letters, checking guesses, and determining game over conditions.

## Testing

### Testing Process
Testing was conducted manually by running the game and verifying the behavior against expected outcomes. Input validation was thoroughly tested to ensure correct handling of various inputs.

### Bugs
- Fixed a bug related to indentation in the `run()` method.
- Addressed issues with capitalization of stored words for comparison.
- Corrected game over conditions to handle cases where the entire word is guessed.

### Validator Testing
The code was tested using PEP 8 guidelines and passed validation.

## Deployment
The game can be deployed locally by cloning the repository and running `main.py` with a Python interpreter.
Deployement in progress due to Heroku.
Screenshots will be provided after deployement on Heroku.
## Credits
- Code Institute for educational resources.
- Wikipedia for information on Hangman game.
- ChatGPT for general topics.
