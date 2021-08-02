import numpy as np
from colorama import Fore, Style
from .blocks import Block_1, Block_2, Block_3, Piano, Exit


class Representation:
    def is_victory(self):
        return False


class PianoMoverRepresentation(Representation):
    def __init__(self, dim=(10, 10), blocks=None):
        self.dim = dim
        self.grid = np.zeros(shape=dim, dtype=int)

        if blocks is None:
            self.blocks = {}
            self.__generate_blocks()
        else:
            self.blocks = blocks
            self.update_grid()

    # random block generation
    def __generate_blocks(self):
        self.blocks[0] = Piano(self)
        self.update_grid()
        self.blocks[1] = Exit(self, self.blocks[0])
        self.update_grid()
        self.blocks[2] = Block_3(self)
        self.update_grid()
        self.blocks[3] = Block_3(self)
        self.update_grid()
        self.blocks[4] = Block_3(self)
        self.update_grid()
        self.blocks[5] = Block_3(self)
        self.update_grid()
        self.blocks[6] = Block_3(self)
        self.update_grid()
        self.blocks[7] = Block_3(self)
        self.update_grid()
        self.blocks[8] = Block_2(self)
        self.update_grid()
        self.blocks[9] = Block_2(self)
        self.update_grid()
        self.blocks[10] = Block_1(self)
        self.update_grid()

    def update_grid(self):
        self.grid = np.zeros(shape=self.dim, dtype=int)
        for k in self.blocks:
            block = self.blocks[k]
            for block_coordinates in block.pos:
                self.grid[block_coordinates[0], block_coordinates[1]] = block.value

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
