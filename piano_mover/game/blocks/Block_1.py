import random

# 1 obstacles
class Block_1:
    def __init__(self, representation=None):
        self.repr = representation
        self.pos = []
        self.value = 1

        self.__generate_positions()

    def move_up(self):
        pass

    def __generate_positions(self):
        while True:
            head_x = random.randint(0, self.repr.get_grid_shape()[0] - 1)
            head_y = random.randint(0, self.repr.get_grid_shape()[1] - 1)

            if self.repr.grid[head_x, head_y] == 0:
                self.pos = []
                self.pos.append((head_x, head_y))
                break

    def __update_repr(self):
        self.repr.update_grid()
