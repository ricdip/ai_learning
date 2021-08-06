from .state import PianoMoverState


class Game:
    def neighbors(self, state):
        return set([])


class PianoMoverGame(Game):
    def neighbors(self, state):
        children = set([])

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
                # we create ammissible states
                child = PianoMoverState(parent=state, representation=move)
                children.add(child)

        return children
