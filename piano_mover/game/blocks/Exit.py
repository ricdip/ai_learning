import random

#  exit
class Exit:
    def __init__(self, representation=None, piano_block=None):
        self.repr = representation
        self.pos = []
        self.value = 0
        self.piano_block = piano_block
        self.head_x = None
        self.head_y = None
        self.body_1_x = None
        self.body_1_y = None
        self.body_2_x = None
        self.body_2_y = None
        self.body_3_x = None
        self.body_3_y = None

        self.__generate_positions()

    def __generate_positions(self):
        # H*
        # **
        self.head_x = self.repr.get_grid_shape()[0] - self.piano_block.head_x - 2
        self.head_y = self.repr.get_grid_shape()[1] - self.piano_block.head_y - 2

        self.body_1_x = self.head_x
        self.body_1_y = self.head_y + 1
        self.body_2_x = self.head_x + 1
        self.body_2_y = self.head_y
        self.body_3_x = self.head_x + 1
        self.body_3_y = self.head_y + 1

        self.pos = []
        self.pos.append((self.head_x, self.head_y))
        self.pos.append((self.body_1_x, self.body_1_y))
        self.pos.append((self.body_2_x, self.body_2_y))
        self.pos.append((self.body_3_x, self.body_3_y))
