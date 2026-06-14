class SW_LudoBot1:
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
        enemy_pieces=[p for p in game_state.board.keys() if not p.startswith(self.color)]
        if not legal_moves:
            return None
        #capture check
        for p in legal_moves:
            if game_state.prog[p] > 0 and game_state.prog[p] +dice <= 51:
                curr_pos = game_state.board[p]
                new_pos=(curr_pos+dice-1)%52 + 1
                for ep in enemy_pieces:
                    if game_state.board[ep]==new_pos:
                        return p

        #opening a piece
        if dice == 6:
            for p in legal_moves:
                if game_state.prog[p] == 0:
                    return p

        #escaping
        for p in legal_moves:
            if game_state.prog[p] > 0 and game_state.board[p] not in (0, 100):
                curr_pos = game_state.board[p]

                for ep in enemy_pieces:
                    ep_pos = game_state.board[ep]
                    if ep_pos not in (0, 100):

                        dist_behind = (curr_pos - ep_pos) % 52
                        if 1 <= dist_behind <= 6:
                            return p
        legal_moves.sort(key=lambda x: game_state.prog[x], reverse=True)
        return legal_moves[0]
