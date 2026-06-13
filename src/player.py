import random

class Player:
    def __init__(self, color):
        self.active = False
        self.color = color
        self.current_piece = None
        self.in_pieces = 0

    def move_piece(self, dice, game_state):

        legal_moves = []

        for i in range(1, 5):
            piece = self.color + str(i)

            if piece not in game_state.prog:
                continue

            prog = game_state.prog[piece]

            # piece in home
            if prog == 0:
                if dice == 6:
                    legal_moves.append(piece)

            # piece already active
            else:
                if prog + dice <= 57:
                    legal_moves.append(piece)

        if legal_moves:
            return random.choice(legal_moves)

        # no legal move exists
        for i in range(1, 5):
            piece = self.color + str(i)
            if piece in game_state.prog:
                return piece
