from collections import deque
from queue import PriorityQueue
from typing import Union
import timeit
from tkinter import *




start = timeit.default_timer()


queue = deque()  # Queue for BFS
stack = deque()  # Stack for DFS
heapqu = PriorityQueue()  # Priority queue for A*

state_path = []
dir_path = []
explored = list()
basicwindow = Tk()
lable = Label(basicwindow, text = "8 P U Z Z L E " , bg='blue')
lable.pack(fill = X)
label1 = Label(basicwindow, text='Choose The Solving Algorithim',bg='green')
label1.pack(fill = X)
#label1.pack()

def bfs(initial_state, goal_state):
    queue.append(createNode(initial_state, "bfs", None, "", 0, 0))
    while len(queue):
        current_node: Node = queue.popleft()
        explored.append(list(current_node.state))

        if current_node.state == goal_state:
            return current_node
        neighbours = expandNode(current_node)

        for neighbour in neighbours:
            if (neighbour not in queue) and (neighbour.state not in explored):
                queue.append(neighbour)
    return False


def dfs(initial_state, goal_state):
    stack.append(createNode(initial_state, "dfs", None, "", 0, 0))
    while len(stack):
        current_node: Node = stack.pop()
        explored.append(current_node.state)

        if current_node.state == goal_state:
            return current_node
        neighbours = expandNode(current_node)

        for neighbour in neighbours:
            if (neighbour not in stack) and (neighbour.state not in explored):
                stack.append(neighbour)
    return False


def createNode(state, algo, parent, operation, cost, depth):
    return Node(state, str(algo), parent, operation, cost, depth)


def expandNode(node):
    children = list()
    children.append(createNode(down(node.state), node.algorithm, node, "DOWN", node.cost + 1, node.depth + 1))
    children.append(createNode(right(node.state), node.algorithm, node, "RIGHT", node.cost + 1, node.depth + 1))
    children.append(createNode(left(node.state), node.algorithm, node, "LEFT", node.cost + 1, node.depth + 1))
    children.append(createNode(up(node.state), node.algorithm, node, "UP", node.cost + 1, node.depth + 1))
    return [child for child in children if child.state is not None]


def Asearch(initial_state, goal_state):
    heapqu.put(createNode(initial_state, "ast", None, "", 0, 0))
    while not heapqu.empty():

        temp = list()
        temp.clear()
        node: Node = heapqu.get()
        explored.append(node.state)

        if node.state == goal_state:
            return node

        neighbours = expandNode(node)

        while not heapqu.empty():
            temp.append(heapqu.get())

        for neighbour in neighbours:
            if (neighbour not in temp) and (neighbour.state not in explored):
                heapqu.put(neighbour)
            elif neighbour in temp:  # agebo mn l temp w a3dl fel cost bta3to
                current_nodeIndex: int = temp.index(neighbour)
                current_node = temp[current_nodeIndex]
                temp.remove(current_node)
                current_node.cost = int(manhatn(current_node.state)) + neighbour.depth
         #       print(current_node.cost)
                temp.append(current_node)

        for i in range(len(temp)):
            heapqu.put(temp[i])

        #print(heapqu.qsize())

    return False


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


def manhatn(state):
    manhatn_cost : int = 0
    state = list(state)
    for i in range(9):
        manhatn_cost += abs(state[i] / 3 - (i % 3)) + abs(state[i] % 3 - (i / 3))
    return manhatn_cost


class Node:
    def __init__(self, state, algorithm, parent, operation, depth, cost):
        self.state = state
        self.algorithm = algorithm
        self.parent = parent
        self.operation = operation
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        if str(self.algorithm) == "ast":
            return self.cost < other.cost
        else:
            pass

    def __eq__(self, other):
        if str(self.algorithm) == "ast":
            return self.cost == other.cost
        else:
            pass

    def __contains__(self, item):
        if str(self.algorithm) == "ast":
            return self.state == item.state
        else:
            pass

def split_list(a_list):
    third = len(a_list)//3
    return a_list[:third], a_list[third:] , a_list[:third:]

#intial=[3, 1, 2, 6, 4, 5, 7, 8, 0]
#goal=[0, 1, 2, 3, 4, 5, 6, 7, 8]

node: Union[Node, bool] = Asearch([3, 1, 2, 6, 4, 5, 7, 8, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8])
node = Node(node.state, node.algorithm, node.parent, node.operation, node.cost, node.depth)

def split_list(alist):
    length = len(alist)
    return [ alist[i*length // 3: (i+1)*length // 3]
             for i in range(3) ]

def findPath(node: Node):
    dir_path.append(node.operation)
    state_path.append(node.state)
    if node.depth == 0:
        return None
    else:
        return findPath(node.parent)
#label1 = Label(basicwindow, text = 'test')
#label1.grid(row=0)
#label1.pack()
#canvas = Canvas (basicwindow)
#canvas.pack()
#blackline = canvas.create_line(0,9,100,50)
#button1 = Button(basicwindow,text = 'A* Search',command =Asearch)
#button1.pack()
#button2 = Button(basicwindow,text = 'DFS Search',command =dfs)
#button2.pack()
#button3 = Button(basicwindow,text = 'BFS Search',command =bfs)
#button3.pack()
fw = open("output.txt" , "w")
findPath(node)
# State path
stop = timeit.default_timer()
basicwindow.mainloop()
for i in state_path[::-1]:
    a,b,c= split_list(i)
    print(a)
    print(b)
    print(c,'\n','\n')
fw.write("path_to_goal:")  # Direction path
fw.write(str([i for i in dir_path[::-1] if i is not '']))
fw.write("\ncost_of_path:")  # Path cost
fw.write(str(node.cost))
fw.write("\nnodes_expanded:")#nodes explored
fw.write(str(explored.__len__()))
fw.write("\nsearch_depth:")  # Path depth
fw.write(str(node.depth + 1))
fw.write("\nrunning_time:")
fw.write(str(stop - start))
fw.close()
print([i for i in dir_path[::-1] if i is not ''])  # Direction path
print(node.cost)  # Path cost
print(explored.__len__()) #nodes explored
print(node.depth + 1)  # Path depth
