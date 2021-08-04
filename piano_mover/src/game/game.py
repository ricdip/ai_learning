from .state import PianoMoverState


class Game:
    def __init__(self, heuristic=None, g_valuation=None, f_valuation=None):
        pass

    def neighbors(self, state):
        return set([])


class PianoMoverGame(Game):
    def __init__(self, heuristic=None, g_valuation=None, f_valuation=None):
        self.H = heuristic
        self.G = g_valuation
        self.F = f_valuation

    def neighbors(self, state):
        if state.f is None:
            # initial state
            self.assign_scores(state, None)

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
                child = PianoMoverState(parent=state, representation=move)
                self.assign_scores(child, state)
                children.append(child)

        return set(children)

    def assign_scores(self, curr_state, parent_state):
        curr_state.h = self.H(curr_state)
        curr_state.g = self.G(curr_state, parent_state)
        curr_state.f = self.F(curr_state.g, curr_state.h)
