class Game:
    def __init__(self, heuristic=None, f_valuation=None):
        pass

    def neighbors(self, state):
        return set([])


class PianoMoverGame(Game):
    def __init__(self, heuristic=None, f_valuation=None):
        self.H = heuristic.H
        self.F = f_valuation.F

    def neighbors(self, state):
        return set([])
