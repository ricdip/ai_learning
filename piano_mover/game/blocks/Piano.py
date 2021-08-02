import random

# piano
class Piano:
    def __init__(self, representation=None):
        self.repr = representation
        self.pos = []
        self.value = 4
        self.head_x = None
        self.head_y = None
        self.body_1_x = None
        self.body_1_y = None
        self.body_2_x = None
        self.body_2_y = None
        self.body_3_x = None
        self.body_3_y = None

        self.__generate_positions()

    def move_up(self):
        pass

    def __generate_positions(self):
        while True:
            # H*
            # **
            # orientation 1 -> piano on bottom of grid
            # orientation 2 -> piano on left of grid
            orientation = random.choice([0, 1])
            if orientation == 0:
                self.head_x = self.repr.get_grid_shape()[0] - 2
                self.head_y = random.randint(0, self.repr.get_grid_shape()[1] - 2)
            elif orientation == 1:
                self.head_x = random.randint(0, self.repr.get_grid_shape()[1] - 2)
                self.head_y = 0

            self.body_1_x = self.head_x
            self.body_1_y = self.head_y + 1
            self.body_2_x = self.head_x + 1
            self.body_2_y = self.head_y
            self.body_3_x = self.head_x + 1
            self.body_3_y = self.head_y + 1

            if (
                (self.repr.grid[self.head_x, self.head_y] == 0)
                and (self.repr.grid[self.body_1_x, self.body_1_y] == 0)
                and (self.repr.grid[self.body_2_x, self.body_2_y] == 0)
                and (self.repr.grid[self.body_3_x, self.body_3_y] == 0)
            ):
                break

        self.pos = []
        self.pos.append((self.head_x, self.head_y))
        self.pos.append((self.body_1_x, self.body_1_y))
        self.pos.append((self.body_2_x, self.body_2_y))
        self.pos.append((self.body_3_x, self.body_3_y))

    def __update_repr(self):
        self.repr.update_grid()
