import random

# 3 obstacles
class Block_3:
    def __init__(self, representation=None):
        self.repr = representation
        self.pos = []
        self.value = 3
        self.head_x = None
        self.head_y = None
        self.body_1_x = None
        self.body_1_y = None
        self.body_2_x = None
        self.body_2_y = None

        self.__generate_positions()

    def move_up(self):
        pass

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

    def __update_repr(self):
        self.repr.update_grid()
