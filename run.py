import os
from game_logic import Game

#Handle game initialization within the main function
def main():
    game = Game()
    game.run()

#Ensures that run.py is the main entry and it runs directly from the Python interpreter
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)