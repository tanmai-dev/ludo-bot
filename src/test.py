def capture(self, piece):

    if self.board[piece] > 52:
        self.board[piece] -= 52
    
    if self.board[piece] not in [1, 9, 14, 22, 27, 35, 40, 48]:
        for i in self.board:
            if self.board[i] == self.board[piece] and i != piece and self.board[i] != 'L' and i[0]!= piece[0]:
                self.board[i] = 0
                self.prog[i] = 0
            elif self.board[i] == self.board[piece] and i != piece and self.board[i] != 'L' and i[0] == piece[0]:
                return False

print(-3 % 52)