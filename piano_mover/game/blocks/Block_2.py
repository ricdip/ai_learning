import random
from copy import deepcopy
import game

# 2 obstacles
class Block_2:
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
            self.body_x = pos[1][0]
            self.body_y = pos[1][1]

        self.value = 2

    def move_up(self):
        new_head_x = self.head_x - 1
        new_head_y = self.head_y
        new_body_x = self.body_x - 1
        new_body_y = self.body_y
        new_pos = []
        new_pos.append((new_head_x, new_head_y))
        new_pos.append((new_body_x, new_body_y))

        return self.__move(new_pos)

    def move_down(self):
        new_head_x = self.head_x + 1
        new_head_y = self.head_y
        new_body_x = self.body_x + 1
        new_body_y = self.body_y
        new_pos = []
        new_pos.append((new_head_x, new_head_y))
        new_pos.append((new_body_x, new_body_y))

        return self.__move(new_pos)

    def move_left(self):
        new_head_x = self.head_x
        new_head_y = self.head_y - 1
        new_body_x = self.body_x
        new_body_y = self.body_y - 1
        new_pos = []
        new_pos.append((new_head_x, new_head_y))
        new_pos.append((new_body_x, new_body_y))

        return self.__move(new_pos)

    def move_right(self):
        new_head_x = self.head_x
        new_head_y = self.head_y + 1
        new_body_x = self.body_x
        new_body_y = self.body_y + 1
        new_pos = []
        new_pos.append((new_head_x, new_head_y))
        new_pos.append((new_body_x, new_body_y))

        return self.__move(new_pos)

    def __move(self, new_pos):
        if not self.__collision(new_pos):
            new_blocks = deepcopy(self.repr.blocks)
            new_repr = game.PianoMoverRepresentation(
                dim=self.repr.dim, blocks=new_blocks
            )
            new_repr.update_block(Block_2(self.id, new_repr, new_pos))

            return new_repr
        return None

    def __generate_positions(self):
        while True:
            block_type = random.choice(["hz", "vt"])
            # H*
            if block_type == "hz":
                self.head_x = random.randint(0, self.repr.get_grid_shape()[0] - 1)
                self.head_y = random.randint(0, self.repr.get_grid_shape()[1] - 2)

                self.body_x = self.head_x
                self.body_y = self.head_y + 1

            # H
            # *
            elif block_type == "vt":
                self.head_x = random.randint(0, self.repr.get_grid_shape()[0] - 2)
                self.head_y = random.randint(0, self.repr.get_grid_shape()[1] - 1)

                self.body_x = self.head_x + 1
                self.body_y = self.head_y

            if (self.repr.grid[self.head_x, self.head_y] == 0) and (
                self.repr.grid[self.body_x, self.body_y] == 0
            ):
                break

        self.pos = []
        self.pos.append((self.head_x, self.head_y))
        self.pos.append((self.body_x, self.body_y))

    def __collision(self, new_pos):
        for pos in new_pos:
            if (
                pos[0] < 0
                or pos[0] > self.repr.get_grid_shape()[0] - 1
                or pos[1] < 0
                or pos[1] > self.repr.get_grid_shape()[1] - 1
                or self.__block_collision(new_pos)
            ):
                return True

        return False

    def __block_collision(self, new_pos):
        for k in self.repr.blocks:
            if self.repr.blocks[k].id != "exit" and self.repr.blocks[k].id != self.id:
                for pos in self.repr.blocks[k].pos:
                    if pos in new_pos:
                        return True

        return False
