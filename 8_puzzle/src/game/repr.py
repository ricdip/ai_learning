from copy import deepcopy


# 8-puzzle representation
class Repr:
    def __init__(self, grid=None):
        if grid is not None:
            self.grid = grid
        else:
            # this instance is unsolvable
            #self.grid = [[8, '*', 6],
            #              [5, 4, 7],
            #              [2, 3, 1]]
            # this instance is solvable
            #self.grid = [[1, 2, 3],
            #              ['*', 4, 6],
            #              [7, 5, 8]]
            self.grid = [[1, 8, 2],
                          ['*', 4, 3],
                          [7, 6, 5]]

        self.victory_grid = [[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, '*']]
    
    def __eq__(self, other):
        if not isinstance(other, Repr):
            return False
        return self.grid == other.grid

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.grid))

    def find_blank(self):
        for x in range(0, 3):
            for y in range(0, 3):
                if self.grid[x][y] == '*':
                    return (x, y)
            
    def move_up(self):
        x, y = self.find_blank()
        grid = deepcopy(self.grid)
        if x - 1 >= 0:
            tmp = grid[x-1][y]
            grid[x-1][y] = grid[x][y]
            grid[x][y] = tmp
            return grid
        return None

    def move_down(self):
        x, y = self.find_blank()
        grid = deepcopy(self.grid)
        if x + 1 < len(grid):
            tmp = grid[x+1][y]
            grid[x+1][y] = grid[x][y]
            grid[x][y] = tmp
            return grid
        return None

    def move_left(self):
        x, y = self.find_blank()
        grid = deepcopy(self.grid)
        if y - 1 >= 0:
            tmp = grid[x][y-1]
            grid[x][y-1] = grid[x][y]
            grid[x][y] = tmp
            return grid
        return None

    def move_right(self):
        x, y = self.find_blank()
        grid = deepcopy(self.grid)
        if y + 1 < len(grid[x]):
            tmp = grid[x][y+1]
            grid[x][y+1] = grid[x][y]
            grid[x][y] = tmp
            return grid
        return None

    def is_victory(self):
        for x in range(0, 3):
            for y in range(0, 3):
                if self.grid[x][y] != self.victory_grid[x][y]:
                    return False
        return True

    def print_grid(self):
        for x in range(0, 3):
            for y in range(0, 3):
                print(" {} ".format(self.grid[x][y]), end='')
            print()
