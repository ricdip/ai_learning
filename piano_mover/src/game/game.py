from .state import PianoMoverState


class Game:
    def __init__(self, heuristic=None, f_valuation=None):
        pass

    def neighbors(self, state):
        return set([])


class PianoMoverGame(Game):
    def __init__(self, heuristic=None, f_valuation=None):
        self.H = heuristic
        self.F = f_valuation

    def neighbors(self, state):
        if state.f is None:
            # initial state
            self.assign_scores(state)

        children = []
        # perform all possible moves
        moves = []
        for block in state.representation.blocks:
            if block != "exit":
                moves.append(state.representation.blocks[block].move_up())
                moves.append(state.representation.blocks[block].move_down())
                moves.append(state.representation.blocks[block].move_left())
                moves.append(state.representation.blocks[block].move_right())
        for move in moves:
            if move is not None:
                child = PianoMoverState(
                    parent=state, representation=move, g=state.g + 1
                )
                self.assign_scores(child)
                children.append(child)

        return set(children)

    def assign_scores(self, state):
        state.h = self.H(state)
        state.f = self.F(state.g, state.h)
