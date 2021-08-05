import numpy as np
from colorama import Fore, Back, Style
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

        self.moved_block = None

    def __eq__(self, other):
        if not isinstance(other, PianoMoverRepresentation):
            return False
        return np.array_equal(self.grid, other.grid)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.grid))

    # random block generation
    def __generate_blocks(self):
        self.blocks["piano"] = Piano("piano", self)
        self.update_grid()
        self.blocks["exit"] = Exit("exit", self, self.blocks["piano"])
        self.update_grid()
        self.blocks["3_1"] = Block_3("3_1", self)
        self.update_grid()
        self.blocks["3_2"] = Block_3("3_2", self)
        self.update_grid()
        self.blocks["3_3"] = Block_3("3_3", self)
        self.update_grid()
        self.blocks["3_4"] = Block_3("3_4", self)
        self.update_grid()
        self.blocks["3_5"] = Block_3("3_5", self)
        self.update_grid()
        self.blocks["3_6"] = Block_3("3_6", self)
        self.update_grid()
        self.blocks["2_1"] = Block_2("2_1", self)
        self.update_grid()
        self.blocks["2_2"] = Block_2("2_2", self)
        self.update_grid()
        self.blocks["1_1"] = Block_1("1_1", self)
        self.update_grid()

    def update_block(self, block):
        self.blocks[block.id] = block
        self.update_grid()

    def update_grid(self):
        self.grid = np.zeros(shape=self.dim, dtype=int)
        for k in self.blocks:
            if k != "exit":
                block = self.blocks[k]
                for block_coordinates in block.pos:
                    self.grid[block_coordinates[0], block_coordinates[1]] = block.value

    # get grid shape: (x, y)
    def get_grid_shape(self):
        return np.shape(self.grid)

    # print colored grid
    def print_grid(self):
        exit_block = self.blocks.get("exit")

        for i in range(self.get_grid_shape()[0]):
            for j in range(self.get_grid_shape()[1]):
                exit_block_cell = (exit_block is not None) and (
                    (i == exit_block.head_x and j == exit_block.head_y)
                    or (i == exit_block.body_1_x and j == exit_block.body_1_y)
                    or (i == exit_block.body_2_x and j == exit_block.body_2_y)
                    or (i == exit_block.body_3_x and j == exit_block.body_3_y)
                )

                if self.grid[i, j] == 0 and not exit_block_cell:
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
                elif exit_block_cell:
                    # exit's cell
                    print(
                        "{} {} {}".format(Back.GREEN, self.grid[i, j], Style.RESET_ALL),
                        end="",
                    )
            print()

    def is_victory(self):
        exit_block = self.blocks["exit"]
        piano_block = self.blocks["piano"]

        if len(exit_block.pos) != len(piano_block.pos):
            return False

        return (
            (piano_block.pos[0] == exit_block.pos[0])
            and (piano_block.pos[1] == exit_block.pos[1])
            and (piano_block.pos[2] == exit_block.pos[2])
            and (piano_block.pos[3] == exit_block.pos[3])
        )
