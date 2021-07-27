# h(n): an heuristic function for 8-puzzle
# number of misplaced tiles (simple but not the best heuristic, Manhattan distance is better)
def heuristic(currState):
    diff = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if currState.repr.grid[i][j] != currState.repr.victory_grid[i][j] and currState.repr.grid[i][j] != '*':
                diff += 1
    return diff


# A* algorithm possible implementation
# the chosen state is the state (never visited before) that minimizes f(n) = g(n) + h(n)
# g(n): distance from initial state (root)
# h(n): distance from goal state (number of misplaced tiles)
#
# return: path from initial state to victory state
def search(init_state=None):
    curr_state = init_state
    fringe = []
    visited = []
    fringe.append(curr_state)

    while True:
        curr_state = fringe[0]

        if curr_state.victory:
            return backpath(curr_state)

        for child in curr_state.neighbors():
            if child not in visited:
                fringe.append(child)

        visited.append(curr_state)
        del fringe[0]

        fringe.sort(key = lambda x:x.f, reverse=False)


# return the reverse path from node to the initial node
def backpath(node):
    states = [node]
    parent = node.parent
    while parent != None:
        states += [parent]
        parent = parent.parent
    return reversed(states)
