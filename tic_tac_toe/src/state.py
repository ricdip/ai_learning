from representation import TicTacToeRepresentation


class TicTacToeState:
    def __init__(self, representation=None, turn=None):
        if representation is None:
            self.representation = TicTacToeRepresentation()
        else:
            self.representation = representation

        self.turn = turn

    def victory(self):
        return self.representation.victory()

    def game_over(self):
        return self.representation.game_over()

    def print_state(self):
        self.representation.print_grid()
