class GameState:

    def __init__(self, player1, player2, player3, player4):
        board = dict()
        player = {"R":player1, "G":player2, "B":player3, "Y":player4}
        for i in ["R", "G", "B", "Y"]:
            for j in range(1, 14):
                board[i+str(j)] = 0
            for j in range(1, 6):
                board[i+str(j)+"L"] = 0
            for j in range(1, 5):
                board[i+str(j)+"B"] = player[i].pieces[j]
            board[i+"W"] = 0
        self.board = board

    def get_positions(self):
        pass