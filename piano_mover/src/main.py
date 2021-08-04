import piano_mover

# heuristics import
from ai import ManhattanDistance

# search algorithms import
from ai import A_Star


def main():
    heuristic = ManhattanDistance
    search_algorithm = A_Star

    piano_mover.run(heuristic=heuristic, search_algorithm=search_algorithm)


if __name__ == "__main__":
    main()
