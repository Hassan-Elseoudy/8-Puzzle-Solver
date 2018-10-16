from collections import deque

queue = deque() #Queue for BFS
stack = [] #Stack for DFS

state_path = []
dir_path = []
explored = list()

def bfs(initial_state, goal_state):

    queue.append(createNode(initial_state, None, "", 0, 0))
    while len(queue):
        node = queue.popleft()
        explored.append(list(node.state))

        if node.state == goal_state:
            return node
        neighbours = expandNode(node)

        for neighbour in neighbours:
            if (neighbour not in queue) and (neighbour.state not in explored):
                queue.append(neighbour)
    return False



def dfs(initial_state, goal_state):

    stack.append(createNode(initial_state, None, "", 0, 0))
    while len(stack):
        node = stack.pop()
        explored.append(list(node.state))

        if node.state == goal_state:
            return node
        neighbours = expandNode(node)
        print(explored.__len__())

        for neighbour in neighbours:
            if (neighbour not in stack) and (neighbour.state not in explored):
                stack.append(neighbour)
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

node = dfs([1,4,2,6,5,8,7,3,0], [0, 1, 2, 3, 4, 5, 6, 7, 8])
node = Node(node.state,node.parent,node.operation,node.cost,node.depth)



def findPath(node: Node):
    dir_path.append(node.operation)
    state_path.append(node.state)
    if node.operation == "":
        return None
    else:
        return findPath(node.parent)


findPath(node)
print([i for i in dir_path[::-1] if i is not ""]) #Direction path
#State path
for i in state_path[::-1]:
    print(i,)
print(node.cost) #Path cost
print(node.depth + 1) #Path depth
print(explored.__len__())