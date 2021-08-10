from heuristics import Heuristic
from game import TicTacToeGame
from state import TicTacToeState
import sys

h = Heuristic()
g = TicTacToeGame()
# max depth of minmax tree
depth = 5

# AI? (if not AI -> human)
AI = True

# Use alpha-beta pruning?
alpha_beta = True


def main():
    if AI:
        print("tic tac toe: AI vs. AI")
    else:
        print("tic tac toe: AI vs. human")
    print()
    state_0 = TicTacToeState()

    curr_state = state_0
    while True:
        # ai turn (X)
        print("X turn")
        curr_state = best_move_max_player(curr_state)
        curr_state.print_state()
        print()

        check_win(curr_state)

        print("O turn")
        if not AI:
            # our move (O)[human]
            x = int(input("x: "))
            y = int(input("y: "))
            curr_state = TicTacToeState(curr_state.representation.move((x, y), "O"))
        else:
            # ai turn (O)
            curr_state = best_move_min_player(curr_state)

        curr_state.print_state()
        print()

        check_win(curr_state)


def check_win(state):
    if state.game_over():
        win_player = state.victory()
        if win_player is None:
            print("draw")
        else:
            print("{} won".format(win_player))
        sys.exit(0)


# maximizer player is X
def best_move_max_player(state):
    best_val = float("-inf")
    best_move = None
    for move in g.neighbors(state, "X"):
        # TODO: is it ok to put O instead of X
        if alpha_beta:
            value = h.H2(move, depth, float("-inf"), float("inf"), "O")
        else:
            value = h.H1(move, depth, "O")
        if value > best_val:
            best_val = value
            best_move = move
    return best_move


# minimizer player is O
def best_move_min_player(state):
    best_val = float("inf")
    best_move = None
    for move in g.neighbors(state, "O"):
        if alpha_beta:
            value = h.H2(move, depth, float("-inf"), float("inf"), "X")
        else:
            value = h.H1(move, depth, "X")
        if value < best_val:
            best_val = value
            best_move = move
    return best_move


if __name__ == "__main__":
    main()
