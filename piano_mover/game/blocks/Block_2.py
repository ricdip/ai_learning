import random

# 2 obstacles
class Block_2:
    def __init__(self, representation=None):
        self.repr = representation
        self.pos = []
        self.value = 2
        self.head_x = None
        self.head_y = None
        self.body_x = None
        self.body_y = None

        self.__generate_positions()

    def move_up(self):
        pass

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

    def __update_repr(self):
        self.repr.update_grid()
