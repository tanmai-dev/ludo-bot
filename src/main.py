from game_state_alt import GameState
from player import Player
from player_alt import EvilPlayer

p1 = Player("R")
p2 = Player("G")
p3 = Player("Y")
p4 = EvilPlayer("B")

game = GameState(p1, p2, p3, p4)

while True:
    result = game.update_board()

    if result == "terminated":
        print("Game terminated.")
        break

    if result == "over":
        break
