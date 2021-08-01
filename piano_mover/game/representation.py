import numpy as np
from colorama import Fore, Style


class Representation:
    def is_victory(self):
        return False


class PianoMoverRepresentation(Representation):
    def __init__(self, dim=(10, 10), grid=None, blocks=None):
        if grid is None:
            self.grid = np.zeros(shape=dim, dtype=int)
            self.blocks = self.__generate_blocks()
        else:
            self.grid = grid
            self.blocks = blocks

    # random block generation
    def __generate_blocks(self):
        return {}

    # get grid shape: (x, y)
    def get_grid_shape(self):
        return np.shape(self.grid)

    # print colored grid
    def print_grid(self):
        for i in range(self.get_grid_shape()[0]):
            for j in range(self.get_grid_shape()[1]):
                if self.grid[i, j] == 0:
                    # empty cell
                    print(
                        " {}{}{} ".format(Fore.BLUE, self.grid[i, j], Style.RESET_ALL),
                        end="",
                    )
                elif (
                    self.grid[i, j] == 1 or self.grid[i, j] == 2 or self.grid[i, j] == 3
                ):
                    # obstacle's cell
                    print(
                        " {}{}{} ".format(Fore.RED, self.grid[i, j], Style.RESET_ALL),
                        end="",
                    )
                elif self.grid[i, j] == 4:
                    # piano's cell
                    print(
                        " {}{}{} ".format(
                            Fore.YELLOW, self.grid[i, j], Style.RESET_ALL
                        ),
                        end="",
                    )
                elif self.grid[i, j] == 5:
                    # exit's cell
                    print(
                        " {}{}{} ".format(Fore.GREEN, self.grid[i, j], Style.RESET_ALL),
                        end="",
                    )
            print()
