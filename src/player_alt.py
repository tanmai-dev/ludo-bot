import random

class EvilPlayer:
    def __init__(self, color):
        self.active = False
        self.color = color
        self.current_piece = None
        self.in_pieces = 0

    def move_piece(self, dice, game_state):

        legal_moves = []
        illegal_moves = []

        for i in range(1, 5):
            piece = self.color + str(i)

            if piece not in game_state.prog:
                continue

            prog = game_state.prog[piece]

            legal = False

            if prog == 0:
                if dice == 6:
                    legal = True
            else:
                if prog + dice <= 57:
                    legal = True

            if legal:
                legal_moves.append(piece)
            else:
                illegal_moves.append(piece)

        # If there is at least one legal move,
        # intentionally choose an illegal one.
        if legal_moves and illegal_moves:
            return random.choice(illegal_moves)

        # Otherwise behave normally.
        if legal_moves:
            return random.choice(legal_moves)

        # No legal moves exist, return any remaining piece.
        if illegal_moves:
            return random.choice(illegal_moves)

        return None 

