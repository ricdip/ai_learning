import random
from copy import deepcopy
import game

# 1 obstacles
class Block_1:
    def __init__(self, id=None, representation=None, pos=None):
        self.id = id
        self.repr = representation

        if pos is None:
            self.pos = []
            self.__generate_positions()
        else:
            self.pos = pos
            self.head_x = pos[0][0]
            self.head_y = pos[0][1]

        self.value = 1

    def move_up(self):
        new_head_x = self.head_x - 1
        new_head_y = self.head_y
        new_pos = []
        new_pos.append((new_head_x, new_head_y))

        if not self.__collision(new_pos):
            new_blocks = deepcopy(self.repr.blocks)
            new_repr = game.PianoMoverRepresentation(
                dim=self.repr.dim, blocks=new_blocks
            )
            new_repr.update_block(Block_1(self.id, new_repr, new_pos))

            return new_repr
        return None

    def __generate_positions(self):
        while True:
            # H
            self.head_x = random.randint(0, self.repr.get_grid_shape()[0] - 1)
            self.head_y = random.randint(0, self.repr.get_grid_shape()[1] - 1)

            if self.repr.grid[self.head_x, self.head_y] == 0:
                break

        self.pos = []
        self.pos.append((self.head_x, self.head_y))

    def __collision(self, new_pos):
        for pos in new_pos:
            if (
                pos[0] < 0
                or pos[0] > self.repr.get_grid_shape()[0] - 1
                or pos[1] < 0
                or pos[1] > self.repr.get_grid_shape()[1] - 1
                or self.repr.grid[pos[0], pos[1]] != 0
            ):
                return True

        return False
