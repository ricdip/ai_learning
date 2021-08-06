from .utils import backpath, print_state_online, get_state_from_set, get_min


class SearchAlgorithm:
    def __init__(self, heuristic=None, game=None):
        pass

    def search(self, initial_state=None):
        return None

    def F(self, g=0, h=0.0):
        return 0


class A_Star(SearchAlgorithm):
    def __init__(self, heuristic=None, game=None):
        self.heuristic = heuristic
        self.game = game

    # this is a possible implementation of the A* algorithm
    # the chosen state is the state (never visited before) that minimizes f(n) = g(n) + h(n)
    # g(n): distance from initial state (root) to n
    # h(n): distance from n to goal state (heuristic)
    #
    # return: path from init_state to victory_state
    def search(self, initial_state=None):
        fringe = set([])
        visited = set([])

        # assign scores to initial state before starting
        initial_state.g = self.heuristic.G(initial_state, None)
        initial_state.h = self.heuristic.H(initial_state)
        initial_state.f = self.F(initial_state.g, initial_state.h)

        fringe.add(initial_state)
        while len(fringe) > 0:
            # get current node
            curr_state = get_min(fringe)
            # remove current node from fringe
            fringe = fringe - set([curr_state])

            # print current state status
            print_state_online(curr_state, len(fringe), len(visited))

            # check if current node is goal
            if curr_state.is_victory():
                return backpath(curr_state)

            # generate current node's neighbors
            curr_state_children = self.game.neighbors(curr_state)

            # checks on children nodes
            # all node's children are possible moves
            for child in curr_state_children:
                # if child is already in visited, continue
                if child in visited:
                    continue

                # assign scores to child
                child.g = self.heuristic.G(child, curr_state)
                child.h = self.heuristic.H(child)
                child.f = self.F(child.g, child.h)

                # if child is already in fringe (state generated previously)
                if child in fringe:
                    # previous is the previous child's state,
                    # we want to check if now child is better
                    previous = get_state_from_set(fringe, child)
                    # if previous state is better, continue
                    # else, substitute child's state
                    # if previous.g <= child.g:
                    if previous.f <= child.f:
                        continue
                    else:
                        fringe = fringe - set([previous])
                        fringe.add(child)

                if child not in fringe:
                    fringe.add(child)

            visited.add(curr_state)

        return None

    # f valuation logic
    # f(n) = g(n) + h(n)
    def F(self, g=0, h=0.0):
        f = g + h
        return f
