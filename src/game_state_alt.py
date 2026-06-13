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

        if self.board[piece] > 52 and self.board[piece] != 'L':
            self.board[piece] -= 52
        
        
        if self.board[piece] not in [1, 9, 14, 22, 27, 35, 40, 48]:
            for i in self.board:
                if self.board[i] == self.board[piece] and i != piece and self.board[i] != 'L' and i[0]!= piece[0]:
                    self.board[i] = 0
                    self.prog[i] = 0
                elif self.board[i] == self.board[piece] and i != piece and self.board[i] != 'L' and i[0] == piece[0]:
                    return "reroll"
        
        if self.prog[piece] == 57:
                print(f"Peg {piece} has reached the end!")
                self.current_player.in_pieces += 1
                del self.board[piece]
                del self.prog[piece]
                return "win"
        
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
        print("*"*75)
        dice = random.randint(1, 6)
        self.current_player = self.players[self.turn]
        print("Dice rolled:", dice)
    
        piece = self.current_player.move_piece(dice, self)
    
        move_status = False
    
        if self.prog[piece] == 0:
            if dice == 6 and piece[0] == "R":
                self.board[piece] = 1
                self.prog[piece] = 1
                move_status = True
            elif dice == 6 and piece[0] == "G":
                self.board[piece] = 14
                self.prog[piece] = 1
                move_status = True
            elif dice == 6 and piece[0] == "Y":
                self.board[piece] = 27
                self.prog[piece] = 1
                move_status = True
            elif dice == 6 and piece[0] == "B":
                self.board[piece] = 40
                self.prog[piece] = 1
                move_status = True
    
        else:
            if self.prog[piece] + dice <= 57:
    
                if self.board[piece] != 'L':
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
                    self.board[piece] = 'L'
    
        if not move_status:
            if self.check_move_status(dice, piece):
                return "terminated"
    
        if self.current_player.in_pieces == 4:
            print(f"Player {self.current_player.color} has won the game!")
    
            self.players.remove(self.current_player)
            self.winners.append(self.current_player.color)
            self.player_no -= 1
    
            if self.player_no == 1:
                print("Game Ends!")
        
                for i in range(3):
                    print(f"Ranking {i+1}: Player {self.winners[i]}")
        
                print("*"*75)
                return "over"
            return "next"
    
        if dice != 6:
            self.turn += 1
    
            if self.turn >= self.player_no:
                self.turn %= self.player_no
    
        print("*"*75)
    
        if move_status:
            return "next"
    
        return None
