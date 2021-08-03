from game import PianoMoverState
from ai import ManhattanDistance, A_star
import sys


def main():
    heuristic = ManhattanDistance()
    search = A_star(heuristic)

    initial_state = PianoMoverState()

    print("Initial state grid:")
    initial_state.representation.print_grid()

    path = search.search(initial_state)

    if path is None:
        print("A* could not find the victory path.")
        sys.exit(1)

    print()
    print("Path from initial state:")
    for node in path:
        node.print_state()
        print("---------------------------------------")
        print()

    print("Victory state reached")


if __name__ == "__main__":
    main()
