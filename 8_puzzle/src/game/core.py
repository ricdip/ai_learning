import random
from .display import Display
import time

class Game:
    def __init__(self):
        self.grid = _Grid()
        self.display = Display()

    def start(self):
        self.__game_loop()

    def __game_loop(self):
        while True:
            self.display.redraw(self.grid.grid)
            # TODO: for now we redraw the screen every 1 second, but we will redraw the screen every move
            time.sleep(1)


class _Grid:
    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.__init_grid()
        self.__shuffle_grid()

    
    def __shuffle_grid(self):
        for row in self.grid:
            random.shuffle(row)
        random.shuffle(self.grid)

    def __init_grid(self):
        self.grid = []
        i = 1
        for x in range(0, self.rows):
            self.grid.append([])
            for y in range(0, self.cols):
                if (x == self.rows - 1) and (y == self.cols - 1):
                    self.grid[x].append('*')
                else:
                    self.grid[x].append(i)
                    i = i + 1
