from state import TicTacToeState


class TicTacToeGame:
    def neighbors(self, state, turn):
        children = set([])

        moves = []
        for i in range(0, 3):
            for j in range(0, 3):
                if state.representation.grid[i][j] == ".":
                    move = state.representation.move((i, j), turn)
                    child = TicTacToeState(representation=move, turn=turn)
                    moves.append(child)

        for move in moves:
            if move is not None:
                children.add(move)

        return children
