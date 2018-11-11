check = []
nos = ((0, 1), (0, 2), (1, 0), (2, 0), (1, 1))

# State tree class
class tree:
    global check

    #Class initialization
    def __init__(self, m=None, c=None, parent = None):

        self.kids = []
        if parent is None:
            self.m = 3
            self.c = 3
            self.parent = None
            self.river = 0
        else:
            self.m = m
            self.c = c
            self.parent = parent
            self.river = 1 - parent.river

    #Function to print nos of Missionaries, Cannibals and Boat side...in short, function to print the state
    def __str__(self):
        return "{}{}{}".format(self.m, self.c, self.river)

    #Function to add children nodes in tree
    def addkids(self, obj):
        self.kids.append(obj)

    #Function to check if problem achieved final solution or not
    def is_final(self):
        if self.m is 0 and self.c is 0:
            return 1
        else:
            return 0

    #Function to check if the state is valid or not. For eg: if no of Missionaries is less than no of Cannibals, the state is invalid
    def decide(self, m, c):
        if (m >= 0 and 3 - m >= 0) and (c >= 0 and 3 - c >= 0) and (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c):
            return 1
        else:
            return 0

    # def draw(self):
    #     return "{}{}{}".format(self.m, self.c, self.river)

#Function to add valid child in a node and append them in a list kids
def producekids(state):
    kids = []
    for j, k in nos:
        if state.river is 1:
            if j > 3 - state.m or k > 3 - state.c:
                continue
        else:
            if j > state.m or k > state.c:
                continue

        m = state.m - (-1) ** state.river * j
        c = state.c - (-1) ** state.river * k

        kid = tree(m, c, state)
        if kid.decide(m, c) is 1:
            kid.parent = state
            state.kids.append(kid)
            kids.append(kid)
    return kids

#Function which implements Breadth First Search and keeping track of parent node, and returns final state i.e. 0 0 1
def bfs():
    start = tree()
    if start.is_final():
        return start
    current = []
    container = set()
    current.append(start)
    while current:
        state = current.pop(0)
        if state.is_final():
            return state
        container.add(state)
        children = producekids(state)
        for child in children:
            if (child not in container) or (child not in current):
                current.append(child)
    return None

#Implements function bfs() to create a hierarchical string using 3 symbols: (),
def printx(solution):
    final = "("
    a = ""
    path = []
    path.append(solution)
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent
    for t in range(len(path)):
        state = path[len(path) - t - 1]
        state1 = path[len(path) - t - 2]
        if t is len(path) -1:
            final = final + "001))))))))))))"
            break
        final = final + str(state) + "("
        for i in state.kids:
            if i is state1:
                break
            else:
                final = final+str(i)+","

    return final

#Final function which prints the hierarchical string generated by function printx() in terminal representing a tree to some extend
def finalprint(string):
    j = 1
    print("<<< 'M means number of missionaries on the initial bank of river' >>>")
    print("<<< 'C means number of missionaries on the initial bank of river' >>>")
    print("<<< 'B means position of boat'                                    >>>")
    print("<<< 'If B = 0, then boat is in initial/starting bank'             >>>")
    print("<<< 'If B = 1, then boat is in final/target bank'                 >>>")
    print(" M C B", end = "")
    for i in string:
        if i is '(':
            print("")
            print(j*" "+"|")
            print(j*" "+"|")
            print(j*" ", end = "")
            j += 1
        elif i is ",":
            print(", ", end = " ")
            j += 2
        elif i is ")":
            break
        else:
            print(i, end = " ")
            j += 1
    print("====> Final State (^_^)")

#Implementation
ggwp = bfs()
finalprint(printx(ggwp))
