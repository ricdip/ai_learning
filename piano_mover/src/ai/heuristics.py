import math


class Heuristic:
    def H(self, state):
        return 1

    def G(self, curr_state=None, parent_state=None):
        return 1


# Manhattan distance heuristic
class ManhattanDistance(Heuristic):
    # estimated cost from current state to goal state
    def H(self, state):
        piano_pos = state.representation.blocks["piano"].pos
        exit_pos = state.representation.blocks["exit"].pos

        distance = 0.0
        positions = zip(piano_pos, exit_pos)

        for pos in list(positions):
            piano_coord = pos[0]
            exit_coord = pos[1]
            distance += math.fabs(piano_coord[0] - exit_coord[0]) + math.fabs(
                piano_coord[1] - exit_coord[1]
            )

        return distance

    # cost for a single move
    def G(self, curr_state=None, parent_state=None):
        # if curr_state is initial state
        if parent_state is None:
            return 0

        if curr_state.representation.moved_block == "piano":
            # if we moved the piano, cost of move is 1
            # return parent_state.g + 1
            return parent_state.g + 4
        else:
            # if we moved the obstacles, cost of move is 2
            # return parent_state.g + 2
            return parent_state.g + 6


# we try to consider only the heads positions
# class ManhattanDistanceVariant(Heuristic):
#    def H(self, state):
#        piano_head_x = state.representation.blocks["piano"].head_x
#        piano_head_y = state.representation.blocks["piano"].head_y
#        exit_head_x = state.representation.blocks["exit"].head_x
#        exit_head_y = state.representation.blocks["exit"].head_y
#
#        return math.fabs(piano_head_x - exit_head_x) + math.fabs(
#            piano_head_y - exit_head_y
#        )
