from game import PianoMoverState
from ai import ManhattanDistance, A_Star
import sys


def run(heuristic=None, search_algorithm=None):
    if heuristic is None:
        heuristic = ManhattanDistance

    # instantiate heuristic
    heuristic = heuristic()
    heuristic_name = type(heuristic).__name__

    if search_algorithm is None:
        search_algorithm = A_star

    # instantiate search algorithm
    search_algorithm = search_algorithm(heuristic=heuristic)
    search_algorithm_name = type(search_algorithm).__name__

    print()
    print("Chosen heuristic: {}".format(heuristic_name))
    print()
    print("Chosen search algorithm: {}".format(search_algorithm_name))
    print()

    # create initial state
    initial_state = PianoMoverState()

    print("Initial state grid:")
    initial_state.representation.print_grid()
    print()
    print("Realtime progress status:")

    # solve the problem using the search algorithm
    path = search_algorithm.search(initial_state)

    if path is None:
        print("{} could not find the victory path.".format(search_algorithm_name))
        sys.exit(1)

    print()
    print()
    print("Solution found")
    print()
    print("Path from initial state:")
    for node in path:
        node.print_state()
        print("---------------------------------------")
        print()

    print("Victory state reached")
