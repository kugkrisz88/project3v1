# 7 Tides (Hangman Game)
- <img src="/screenshot/d2.png" alt="screenshot" width="1000" height="600">
## Lore and Purpose
- Welcome to 7 Tides, a Hangman game steeped in pirate lore and mystery. Set sail on a perilous journey as you attempt to decipher the secrets of the seven deadly sins that have ensnared a legendary pirate. 
- Immerse yourself in an immersive narrative that unfolds with each guess, revealing the depths of the pirate's past and the challenges that lie ahead.
- Your task is not only to solve the hidden word but also to uncover the sins that have plagued the pirate's life. With each correct guess, you inch closer to redemption, while every misstep brings you closer to the abyss. Can you conquer your own demons and emerge victorious in the face of adversity?

## How to play
- To play the game, simply run `run.py` from your terminal. Follow the prompts to guess letters and solve the hidden word. You have 7 attempts to guess the word correctly.
- On Heroku the game is already running through this link : https://seven-tides-9775c5e60f58.herokuapp.com/

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
- Screen size support. (Currently does NOT support)

## Setting up envirement
### Core steps
- 1.pip install Pylance , Python , GitPod , rich external library
- 2.Create core files
- 3.Connect to GitHub repository
- 4.Create core logic
- 5.Create input handling, exceptions
- 6.Create content and overall design
- 7.Testing
- 8.Deployement process

## Data Model
The game consists of a `Game` class with methods for managing game logic, including word selection, displaying the word with hidden letters, checking guesses, and determining game over conditions.

## Testing

### Testing Process
Testing was conducted manually by running the game and verifying the behavior against expected outcomes. Input validation was thoroughly tested to ensure correct handling of various inputs.

### Bugs
- Fixed a bug related to indentation in the `run()` method.
- Addressed issues with capitalization of stored words for comparison.
- Corrected game over conditions to handle cases where the entire word is guessed. (Added a check winner condtition to avoid getting "Run out of attempts" message on correctly guessed word)

### Validator Testing
- The code was tested using Python tester and passed validation.
https://extendsclass.com/python-tester.html
- <img src="/screenshot/d14.png" alt="screenshot" width="500" height="220">
- The code was tested in VSCode PEP8 validator with no issues. (Warnings only for the commented out code is too long for PEP8 but the code itself is perfectly fine for all PEP8 standards)


## Deployment Process
- Original Code Institute GitHub repository needs to be copied for Heroku to work.
- Make sure the program entry file is named run.py
- Create new app, then add name of the web app and chose Europe as region
- <img src="/screenshot/d6.png" alt="screenshot" width="150" height="100">
- <img src="/screenshot/d7.png" alt="screenshot" width="550" height="300">
- Connect GitHub repository
- <img src="/screenshot/d8.png" alt="screenshot" width="1000" height="400">
- Go settings to set up the `PORT` to `8000` and the Buildpacks for `Python` and `Nodejs`.
- <img src="/screenshot/d9.png" alt="screenshot" width="600" height="50">
- <img src="/screenshot/d16.png" alt="screenshot" width="1000" height="400">
- Go back to the Deploy tab.
- <img src="/screenshot/d10.png" alt="screenshot" width="600" height="50">
- Scroll down to manual deployment. Press `Deploy Branch`.
- <img src="/screenshot/d11.png" alt="screenshot" width="1000" height="200">
- It installs everything that is set and all `pip` from the `requirements.txt`.
- On top of the page `Open App` is ready to open the page, and the app is succesfully deployed.
- <img src="/screenshot/d12.png" alt="screenshot" width="1000" height="60">
## Deployment Issues
- This is the Error if the original CodeInstitute P3 repository files are not included.
- <img src="/screenshot/d1.png" alt="screenshot" width="350" height="150">
- This is the Error log if the original CodeInstitute P3 repository files are not included.
- <img src="/screenshot/d4.png" alt="screenshot" width="1000" height="400">
- To check logs open this panel
- <img src="/screenshot/d13.png" alt="screenshot" width="150" height="200">
## Credits
- Code Institute for educational resources.
- Wikipedia for information on Hangman game.
- ChatGPT for general topics.
