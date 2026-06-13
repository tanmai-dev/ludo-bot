class goti:
    def __init__(self, color, number):
        self.active = False
        self.color = color
        self.number = number
        self.position = "base"
        self.progression = 0

class Player:
    def __init__(self, color):
        self.active = False
        self.piece1 = goti(color, 1)
        self.piece2 = goti(color, 2)
        self.piece3 = goti(color, 3)
        self.piece4 = goti(color, 4)
        self.current_piece = None

    def move_piece(self, dice, game_state):
        print(game_state)
        print(dice)
        choice=input('enter a piece')
        return choice

