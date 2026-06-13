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

            # piece already finished
            if piece not in game_state.prog:
                continue

            if game_state.prog[piece] == 0:
                if dice == 6:
                    legal_moves.append(piece)
            else:
                if game_state.prog[piece] + dice <= 57:
                    legal_moves.append(piece)

        if legal_moves:
            return random.choice(legal_moves)

        # no legal move exists
        # return ANY surviving piece
        for i in range(1, 5):
            piece = self.color + str(i)

            if piece in game_state.prog:
                return piece
            else:
                continue
