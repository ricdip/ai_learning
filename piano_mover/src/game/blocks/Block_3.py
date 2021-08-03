import random
from copy import deepcopy
import game

# 3 obstacles
class Block_3:
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
            self.body_1_x = pos[1][0]
            self.body_1_y = pos[1][1]
            self.body_2_x = pos[2][0]
            self.body_2_y = pos[2][1]

        self.value = 3

    def move_up(self):
        new_head_x = self.head_x - 1
        new_head_y = self.head_y
        new_body_1_x = self.body_1_x - 1
        new_body_1_y = self.body_1_y
        new_body_2_x = self.body_2_x - 1
        new_body_2_y = self.body_2_y
        new_pos = []
        new_pos.append((new_head_x, new_head_y))
        new_pos.append((new_body_1_x, new_body_1_y))
        new_pos.append((new_body_2_x, new_body_2_y))

        return self.__move(new_pos)

    def move_down(self):
        new_head_x = self.head_x + 1
        new_head_y = self.head_y
        new_body_1_x = self.body_1_x + 1
        new_body_1_y = self.body_1_y
        new_body_2_x = self.body_2_x + 1
        new_body_2_y = self.body_2_y
        new_pos = []
        new_pos.append((new_head_x, new_head_y))
        new_pos.append((new_body_1_x, new_body_1_y))
        new_pos.append((new_body_2_x, new_body_2_y))

        return self.__move(new_pos)

    def move_left(self):
        new_head_x = self.head_x
        new_head_y = self.head_y - 1
        new_body_1_x = self.body_1_x
        new_body_1_y = self.body_1_y - 1
        new_body_2_x = self.body_2_x
        new_body_2_y = self.body_2_y - 1
        new_pos = []
        new_pos.append((new_head_x, new_head_y))
        new_pos.append((new_body_1_x, new_body_1_y))
        new_pos.append((new_body_2_x, new_body_2_y))

        return self.__move(new_pos)

    def move_right(self):
        new_head_x = self.head_x
        new_head_y = self.head_y + 1
        new_body_1_x = self.body_1_x
        new_body_1_y = self.body_1_y + 1
        new_body_2_x = self.body_2_x
        new_body_2_y = self.body_2_y + 1
        new_pos = []
        new_pos.append((new_head_x, new_head_y))
        new_pos.append((new_body_1_x, new_body_1_y))
        new_pos.append((new_body_2_x, new_body_2_y))

        return self.__move(new_pos)

    def __move(self, new_pos):
        if not self.__collision(new_pos):
            new_blocks = deepcopy(self.repr.blocks)
            new_repr = game.PianoMoverRepresentation(
                dim=self.repr.dim, blocks=new_blocks
            )
            new_repr.update_block(Block_3(self.id, new_repr, new_pos))

            return new_repr
        return None

    def __generate_positions(self):
        while True:
            block_type = random.choice(["hz", "vt", "l_1", "l_2", "l_3", "l_4"])

            # H**
            if block_type == "hz":
                self.head_x = random.randint(0, self.repr.get_grid_shape()[0] - 1)
                self.head_y = random.randint(0, self.repr.get_grid_shape()[1] - 3)

                self.body_1_x = self.head_x
                self.body_1_y = self.head_y + 1
                self.body_2_x = self.head_x
                self.body_2_y = self.head_y + 2

            # H
            # *
            # *
            elif block_type == "vt":
                self.head_x = random.randint(0, self.repr.get_grid_shape()[0] - 3)
                self.head_y = random.randint(0, self.repr.get_grid_shape()[1] - 1)

                self.body_1_x = self.head_x + 1
                self.body_1_y = self.head_y
                self.body_2_x = self.head_x + 2
                self.body_2_y = self.head_y

            # H*
            # *
            elif block_type == "l_1":
                self.head_x = random.randint(0, self.repr.get_grid_shape()[0] - 2)
                self.head_y = random.randint(0, self.repr.get_grid_shape()[1] - 2)

                self.body_1_x = self.head_x
                self.body_1_y = self.head_y + 1
                self.body_2_x = self.head_x + 1
                self.body_2_y = self.head_y

            # H*
            #  *
            elif block_type == "l_2":
                self.head_x = random.randint(0, self.repr.get_grid_shape()[0] - 2)
                self.head_y = random.randint(0, self.repr.get_grid_shape()[1] - 2)

                self.body_1_x = self.head_x
                self.body_1_y = self.head_y + 1
                self.body_2_x = self.head_x + 1
                self.body_2_y = self.head_y + 1

            # H
            # **
            elif block_type == "l_3":
                self.head_x = random.randint(0, self.repr.get_grid_shape()[0] - 2)
                self.head_y = random.randint(0, self.repr.get_grid_shape()[1] - 2)

                self.body_1_x = self.head_x + 1
                self.body_1_y = self.head_y
                self.body_2_x = self.head_x + 1
                self.body_2_y = self.head_y + 1

            #  H
            # **
            elif block_type == "l_4":
                self.head_x = random.randint(0, self.repr.get_grid_shape()[0] - 2)
                self.head_y = random.randint(1, self.repr.get_grid_shape()[1] - 1)

                self.body_1_x = self.head_x + 1
                self.body_1_y = self.head_y
                self.body_2_x = self.head_x + 1
                self.body_2_y = self.head_y - 1

            if (
                (self.repr.grid[self.head_x, self.head_y] == 0)
                and (self.repr.grid[self.body_1_x, self.body_1_y] == 0)
                and (self.repr.grid[self.body_2_x, self.body_2_y] == 0)
            ):
                break

        self.pos = []
        self.pos.append((self.head_x, self.head_y))
        self.pos.append((self.body_1_x, self.body_1_y))
        self.pos.append((self.body_2_x, self.body_2_y))

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