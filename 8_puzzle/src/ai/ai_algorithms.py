from .utils import backpath


# AI Algorithms


class SearchAlgorithm:
    # definition of the search algorithm
    def search(self, init_state=None):
        return None

    # definition of f (node evaluation)
    def F(self, g=0, h=0.0):
        return 0.0


class A_star(SearchAlgorithm):
    # the chosen state is the state (never visited before) that minimizes f(n) = g(n) + h(n)
    # g(n): distance from initial state (root) to n
    # h(n): distance from n to goal state (Manhattan distance)
    # this is a possible implementation of the A* algorithm
    # return: path from init_state to victory_state
    def search(self, init_state=None):
        fringe = set([])
        visited = set([])

        fringe.add(init_state)
        while len(fringe) > 0:
            # get current node
            curr_state = min(fringe, key=lambda node: node.f)
            # remove current node from fringe
            fringe = fringe - set([curr_state])

            # curr_state.print_state()

            # check if current node is goal
            if curr_state.victory:
                return backpath(curr_state)

            # generate current node's neighbors
            curr_state_children = set(curr_state.neighbors())

            # checks on children nodes
            # all node's children are possible moves
            for child in curr_state_children:
                # if child is already in visited, continue
                if child in visited:
                    continue

                # if child is already in fringe (state generated previously)
                if child in fringe:
                    fringe_list = list(fringe)
                    # previous is the previous child's state,
                    # we want to check if now child is better
                    previous = fringe_list[fringe_list.index(child)]
                    # if previous state is better, continue
                    # else, substitute child's state
                    if previous.g <= child.g:
                        continue
                    else:
                        fringe = fringe - set([previous])
                        fringe.add(child)

                if child not in fringe:
                    fringe.add(child)

            visited.add(curr_state)

        return None

    # f = g + h
    def F(self, g=0, h=0.0):
        f = g + h
        return f
