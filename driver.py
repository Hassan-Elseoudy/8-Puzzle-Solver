from collections import deque


def bfs(initial_state, goal_state):
    frontier = deque()
    frontier.append(createNode(initial_state, None, "",0, 0))
    explored = set()
    while len(frontier):
        node = frontier.popleft()
        explored.add(node)
        print(node.state)

        if node.state == goal_state:
            return node
        neighbours = expandNode(node)

        for neighbour in neighbours:
            if (neighbour not in frontier) and (neighbour not in explored):
                frontier.append(neighbour)
    return False


def createNode(state, parent, operation, cost, depth):
    return Node(state, parent, operation, cost, depth)


def expandNode(node):
    children = list()
    children.append(createNode(up(node.state), node, "UP", node.cost + 1, node.depth + 1))
    children.append(createNode(down(node.state), node, "DOWN", node.cost + 1, node.depth + 1))
    children.append(createNode(right(node.state), node, "RIGHT", node.cost + 1, node.depth + 1))
    children.append(createNode(left(node.state), node, "LEFT", node.cost + 1, node.depth + 1))
    return [child for child in children if child.state is not None]


def down(state):
    state = list(state)
    index = state.index(0)
    if index + 3 <= 8:
        state[index], state[index + 3] = state[index + 3], state[index]
        return state
    else:
        return None


def up(state):
    state = list(state)
    index = state.index(0)
    if index - 3 >= 0:
        state[index], state[index - 3] = state[index - 3], state[index]
        return state
    else:
        return None


def right(state):
    state = list(state)
    index = state.index(0)
    if (index + 1) % 3 != 0:
        state[index], state[index + 1] = state[index + 1], state[index]
        return state
    else:
        return None


def left(state):
    state = list(state)
    index = state.index(0)
    if (index - 1) % 3 != 2:
        state[index], state[index - 1] = state[index - 1], state[index]
        return state
    else:
        return None


class Node:
    def __init__(self, state, parent, operation, depth, cost):
        self.state = state
        self.parent = parent
        self.operation = operation
        self.depth = depth
        self.cost = cost

node = bfs([1, 2, 3, 4, 5, 6, 7, 8, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8])
node = Node(node.state,node.parent,node.operation,node.cost,node.depth)

path = []
def findEveryThing(node: Node):
    path.append(node.operation)
    if node.operation == "":
        return None
    else:
        return findEveryThing(node.parent)


findEveryThing(node)
print([i for i in path[::-1] if i is not ""])