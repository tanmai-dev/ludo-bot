from game_state import GameState
from random_bot import Player
from SW_LudoBot1 import SW_LudoBot1

score = {"R":0, "G":0, "Y":0, "B":0}
for i in range(1000):
    
    p1 = Player("R")
    p2 = Player("G")
    p3 = SW_LudoBot1("Y")
    p4 = SW_LudoBot1("B")
    game = GameState(p1, p2, p3, p4)
    while True:
        result = game.update_board()

        if result == "terminated":
            print("Game terminated.")
            break

        if result == "over":
            for j in range(3):
                score[game.winners[j]] += 3-j
            break

print(score)
