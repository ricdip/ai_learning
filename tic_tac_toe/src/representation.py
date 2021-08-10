from copy import deepcopy


class TicTacToeRepresentation:
    def __init__(self, grid=None):
        if grid is None:
            self.grid = []
            self.draw_grid()
        else:
            self.grid = grid

    def draw_grid(self):
        for i in range(0, 3):
            self.grid.append([])
            for j in range(0, 3):
                self.grid[i].append(".")

    def print_grid(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print(" {} ".format(self.grid[i][j]), end="")
            print()

    def move(self, coord, turn):
        if turn != "X" and turn != "O":
            raise ValueError("turn = [X, O]")

        x = coord[0]
        y = coord[1]

        if self.grid[x][y] == ".":
            grid = deepcopy(self.grid)
            grid[x][y] = turn

            return TicTacToeRepresentation(grid=grid)
        return None

    def game_over(self):
        if self.victory() is not None:
            return True

        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[i][j] == ".":
                    return False

        return True

    def victory(self):
        if (
            self.grid[0][0] == self.grid[0][1]
            and self.grid[0][1] == self.grid[0][2]
            and self.grid[0][2] != "."
        ):
            return self.grid[0][0]

        if (
            self.grid[1][0] == self.grid[1][1]
            and self.grid[1][1] == self.grid[1][2]
            and self.grid[1][2] != "."
        ):
            return self.grid[1][0]

        if (
            self.grid[2][0] == self.grid[2][1]
            and self.grid[2][1] == self.grid[2][2]
            and self.grid[2][2] != "."
        ):
            return self.grid[2][0]

        if (
            self.grid[0][0] == self.grid[1][0]
            and self.grid[1][0] == self.grid[2][0]
            and self.grid[2][0] != "."
        ):
            return self.grid[0][0]

        if (
            self.grid[0][1] == self.grid[1][1]
            and self.grid[1][1] == self.grid[2][1]
            and self.grid[2][1] != "."
        ):
            return self.grid[0][1]

        if (
            self.grid[0][2] == self.grid[1][2]
            and self.grid[1][2] == self.grid[2][2]
            and self.grid[2][2] != "."
        ):
            return self.grid[0][2]

        if (
            self.grid[0][0] == self.grid[1][1]
            and self.grid[1][1] == self.grid[2][2]
            and self.grid[2][2] != "."
        ):
            return self.grid[0][0]

        if (
            self.grid[0][2] == self.grid[1][1]
            and self.grid[1][1] == self.grid[2][0]
            and self.grid[2][0] != "."
        ):
            return self.grid[0][2]

        return None
