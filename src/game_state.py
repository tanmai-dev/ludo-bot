import random

class GameState:

    def __init__(self, player1, player2, player3, player4):
        self.board = {'R1':0,'R2':0,'R3':0,'R4':0,'G1':0,'G2':0,'G3':0,'G4':0,'Y1':0,'Y2':0,'Y3':0,'Y4':0,'B1':0,'B2':0,'B3':0,'B4':0}
        self.prog = {'R1':0,'R2':0,'R3':0,'R4':0,'G1':0,'G2':0,'G3':0,'G4':0,'Y1':0,'Y2':0,'Y3':0,'Y4':0,'B1':0,'B2':0,'B3':0,'B4':0}
        self.turn = 0
        self.players = [player1, player2, player3, player4]
        self.player_no = 4
        self.winners = []
        self.current_player = self.players[self.turn]

    def move_and_capture(self, piece):

        if self.board[piece] > 52 and self.board[piece] != 100:
            self.board[piece] -= 52
        
        
        if self.board[piece] not in [1, 9, 14, 22, 27, 35, 40, 48]:
            for i in self.board:
                if self.board[i] == self.board[piece] and i != piece and self.board[i] != 100 and i[0]!= piece[0]:
                    self.board[i] = 0
                    self.prog[i] = 0
                elif self.board[i] == self.board[piece] and i != piece and self.board[i] != 100 and i[0] == piece[0]:
                    return "reroll"
        
        if self.prog[piece] == 57:
                print(f"Peg {piece} has reached the end!")
                self.current_player.in_pieces += 1
                del self.board[piece]
                del self.prog[piece]
                if self.current_player.in_pieces != 4:
                    return "win"
                else:
                    return
        
        print(f"{piece} moved to {self.board[piece]}")
        
    def check_move_status(self, dice, piece):
        color = self.current_player.color
        Move_status = False
        for i in range(4):
            key = color + str(i+1)
            if self.board.get(key) is None:
                continue
            if key == piece:
                continue
            else:
                if self.prog[key] == 0:
                    if dice == 6 and key[0] == "R":
                        Move_status = True
                    elif dice == 6 and key[0] == "G":
                        Move_status = True
                    elif dice == 6 and key[0] == "Y":
                        Move_status = True
                    elif dice == 6 and key[0] == "B":
                        Move_status = True

                else:   
                    if self.prog[key] + dice <= 57:
                        Move_status = True
                    
            if Move_status:
                print(f"Invalid move by {self.current_player.color}. Game Terminated!")
                return True
        return False            
            
    def update_board(self):
        dice = random.randint(1, 6)
        self.current_player = self.players[self.turn]
    
        if self.current_player.color in self.winners:
            self.turn += 1
            if self.turn >= 4:
                self.turn %= 4
            return "next"
        print("*"*75)
        print(f"{self.current_player.color} rolled: {dice}")
    
        piece = self.current_player.move_piece(dice, self)
        
        move_status = False
    
        if self.prog[piece] == 0:
            if dice == 6 and piece[0] == "R":
                self.board[piece] = 1
                self.prog[piece] = 1
                print(f"{piece} moved to {self.board[piece]}")
                move_status = True
            elif dice == 6 and piece[0] == "G":
                self.board[piece] = 14
                self.prog[piece] = 1
                print(f"{piece} moved to {self.board[piece]}")
                move_status = True
            elif dice == 6 and piece[0] == "Y":
                self.board[piece] = 27
                self.prog[piece] = 1
                print(f"{piece} moved to {self.board[piece]}")
                move_status = True
            elif dice == 6 and piece[0] == "B":
                self.board[piece] = 40
                self.prog[piece] = 1
                print(f"{piece} moved to {self.board[piece]}")
                move_status = True
    
        else:
            if self.prog[piece] + dice <= 57:
    
                if self.board[piece] != 100:
                    self.board[piece] += dice
    
                self.prog[piece] += dice
                move_status = True
    
                result = self.move_and_capture(piece)
    
                if result == "reroll":
                    self.board[piece] -= dice
                    if self.board[piece] <= 0:
                        self.board[piece] += 52
                    self.prog[piece] -= dice
    
                    print("*"*75)
                    return "next"
    
                elif result == "win":
                    print("*"*75)
                    return "next"
    
                if piece in self.prog and self.prog[piece] > 51:
                    self.board[piece] = 100
    
        if not move_status:
            if self.check_move_status(dice, piece):
                return "terminated"
    
        if self.current_player.in_pieces == 4:
            print(f"Player {self.current_player.color} has won the game!")
            self.winners.append(self.current_player.color)
            self.player_no -= 1
            
            if self.player_no == 1:
                print("Game Ends!")
        
                for i in range(3):
                    print(f"Ranking {i+1}: Player {self.winners[i]}")
        
                print("*"*75)
                return "over"
            self.turn += 1
            if self.turn >= 4:
                self.turn %= 4
            return "next"
    
        if dice != 6:
            self.turn += 1
    
            if self.turn >= 4:
                self.turn %= 4
    
        print("*"*75)
    
        if move_status:
            return "next"
    
        return None
    def view_board(board):
    rs,rc="\U0001F7E5","\U0001F534"
    gs,gc="\U0001F7E9","\U0001F7E2"
    ys,yc="\U0001F7E8","\U0001F7E1"
    bs,bc="\U0001F7E6","\U0001F535"
    ws= "\U00002B1C"
    bl="\U00002B1B"
    L=[

        [bs, bs, bs, bs, bs, bs, ws, ws, ws, rs, rs, rs, rs, rs, rs],
        [bs, bc, ws, ws, bc, bs, ws, rs, rs, rs, rc, ws, ws, rc, rs],
        [bs, ws, ws, ws, ws, bs, bl, rs, ws, rs, ws, ws, ws, ws, rs],
        [bs, ws, ws, ws, ws, bs, ws, rs, ws, rs, ws, ws, ws, ws, rs],
        [bs, bc, ws, ws, bc, bs, ws, rs, ws, rs, rc, ws, ws, rc, rs],
        [bs, bs, bs, bs, bs, bs, ws, rs, ws, rs, rs, rs, rs, rs, rs],
        [ws, bs, ws, ws, ws, ws, bl, bl, bl, ws, ws, ws, bl, ws, ws],
        [ws, bs, bs, bs, bs, bs, bl, bl, bl, gs, gs, gs, gs, gs, ws],
        [ws, ws, bl, ws, ws, ws, bl, bl, bl, ws, ws, ws, ws, gs, ws],
        [ys, ys, ys, ys, ys, ys, ws, ys, ws, gs, gs, gs, gs, gs, gs],
        [ys, yc, ws, ws, yc, ys, ws, ys, ws, gs, gc, ws, ws, gc, gs],
        [ys, ws, ws, ws, ws, ys, ws, ys, ws, gs, ws, ws, ws, ws, gs],
        [ys, ws, ws, ws, ws, ys, ws, ys, bl, gs, ws, ws, ws, ws, gs],
        [ys, yc, ws, ws, yc, ys, ys, ys, ws, gs, gc, ws, ws, gc, gs],
        [ys, ys, ys, ys, ys, ys, ws, ws, ws, gs, gs, gs, gs, gs, gs],


    ]
    pos = {1: (2, 9), 2: (3,9), 3: (4,9), 4: (5,9), 5: (6,9), 6: (7,10), 7: (7,11), 8: (7,12), 9: (7,13), 10: (7,14),
           11: (7,15), 12: (8,15), 13: (9,15), 14: (9,14), 15: (9,13), 16: (9,12), 17: (9,11), 18: (9,10), 19: (10,9), 20: (11, 9),
           21: (12,9), 22: (13,9), 23: (14,9), 24: (15,9), 25: (15,8), 26: (15,7), 27: (14,7), 28: (13,7), 29: (12,7), 30: (11,7),
           31: (10,7), 32: (9,6), 33: (9,5), 34: (9,4), 35: (9,3), 36: (9,2), 37: (9,1), 38: (8,1), 39: (7,1), 40: (7,2),
           41: (7,3), 42: (7,4), 43: (7,5), 44: (7,6), 45: (6,7), 46: (5,7), 47: (4,7), 48: (3,7), 49: (2,7), 50: (1,7),
           51: (1,8), 52: (1,9),
           'R1': (2,11) ,'R2': (2,14), 'R3': (5,11) ,'R4': (5,14),
           'G1': (11,11), 'G2': (11,14), 'G3': (14,11), 'G4': (14,14),
           'Y1': (2,2), 'Y2': (2,5), 'Y3': (2,2), 'Y4': (2,5),
           'B1': (11,2), 'B2': (11,5), 'B3': (14,2), 'B4': (14,5),


           }
    for i in board:
        if board[i] in [0,'L','W']:
            continue
        if i[0]=='R':
            p=rc
        if i[0]=='G':
            p=gc
        if i[0]=='B':
            p=bc
        if i[0]=='Y':
            p=yc
        coordinates=pos[board[i]]
        y_coord=coordinates[0]
        x_coord=coordinates[1]
        L[y_coord-1][x_coord-1]=p
        L[pos[i][0]-1][pos[i][1]-1] = bl


    for i in L:
        for j in i:
            print(j,end=" ")
        print()
