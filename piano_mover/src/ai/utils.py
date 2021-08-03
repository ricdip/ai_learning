# return the reverse path from node to the initial node
def backpath(node):
    states = [node]
    parent = node.parent
    while parent != None:
        states += [parent]
        parent = parent.parent
    return reversed(states)
