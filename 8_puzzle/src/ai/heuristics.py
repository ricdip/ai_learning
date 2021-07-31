class Heuristic:
    def H(self, currState):
        return 1


# h(n): an heuristic function for 8-puzzle
# number of misplaced tiles (simple but not the best heuristic, Manhattan distance is better)
class MisplacedTiles(Heuristic):
    def H(self, currState):
        diff = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if (
                    currState.repr.grid[i][j] != currState.repr.victory_grid[i][j]
                    and currState.repr.grid[i][j] != "*"
                ):
                    diff += 1
        return diff
