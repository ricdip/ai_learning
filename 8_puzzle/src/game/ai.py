from .display import Display

class AI:
    def __init__(self):
        self.display = Display()

    # A* algorithm possible implementation
    # TODO: is this correct ?
    def search(self, initial_state, goal_state):
        fringe = set([])
        explored = set([])
        initial_state.fval = self.f(initial_state, goal_state)
        fringe.add(initial_state)

        iterations = 0
        cur_state = initial_state
        while len(fringe) > 0:
            iterations += 1
            
            self.display.print_status(iterations)

            cur_state = min(fringe, key=lambda x:x.fval)
            
            if self.h(cur_state, goal_state) == 0:
                break

            neighbors = set([])
            for child in cur_state.generate_children():
                child.fval = self.f(child, goal_state)
                neighbors.add(child)

            explored.add(cur_state)
            fringe = (fringe | neighbors) - explored

        return self.backpath(cur_state),iterations

    # f(x)
    def f(self, start, goal):
        g_x = start.level
        h_x = self.h(start, goal)
        ## TODO: why with g(x) + h(x) we don't terminate ?
        #f_x = g_x + h_x
        f_x = h_x
        return f_x
    
    # h(x): heuristic function -> for 8 puzzle, the number of misplaced tiles
    def h(self, start, goal):
        difference = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if start.representation.grid[i][j] != goal[i][j] and start.representation.grid[i][j] != '*':
                    difference += 1
        return difference

    # return the reverse path from a node to the root node
    def backpath(self, node):
        states = [node]
        parent = node.parent
        while parent != None:
            states += [parent]
            parent = parent.parent
        return reversed(states)
