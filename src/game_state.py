import random

class GameState:

    def __init__(self, player1, player2, player3, player4):
        self.board = list()
        for i in range(52):
            self.board.append(0)
        self.R = [player1.piece1, player1.piece2, player1.piece3, player1.piece4, 0, 0, 0, 0, 0, 0]
        self.G = [player2.piece1, player2.piece2, player2.piece3, player2.piece4, 0, 0, 0, 0, 0, 0]
        self.Y = [player3.piece1, player3.piece2, player3.piece3, player3.piece4, 0, 0, 0, 0, 0, 0]
        self.B = [player4.piece1, player4.piece2, player4.piece3, player4.piece4, 0, 0, 0, 0, 0, 0]

        self.current_player = player1
        self.players = [player1, player2, player3, player4]
        self.turn = 0
            
    def update_board(self):
        dice = random.randint(1, 6)
        piece = self.current_player.move_piece(dice, self)
        for i in range(52):
            if self.board[i] == piece:
                if self.current_player == self.players[0]:
                    if i + dice + 1< 52:
                        self.board[i] = 0
                        self.board[i + dice] = piece
                    else:
                        self.board[i] = 0
                        self.R[4 + (i + dice - 52)] = piece
                elif self.current_player == self.players[1]:
                    if ((i+1) + dice  < 13) or ((i+1) >= 14 and (i+1)+dice <= 52):
                        self.board[i] = 0
                        self.board[i + dice] = piece
                    elif (i+1) + dice > 52:
                        self.board[i] = 0
                        self.board[(i+dice+1)%52] = piece
                    else:
                        self.board[i] = 0
                        self.G[4 + (i + dice - 13)] = piece
                elif self.current_player == self.players[2]:
                    if ((i+1) + dice  < 26) or ((i+1) >= 17 and (i+1)+dice <= 52):
                        self.board[i] = 0
                        self.board[i + dice] = piece
                    elif (i+1) + dice > 52:
                        self.board[i] = 0
                        self.board[(i+dice+1)%52] = piece
                    else:
                        self.board[i] = 0
                        self.Y[4 + (i + dice - 26)] = piece
                else:
                    if ((i+1) + dice  < 39) or ((i+1) >= 40 and (i+1)+dice <= 52):
                        self.board[i] = 0
                        self.board[i + dice] = piece
                    elif (i+1) + dice > 52:
                        self.board[i] = 0
                        self.board[(i+dice+1)%52] = piece
                    else:
                        self.board[i] = 0
                        self.B[4 + (i + dice - 39)] = piece
        self.turn += 1
