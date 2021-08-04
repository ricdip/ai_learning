# return the reverse path from node to the initial node
def backpath(node):
    states = [node]
    parent = node.parent
    while parent != None:
        states += [parent]
        parent = parent.parent
    return reversed(states)


def print_state_online(state, fringe_len, explored_len):
    print(
        " fringe_len: {}, explored_len: {}, g(n): {}, h(n): {}, f(n): {}".format(
            fringe_len, explored_len, state.g, state.h, state.f
        ),
        end="\r",
    )


def get_state_from_set(set_of_states, state):
    for node in set_of_states:
        if node == state:
            return node
    return None
