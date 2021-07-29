try:
   import Queue
except ImportError:
   import queue as Queue

### Part 1: define search state
class unblockMeState:
    def __init__(self, numberList):
        self.bricks = []
        self.bricks = numberList[:]
        self.fill = []
        self.fill = [0]*36
        for index in range(36):
            if (self.bricks[index] == 1):
                self.currentLocation = index
                self.fill[index] = 1
                self.fill[index+1] = 1
            elif (self.bricks[index] == 2):
                self.fill[index] = 1
                self.fill[index+1] = 1
            elif (self.bricks[index] == 3):
                self.fill[index] = 1
                self.fill[index+1] = 1
                self.fill[index+2] = 1
            elif (self.bricks[index] == -2):
                self.fill[index] = 1
                self.fill[index+6] = 1
            elif (self.bricks[index] == -3):
                self.fill[index] = 1
                self.fill[index+6] = 1
                self.fill[index+12] = 1
    
    def goalState(self):
        if (self.bricks[16] == 1):
        # if (self.currentLocation == 16):  #both lines are OK.
            return True
        else:
            return False

    def nextActions(self):
        actions = []
        for index in range(36):
            if (self.bricks[index] == 1):
                if (index%6<4) and (self.fill[index+2]==0):
                    actions.append((index, 'right'))
                if (index%6!=0) and (self.fill[index-1]==0):
                    actions.append((index, 'left'))
            if (self.bricks[index] == 2):
                if (index%6<4) and (self.fill[index+2]==0):
                    actions.append((index, 'right'))
                if (index%6!=0) and (self.fill[index-1]==0):
                    actions.append((index, 'left'))
            elif (self.bricks[index] == 3):
                if (index%6<3) and (self.fill[index+3]==0):
                    actions.append((index, 'right'))
                if (index%6!=0) and (self.fill[index-1]==0):
                    actions.append((index, 'left'))
            elif (self.bricks[index] == -2):
                if (index>5) and (self.fill[index-6]==0):
                    actions.append((index, 'up'))
                if (index<24) and (self.fill[index+12]==0):
                    actions.append((index, 'down'))
            elif (self.bricks[index] == -3):
                if (index>5) and (self.fill[index-6]==0):
                    actions.append((index, 'up'))
                if (index<18) and (self.fill[index+18]==0):
                    actions.append((index, 'down'))
        return actions

    def nextState(self, action):
        newState = unblockMeState([0]*36)
        newState.bricks = self.bricks[:]
        newState.fill = self.fill[:]
        newState.currentLocation = self.currentLocation
        index=action[0]
        if action[1] == 'up':
            if self.bricks[index] == -2:
                newState.bricks[index-6] = self.bricks[index]
                newState.bricks[index] = 0
                newState.fill[index-6] = 1
                newState.fill[index+6] = 0
            elif self.bricks[index] == -3:
                newState.bricks[index-6] = self.bricks[index]
                newState.bricks[index] = 0
                newState.fill[index-6] = 1
                newState.fill[index+12] = 0
        if action[1] == 'down':
            if self.bricks[index] == -2:
                newState.bricks[index+6] = self.bricks[index]
                newState.bricks[index] = 0
                newState.fill[index+12] = 1
                newState.fill[index] = 0
            elif self.bricks[index] == -3:
                newState.bricks[index+6] = self.bricks[index]
                newState.bricks[index] = 0
                newState.fill[index+18] = 1
                newState.fill[index] = 0
        if action[1] == 'right':
            if self.bricks[index] == 2:
                newState.bricks[index+1] = self.bricks[index]
                newState.bricks[index] = 0
                newState.fill[index+2] = 1
                newState.fill[index] = 0
            elif self.bricks[index] == 3:
                newState.bricks[index+1] = self.bricks[index]
                newState.bricks[index] = 0
                newState.fill[index+3] = 1
                newState.fill[index] = 0
            elif self.bricks[index] == 1:
                newState.bricks[index+1] = self.bricks[index]
                newState.bricks[index] = 0
                newState.fill[index+2] = 1
                newState.fill[index] = 0
                newState.currentLocation = index+1
        if action[1] == 'left':
            if self.bricks[index] == 2:
                newState.bricks[index-1] = self.bricks[index]
                newState.bricks[index] = 0
                newState.fill[index-1] = 1
                newState.fill[index+1] = 0
            elif self.bricks[index] == 3:
                newState.bricks[index-1] = self.bricks[index]
                newState.bricks[index] = 0
                newState.fill[index-1] = 1
                newState.fill[index+2] = 0
            elif self.bricks[index] == 1:
                newState.bricks[index-1] = self.bricks[index]
                newState.bricks[index] = 0
                newState.fill[index-1] = 1
                newState.fill[index+1] = 0
                newState.currentLocation = index-1
        return newState

    def __str__(self):
        show = []
        show = [0]*36
        for index in range(36):
            if (self.bricks[index] == 1):
                show[index] = '1'
                show[index+1] = '1'
            elif (self.bricks[index] == 2):
                show[index] = '2'
                show[index+1] = '2'
            elif (self.bricks[index] == 3):
                show[index] = '3'
                show[index+1] = '3'
                show[index+2] = '3'
            elif (self.bricks[index] == -2):
                show[index] = '4'
                show[index+6] = '4'
            elif (self.bricks[index] == -3):
                show[index] = '5'
                show[index+6] = '5'
                show[index+12] = '5'
        lines = []
        lines.append('---------------')
        for n in [0, 6, 12, 18, 24, 30]:
            newLine = '|'
            for cell in show[n:n+6]:
                if cell == 0:
                    cell = ' '
                newLine += cell
            if n!= 12:
                newLine = newLine + '|'
            newLine = ' '.join(newLine)
            lines.append(newLine)
        lines.append('---------------')
        lines = '\n'.join(lines)
        return lines

    def __eq__(self, other):
        return (self.bricks == other.bricks)

    def __hash__(self):
        return hash(str(self.bricks))

### Part 2: define seacrh problem
class searchProblem:
    def __init__(self, state):
        self.state = state

    def currentState(self):
        return self.state

    def nextStates(self, state):
        next = []
        for action in state.nextActions():
            next.append((state.nextState(action), action, 1))
        return next

    def theEnd(self, state):
        return state.goalState()


### Part 3: define seacrh method
import Queue
def depthFirstSearch(problem):
    fringeQueue = Queue.LifoQueue()       
    visited = set([])
    path = ()
    node = problem.currentState()
    fringeQueue.put((node, path))
    while (fringeQueue):
        # print len(visited)
        (node, path) = fringeQueue.get()
        if problem.theEnd(node):
            return path
            break
        if node not in visited:
            successors = problem.nextStates(node)
            visited.add(node)
        else:
            successors = []
        for successor in successors:
            if successor[0] not in visited:
                fringeQueue.put(( successor[0], path+(successor[1],) ))

def breadthFirstSearch(problem):
    fringeQueue = Queue.Queue()       
    visited = set([])
    path = ()
    node = problem.currentState()
    fringeQueue.put((node, path))
    while (fringeQueue):
        # print len(visited)
        (node, path) = fringeQueue.get()
        if problem.theEnd(node):
            return path
            break
        if node not in visited:
            successors = problem.nextStates(node)
            visited.add(node)
        else:
            successors = []
        for successor in successors:
            if successor[0] not in visited:
                fringeQueue.put(( successor[0], path+(successor[1],) ))

def manDistance(state):
    return ( 16-state.currentLocation )

def greedySearch(problem):
    fringeQueue = Queue.PriorityQueue()       
    visited = set([])
    priority_number = 0
    path = ()
    node = problem.currentState()
    fringeQueue.put(( priority_number, (node, path) ))
    while (fringeQueue):
        print len(visited)
        (priority_number, (node, path)) = fringeQueue.get()
        if problem.theEnd(node):
            return path
            break
        if node not in visited:
            successors = problem.nextStates(node)
            visited.add(node)
        else:
            successors = []
        for successor in successors:
            if successor[0] not in visited:
                priority_number = manDistance(successor[0])
                fringeQueue.put(( priority_number, ( successor[0], path+(successor[1],) ) ))

def aStarSearch(problem):
    fringeQueue = Queue.PriorityQueue()       
    visited = set([])
    priority_number = 0
    path = ()
    node = problem.currentState()
    fringeQueue.put(( priority_number, (node, path) ))
    while (fringeQueue):
        # print len(visited)
        (priority_number, (node, path)) = fringeQueue.get()
        if problem.theEnd(node):
            return path
            break
        if node not in visited:
            successors = problem.nextStates(node)
            visited.add(node)
        else:
            successors = []
        for successor in successors:
            if successor[0] not in visited:
                priority_number = len(path) + manDistance(successor[0])
                fringeQueue.put(( priority_number, ( successor[0], path+(successor[1],) ) ))

### Part 4: main program
if __name__ == '__main__':
    '''
    numberList = [   0,-2, 0, 0, 0, 0, \
                     0, 0, 0, 0,-2, 0, \
                     1, 0,-2, 0, 0, 0, \
                     0, 0, 0, 0, 0, 0, \
                     -2, 0, 0, 3, 0, 0, \
                     0, 0, 0, 0, 0, 0]
    '''
    numberList = [   0,-2, 2, 0,-2, 0, \
                     0, 0, 2, 0, 0, 0, \
                     1, 0,-2,-3, 0, 0, \
                    -3, 0, 0, 0, 0, 0, \
                     0, 0,-2, 0, 2, 0, \
                     0, 0, 0, 3, 0, 0]
    state = unblockMeState(numberList)
    problem = searchProblem(state)
    path = aStarSearch(problem)

    print('========================================')
    print('Need %d moves to solve this puzzle: %s' % (len(path), str(path)))
    print('========================================')
    print(state)
    i = 1
    for action in path:
        state = state.nextState(action)
        print('move#%d: %s' % (i, action))
        print(state)
        i += 1
    

