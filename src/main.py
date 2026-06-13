from game_state_alt.py import GameState
from player,py import Player

p1 = Player("R")
p2 = Player("G")
p3 = Player("Y")
p4 = Player("B")

game = GameState(p1, p2, p3, p4)

while True:
    result = game.update_board()

    if result == "terminated":
        print("Game terminated.")
        break

    if result == "over":
        break
