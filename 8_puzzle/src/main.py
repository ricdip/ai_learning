from ai import A_star, MisplacedTiles
from game import State


def main():
    search = A_star()
    heuristic = MisplacedTiles().H

    initial_state = State(heuristic=heuristic, f_valuation=search.F)

    print("Initial state:")
    print()
    initial_state.print_state()

    # use A* to find the solution path
    path = search.search(initial_state)

    print("Solution path:")
    print()
    for node in path:
        node.print_state()

    print("Victory state reached")


if __name__ == "__main__":
    main()
