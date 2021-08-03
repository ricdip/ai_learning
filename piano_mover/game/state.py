from .representation import PianoMoverRepresentation


class State:
    def __init__(
        self,
        parent=None,
        representation=None,
        g=0,
    ):
        pass

    def is_victory(self):
        return False


class PianoMoverState(State):
    def __init__(
        self,
        parent=None,
        representation=None,
        g=0,
    ):
        self.parent = parent

        if representation is None:
            # in case we don't have a representation, we create a default one (initial representation with a 10x10 grid)
            self.representation = PianoMoverRepresentation()
        else:
            # we already have a representation, we assign it
            self.representation = representation

        self.g = g
        self.h = None
        self.f = None

    def is_victory(self):
        return self.representation.is_victory()
