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

    def __eq__(self, other):
        if not isinstance(other, PianoMoverState):
            return False
        return self.representation == other.representation

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.representation.__hash__()

    def print_state(self):
        self.representation.print_grid()
        print(" g(n): {}".format(self.g))
        print(" h(n): {}".format(self.h))
        print(" f(n): {}".format(self.f))

    def is_victory(self):
        return self.representation.is_victory()
