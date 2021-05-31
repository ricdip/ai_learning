import random
from .display import Display
from .ai import AI
import copy
import time

# game
class Game:
    def __init__(self, random_grid=False, watch_moves=False):
        self.grid = _Grid(grid=None, random_grid=random_grid)
        self.display = Display()
        self.ai = AI()
        self.watch_moves = watch_moves

    def start(self):
        self.__game_loop()

    def __game_loop(self):
        # victory state
        goal_state = [[1,2,3], [4,5,6], [7,8,'*']]
        # initial state
        initial_state = GameState(parent=None, representation=self.grid, level=0, fval=0)

        # draw initial state
        self.display.draw_state(initial_state, 0)

        # calculate solution
        solutionPath, iterations = self.ai.search(initial_state, goal_state)
        self.display.print_success()

        # list solution and some infos
        moves = 0
        for node in solutionPath:
            if self.watch_moves:
                time.sleep(1)
            self.display.draw_state(node, moves)
            moves += 1

        self.display.print_infos({'Total iterations': iterations, 'Total moves': moves})


# single game state
class GameState:
    def __init__(self, parent=None, representation=None, level=0, fval=0):
        self.parent = parent
        self.representation = representation
        self.level = level
        self.fval = fval

    def __eq__(self, other):
        if not isinstance(other, GameState):
            return False
        return self.representation.__eq__(other.representation)

    def __ne__(self, other):
        return not self.__eq__(other)

    def generate_children(self):
        children = []
        # simulate valid moves (if valid -> grid with move's result, else None)
        move_results = [self.representation.move_up_sim(), self.representation.move_down_sim(), self.representation.move_left_sim(), self.representation.move_right_sim()]
        for move in move_results:
            if move is not None:
                # create a child node for each valid move
                children.append(GameState(parent=self, representation=_Grid(grid=move), level=self.level+1, fval=0))
        return children


# 8-puzzle representation
class _Grid:
    def __init__(self, grid=None, random_grid=False):
        self.rows = 3
        self.cols = 3
        if grid is not None:
            self.grid = grid
        else:
            self.grid = []
            if random_grid:
                self.__init_grid()
                self.__shuffle_grid()
            else:
                self.__init_grid_fixed()

    def __eq__(self, other):
        if not isinstance(other, _Grid):
            return False
        return self.grid == other.grid

    def __ne__(self, other):
        return not self.__eq__(other)


    # moves simulations
    def move_up_sim(self):
        x,y = self.__find_blank()
        grid = copy.deepcopy(self.grid)
        if x-1 >= 0:
            tmp = grid[x-1][y]
            grid[x-1][y] = grid[x][y]
            grid[x][y] = tmp

            return grid
        return None

    def move_down_sim(self):
        x,y = self.__find_blank()
        grid = copy.deepcopy(self.grid)
        if x+1 < len(grid):
            tmp = grid[x+1][y]
            grid[x+1][y] = grid[x][y]
            grid[x][y] = tmp

            return grid
        return None

    def move_left_sim(self):
        x,y = self.__find_blank()
        grid = copy.deepcopy(self.grid)
        if y-1 >= 0:
            tmp = grid[x][y-1]
            grid[x][y-1] = grid[x][y]
            grid[x][y] = tmp

            return grid
        return None

    def move_right_sim(self):
        x,y = self.__find_blank()
        grid = copy.deepcopy(self.grid)
        if y+1 < len(grid[x]):
            tmp = grid[x][y+1]
            grid[x][y+1] = grid[x][y]
            grid[x][y] = tmp

            return grid
        return None

    def __find_blank(self):
        for x in range(0, self.rows):
            for y in range(0, self.cols):
                if self.grid[x][y] == '*':
                    return (x, y)
    
    def __shuffle_grid(self):
        for row in self.grid:
            random.shuffle(row)
        random.shuffle(self.grid)
        while not self.__solvable(self.grid):
            for row in self.grid:
                random.shuffle(row)
            random.shuffle(self.grid)

    def __solvable(self, grid):
        linear_grid = grid[0] + grid[1] + grid[2]
        linear_grid.remove('*')
        if grid == None:
            return False
        invertions = 0
        for i in range(0, len(linear_grid)):
            for j in range(i+1, len(linear_grid)):
                if linear_grid[j] > linear_grid[i]:
                    invertions += 1

        return (invertions % 2) == 0

    def __init_grid_fixed(self):
        self.grid = [[8, '*', 6], [5, 4, 7], [2, 3, 1]]

    def __init_grid(self):
        i = 1
        for x in range(0, self.rows):
            self.grid.append([])
            for y in range(0, self.cols):
                if (x == self.rows - 1) and (y == self.cols - 1):
                    self.grid[x].append('*')
                else:
                    self.grid[x].append(i)
                    i = i + 1
