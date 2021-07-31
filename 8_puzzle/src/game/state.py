from .repr import Repr


# game state
class State:
    def __init__(self, parent=None, g=0, repr=None, heuristic=None, f_valuation=None):
        self.parent = parent
        self.g = g
        self.heuristic = heuristic
        self.f_valuation = f_valuation

        if repr is None:
            self.repr = Repr()
        else:
            self.repr = repr

        self.victory = self.repr.is_victory()

        self.h = self.heuristic(self)

        self.f = self.f_valuation(self.g, self.h)

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self.repr == other.repr

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.repr.__hash__()

    def neighbors(self):
        children = []
        moves = [
            self.repr.move_up(),
            self.repr.move_down(),
            self.repr.move_left(),
            self.repr.move_right(),
        ]

        for move in moves:
            if move is not None:
                children.append(
                    State(
                        self, self.g + 1, Repr(move), self.heuristic, self.f_valuation
                    )
                )

        return children

    def print_state(self):
        self.repr.print_grid()
        print()
        print(" g(n): {}".format(self.g))
        print(" h(n): {}".format(self.h))
        print(" f(n): {}".format(self.f))
        print("------------------------")
        print()
