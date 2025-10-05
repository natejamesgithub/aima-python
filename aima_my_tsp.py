"""
Code skeleton for A* with TSP
For use with the AIMA codebase: https://github.com/aimacode/aima-python
CMSC 421 - Fall 2025
"""
from time import time
import numpy as np
from search import Problem, astar_search
from scipy.sparse import csgraph

### Define TSP ###

class MyTSP(Problem):

    # NOTE: This is just a suggestion for setting up your __init__,
    # you can use any design you want
    def __init__(self, weights, initial=(0,), goal=None):   
        super().__init__(initial, goal)
        self.weights = weights
        self.num_cities = weights.shape[0]
        self.cities = list(range(0, self.num_cities))

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError
        # TODO: your code here

    # NOTE: If you make your state a list object, you'll wind
    # up with an error like this: TypeError: unhashable type: 'list'
    # One work-around is the make your states tuples instead.
    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError
        # TODO: your code here

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        raise NotImplementedError
        # TODO: your code here

    # NOTE: Remember the full cost includes the round trip back to the starting city!
    # So if you are adding the final city to the path, you should also add the cost
    # for the final edge too.
    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        raise NotImplementedError
        # TODO: your code here

    def value(self, state):
        """For optimization problems, each state has a value. Hill Climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError
        # TODO: your code here

    # NOTE: For debugging purposes, you can use h(n)=0 while writing and testing
    # the rest of your code
    def h(self, node):
        """Return the heuristic value for a given state. astar_search will
        look for this heuristic function when run."""
        raise NotImplementedError        
        # TODO: your code here

### Run A* ###

# NOTE: select a weight matrix to load, depending on where you unzipped them
MATRIX_FILE = '/home/carwyn/dev/phd/ta/aima/aima-python/aima-data/mats_911/5_random_adj_mat_0.txt'

MAT = np.loadtxt(MATRIX_FILE)
print('Loaded road cost matrix:')
print(MAT)
MTSP = MyTSP(MAT)

print('Running A*...')
t0 = time()
tsp_sol = astar_search(MTSP, display=True)
print('Solved in %f seconds'%(time()-t0))

tsp_sol = tsp_sol.state
print('Solution Path: ' + str(tsp_sol))
sol_cost = MTSP.value(tsp_sol)
print('Solution Cost: ' + str(sol_cost))
