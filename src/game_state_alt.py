import random

class GameState:

    def __init__(self, player1, player2, player3, player4):
        self.board = {'R1':0,'R2':0,'R3':0,'R4':0,'G1':0,'G2':0,'G3':0,'G4':0,'Y1':0,'Y2':0,'Y3':0,'Y4':0,'B1':0,'B2':0,'B3':0,'B4':0}
        self.prog = {'R1':0,'R2':0,'R3':0,'R4':0,'G1':0,'G2':0,'G3':0,'G4':0,'Y1':0,'Y2':0,'Y3':0,'Y4':0,'B1':0,'B2':0,'B3':0,'B4':0}
        self.turn = 0
        if self.turn >= 4:
            self.turn %= 4
        self.players = [player1, player2, player3, player4]
        self.current_player = self.players[self.turn]




    def update_board(self):
        dice = random.randint(1, 6)
        piece = self.current_player.move_piece(dice, self) #piece is a string (R1,R2,...,B3,B4)
        if self.current_player==self.players[0]:
            self.board[piece] += dice
            self.prog[piece] += dice

            if self.prog[piece]>52:
                self.board[piece] == 'L'

        if self.current_player==self.players[1]:
            #starting value for self.board[piece]=14
            self.board[piece] += dice
            self.prog[piece] += dice
            if self.board[piece]>52:
                self.board[piece] -= 52

            if self.prog[piece]>52:
                self.board[piece] == 'L'

        if self.current_player == self.players[2]:
            # starting value for self.board[piece]=27
            self.board[piece] += dice
            self.prog[piece] += dice
            if self.board[piece] > 52:
                self.board[piece] -= 52

            if self.prog[piece] > 52:
                self.board[piece] == 'L'

        if self.current_player == self.players[3]:
            # starting value for self.board[piece]=40
            self.board[piece] += dice
            self.prog[piece] += dice
            if self.board[piece] > 52:
                self.board[piece] -= 52

            if self.prog[piece] > 52:
                self.board[piece] == 'L'