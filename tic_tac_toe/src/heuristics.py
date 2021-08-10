from game import TicTacToeGame

game = TicTacToeGame()


class Heuristic:
    # leaf node valuation
    def H(self, state):
        if state.victory() is None:
            return 0

        if state.victory() == "X":
            # X is maximizer
            return 10

        elif state.victory() == "O":
            # O is minimizer
            return -10

    # minmax heuristic
    def H1(self, state, depth, turn):
        if depth == 0 or state.game_over():
            # static valuation of state
            return self.H(state)

        if turn == "X":
            # maximizer
            max_val = float("-inf")
            for move in game.neighbors(state, turn):
                val = self.H1(move, depth - 1, "O")
                max_val = max(max_val, val)
            return max_val

        if turn == "O":
            # minimizer
            min_val = float("inf")
            for move in game.neighbors(state, turn):
                val = self.H1(move, depth - 1, "X")
                min_val = min(min_val, val)
            return min_val

    # minmax alpha-beta pruning heuristic
    def H2(self, state, depth, alpha, beta, turn):
        if depth == 0 or state.game_over():
            # static valuation of state
            return self.H(state)

        if turn == "X":
            # maximizer
            max_val = float("-inf")
            for move in game.neighbors(state, turn):
                val = self.H2(move, depth - 1, alpha, beta, "O")
                max_val = max(max_val, val)
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
            return max_val

        if turn == "O":
            # minimizer
            min_val = float("inf")
            for move in game.neighbors(state, turn):
                val = self.H2(move, depth - 1, alpha, beta, "X")
                min_val = min(min_val, val)
                beta = min(beta, val)
                if beta <= alpha:
                    break
            return min_val
