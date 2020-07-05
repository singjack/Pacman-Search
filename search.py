# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    # References: https://medium.com/@akshdeep.sharma1/dfs-bfs-coding-blog-week-10-619175d9469
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    stack = util.Stack()
    visited = []
    root = problem.getStartState()
    # (location, path)
    rootNode = (root, [])
    stack.push(rootNode)
    while stack:
        currNode = stack.pop()
        # print "CurrNode Location: ", currNode[0]
        # print "CurrNode Path: ", currNode[1]
        visited.append(currNode[0])
        # print "Is the currNode a goal?", problem.isGoalState(currNode[0])
        if problem.isGoalState(currNode[0]):
            # print "Goal Path found: ", currNode[1]
            return currNode[1]
        else:
            # print "CurrNode's successors:", problem.getSuccessors(currNode[0])
            successors = problem.getSuccessors(currNode[0])
            # Problem.getSucessors will prioritize North, South, East, West when printing out successors
            # This gives our DFS a priority of expanding through paths: West, East, South, North, when searching
            for element in successors:
                if element[0] not in visited:
                    stack.push((element[0], currNode[1] + [element[1]]))
                else:
                    continue
                

    return 0


def breadthFirstSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST 
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    directionsList = [] #Ultimately holds direction list to the goal state to be return
    visitedNodes = [] 
    currPath = util.Queue() #holds the current path of each node
    frontier = util.Queue() #layer that fans out for search
    currNode = problem.getStartState()  
    #Quick check to reutrn if starting state is also Goal state
    if(problem.isGoalState(currNode)):
        return[]
    frontier.push(currNode) #enqueued starting node
    # visitedNodes.append(currNode)
    currNode = frontier.pop()
    while(problem.isGoalState(currNode) == False):
        if currNode not in visitedNodes:
            successors = problem.getSuccessors(currNode)
            visitedNodes.append(currNode)
                # #now we want to look at first node in Queue
            # for i in successors:
            #     print(i[0])
            #     frontier.push(i[0])
            # for j in successors: 
            #     directionsList.append(j[1])
            #     tempDirections = directionsList
            #     currPath.push(tempDirections)
            i=0
            while i < len(successors):
                frontier.push(successors[i][0])
                currPath.push(directionsList + [successors[i][1]])
                i+=1

        directionsList = currPath.pop()
        currNode = frontier.pop() #grabs top item
        
    return directionsList

def uniformCostSearch(problem):
    # """Search the node of least total cost first."""
    '''
    Resources that I consulted in helping me write my BFS algorithm
    References were for conceptual aid only!
    Youtube Video by John Levine: https://www.youtube.com/watch?v=dRMvK76xQJI
    '''
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    directionsList = [] #Ultimately holds direction list to the goal state to be return
    visitedNodes = [] 
    cost = 0
    currPath = util.PriorityQueue() #holds the current path of each node
    frontier = util.PriorityQueue()
    currNode = problem.getStartState()
    if(problem.isGoalState(currNode)): #returns if start state is goal
        return[]
    frontier.push(currNode,-1)
    currNode = frontier.pop()

    while(problem.isGoalState(currNode) == False):
        if currNode not in visitedNodes:
            successors = problem.getSuccessors(currNode)
            visitedNodes.append(currNode)
            i=0
            while i < len(successors):
                if successors[i][0] not in visitedNodes:
                    # temp = directionsList + [successors[i][1]]
                    currPath.push(directionsList + [successors[i][1]], problem.getCostOfActions(directionsList + [successors[i][1]]))
                    frontier.push(successors[i][0],problem.getCostOfActions(directionsList + [successors[i][1]]))
                i+=1
        directionsList = currPath.pop()
        currNode = frontier.pop() #grabs top item
        
    return directionsList            


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # references: https://laconicml.com/a-star-search-algorithm/
    # Use a priorityQ in order to pop the lowest cost node
    priorityQ = util.PriorityQueue()
    visited = []
    root = problem.getStartState()
    # (location, path, COST)
    rootNode = (root, [], 0)
    priorityQ.push(rootNode, 0)
    while priorityQ:
        currNode = priorityQ.pop()
        if problem.isGoalState(currNode[0]):
            return currNode[1]
        else:
            if currNode[0] not in visited:
                visited.append(currNode[0])
                successors = problem.getSuccessors(currNode[0])
                for element in successors:
                    if element[0] not in visited:
                        # f(n) = total cost
                        # f(n) = g(n) + h(n)
                        # f(n) = (cost of parent and self) + (estimated distance to goal)
                        G = element[2] + currNode[2]
                        H = heuristic(element[0], problem)
                        F = G + H
                        successorNode = (element[0], currNode[1] + [element[1]], G)
                        priorityQ.push(successorNode, F)
                    else:
                        continue
            else:
                continue
    return 0      


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
