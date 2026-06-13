class Player:
    def __init__(self, color):
        self.active = False
        self.color = color
        self.current_piece = None
        self.in_pieces = 0

    def move_piece(self, dice, game_state):
        print(game_state)
        print(dice)
        choice=input('enter a piece')
        return choice

