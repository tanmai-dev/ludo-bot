from game_state_alt import GameState
from player import Player
from player_alt import EvilPlayer

score = {"R":0, "G":0, "Y":0, "B":0}
for i in range(1000):
    
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
            for j in range(3):
                print(game.winners)
                score[game.winners[j]] += 3-j
            break

print(score)
