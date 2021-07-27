from .state import State
from .ai import heuristic, search


def run():
    state0 = State()
    curr = state0

    print("Initial state:")
    print()
    curr.print_state()

    # use A* to find the solution path
    path = search(curr)

    print("Solution path:")
    print()
    for node in path:
        node.print_state()

    print("Victory state reached")
