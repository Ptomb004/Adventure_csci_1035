import io
import sys

from src.game import game
def game_test():
    choices = ["1", "2"]

    sys.stdin = io.StringIO("".join(choices))

    sys.stdout = io.StringIO()
    game()

    output = sys.stdout.getvalue()

    print("Game Test Output:")
    print(output)

if __name__ == "__main__":
    game_test()



     
    