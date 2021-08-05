import math


class Heuristic:
    def H(self, state):
        return 1


# Manhattan distance heuristic
class ManhattanDistance(Heuristic):
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


# we try to consider only the heads positions
class ManhattanDistanceVariant(Heuristic):
    def H(self, state):
        piano_head_x = state.representation.blocks["piano"].head_x
        piano_head_y = state.representation.blocks["piano"].head_y
        exit_head_x = state.representation.blocks["exit"].head_x
        exit_head_y = state.representation.blocks["exit"].head_y

        return math.fabs(piano_head_x - exit_head_x) + math.fabs(
            piano_head_y - exit_head_y
        )
