class goti:
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.position = "base"

class Player:
    def __init__(self, color):
        self.piece1 = goti(color, 1)
        self.piece2 = goti(color, 2)
        self.piece3 = goti(color, 3)
        self.piece4 = goti(color, 4)
    
    def move_piece(self, dice, game_state):
            