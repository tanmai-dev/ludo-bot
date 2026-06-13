import random

class GameState:

    def __init__(self, player1, player2, player3, player4):
        self.board = {'R1':'I','R2':'I','R3':'I','R4':'I','G1':'I','G2':'I','G3':'I','G4':'I','Y1':'I','Y2':'I','Y3':'I','Y4':'I','B1':'I','B2':'I','B3':'I','B4':'I'}
        self.prog = {'R1':'I','R2':'I','R3':'I','R4':'I','G1':'I','G2':'I','G3':'I','G4':'I','Y1':'I','Y2':'I','Y3':'I','Y4':'I','B1':'I','B2':'I','B3':'I','B4':'I'}
        self.turn = 0
        if self.turn >= 4:
            self.turn %= 4
        self.players = [player1, player2, player3, player4]
        self.current_player = self.players[self.turn]

    def capture(self, piece):

        if self.board[piece] > 52:
            self.board[piece] -= 52
        
        if self.board[piece] not in [1, 9, 14, 22, 27, 35, 40, 48]:
            for i in self.board:
                if self.board[i] == self.board[piece] and i != piece and self.board[i] != 'L' and i[0]!= piece[0]:
                    self.board[i] = 0
                    self.prog[i] = 0
                elif self.board[i] == self.board[piece] and i != piece and self.board[i] != 'L' and i[0] == piece[0]:
                    return "reroll"

    def update_board(self):
        dice = random.randint(1, 6)
        piece = self.current_player.move_piece(dice, self) #piece is a string (R1,R2,...,B3,B4)
        if self.current_player==self.players[0]:
            if self.prog[piece] + dice > 57:
                #move not possible
                pass

            self.board[piece] += dice
            self.prog[piece] += dice

            if self.prog[piece]>51:
                self.board[piece] == 'L'

        if self.current_player==self.players[1]:
            #starting value for self.board[piece]=14
            if self.prog[piece] + dice > 57:
                #move not possible
                pass
            self.board[piece] += dice
            self.prog[piece] += dice
            if self.board[piece]>52:
                self.board[piece] -= 52

            if self.prog[piece]>51:
                self.board[piece] == 'L'

        if self.current_player == self.players[2]:
            # starting value for self.board[piece]=27
            if self.prog[piece] + dice > 57:
                #move not possible
                pass
            self.board[piece] += dice
            self.prog[piece] += dice
            if self.board[piece] > 52:
                self.board[piece] -= 52

            if self.prog[piece] > 51:
                self.board[piece] == 'L'

        if self.current_player == self.players[3]:
            # starting value for self.board[piece]=40
            if self.prog[piece] + dice > 57:
                #move not possible
                pass
            self.board[piece] += dice
            self.prog[piece] += dice
            if self.board[piece] > 52:
                self.board[piece] -= 52

            if self.prog[piece] > 51:
                self.board[piece] == 'L'
