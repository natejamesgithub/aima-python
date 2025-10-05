import sys
#sys.path.append('/opt/homebrew/lib/python3.9/site-packages')

import collections, os
from planning import *
from logic import *

from submission1_test import verify_solution
from planning_envs import *

# Problem 4: Planning 

""" **IMPORTANT** Reflection (4 pts)
Please *breifly* report your findings and reflect on what they mean:
As I worked on 4b, I found that it was interesting that I needed to specify that certain tiles were adjacent when I constructed my response. 
Then, I realized that when the planning problem is generalizing, it needs to be able to handle all different types of locations and plans. 
Therefore, telling the algorithm whether two spaces are adjacent or not becomes relevant. 
I think my output is incorrect because when I printed the output, it was a list of two actions:
[PutDown(R1, C3, D3), PutDown(R1, C2, D3)]. I believe this output is incorrect because these two actions can't both 
be performed back to back when the robot isn't holding a package. 
Planning algorithms are very useful for generalizing these issues and having the machine solve logic problems like these ones using planning. 
I liked how easy it was to write and run this planning algorithm, especially compared to the searching in the last project. 
Abstracting this algorithm, machines can solve lots of these type of problems very easily.
"""

# Blocks world modification
def blocksWorldModPlan():
    # BEGIN_YOUR_CODE (make modifications to the initial and goal states)
    initial_state = 'On(A, B) & Clear(A) & OnTable(B) & On(C,D) & Clear(C) & OnTable(D)'
    goal_state = 'On(B, A) & On(C, B) & On(D, C)'
    # END_YOUR_CODE

    planning_problem = \
    PlanningProblem(initial=initial_state,
                    goals=goal_state,
                    actions=[Action('ToTable(x, y)',
                                    precond='On(x, y) & Clear(x)',
                                    effect='~On(x, y) & Clear(y) & OnTable(x)'),
                             Action('FromTable(y, x)',
                                    precond='OnTable(y) & Clear(y) & Clear(x)',
                                    effect='~OnTable(y) & ~Clear(x) & On(y, x)')])
    
    return linearize(GraphPlan(planning_problem).execute())

"""
def logisticsPlan():
    # BEGIN_YOUR_CODE (use the previous problem as a guide and uncomment the starter code below if you want!)
    initial_state = 'RobotIn(R1,D1) & RobotCarrying(R1,C1) & ContainerAt(C2,D1) & ContainerAt(C3,D1) & Adjacent(D1,D2) & Adjacent(D1,D3) & Adjacent(D2,D3) & Adjacent(D2,D1) & Adjacent(D3,D1) & Adjacent(D3,D2)'
    goal_state = 'ContainerAt(C1,D3) & ContainerAt(C2,D3) & ContainerAt(C3,D3)'
    planning_problem = \
        PlanningProblem(initial=initial_state,
                        goals=goal_state,
                        actions=[Action('PickUp(robot,container,location)',
                                        precond='RobotNotCarrying(robot) & RobotIn(robot,location) & ContainerAt(container,location)',
                                        effect='~ContainerAt(container,location) & ~RobotNotCarrying(robot) & RobotCarrying(robot,container)'),
                                 Action('PutDown(robot,container,location)',
                                        precond='RobotIn(robot,location) & RobotCarrying(robot,container)',
                                        effect='~RobotCarrying(robot,container) & RobotNotCarrying(robot) & ContainerAt(container,location)'),
                                 Action('RobotMove(robot,location1,location2)',
                                        precond='RobotIn(robot,location1) & Adjacent(location1,location2)',
                                        effect='~RobotIn(robot,location1) & RobotIn(robot,location2)')])
    # END_YOUR_CODE
    
    return linearize(GraphPlan(planning_problem).execute())
"""


if __name__ == "__main__":
    
    """
    Call the above functions here with initial/goal states for testing your code.
    """

    #initial_state = 'In(C1, R1) & In(C2, D1) & In(C3, D2) & In(R1, D1) & Holding(R1)'
    #goal_state = 'In(C1, D2)'
    #print(logisticsPlanCustom(initial_state, goal_state))

    #initial_state = 'In(C1, R1) & In(C2, D1) & In(C3, D2) & In(R1, D1) & Holding(R1)'
    #goal_state = "In(C1, D1) & In(C3, R1) & In(R1, D3)"
    #print(logisticsPlanCustom(initial_state, goal_state))
   
    # NOW WORKS: issue was in problem domain definition 
    #P = double_tennis_problem()
    #print(GraphPlan(P).execute())

    #P = shopping_problem()
    #gplan = GraphPlan(P).execute()
    #print(gplan)
    #print(Linearize(P).execute())
    """
    [[[PItem(Milk), PSells(SM, Milk), PSells(SM, Banana), PStore(HW), 
    PItem(Banana), PStore(SM), Go(Home, HW), PSells(HW, Drill), 
    PItem(Drill), Go(Home, SM)], 
    [Buy(Drill, HW), Buy(Banana, SM), Buy(Milk, SM)]]]
    """

    #P = shopping_problem()
    #P = air_cargo()
    #P = double_tennis_problem()
    #P = have_cake_and_eat_cake_too()
    #init = "In(C1, R1) & In(C2, D1) & In(C3, D2) & In(R1, D1) & Holding(R1)"
    #goal_state = "In(C1,D1)"
    #goal_state = "In(C2, D3) & In(C3, D3)"
    #goal_state = "In(C1, D3) & In(C2, D3) & In(C3, D3)"
    # putdown(c1), pickup(c2), move(d3), putdown(c2), move(d2), pickup(c3), move(d3), putdown(c3)
    
    #goal_state = "In(C3, D1)"
    #goal_state = "In(C2, D3)"
    #goal_state = "In(C3, D3)"
    # putdown c1, move r1 to d2, pickup c3 in d2, move robot to d1, putdown c3
    #goal_state = "In(C1, D2) & In(C3, D3)"
    #P = logisticsPlanCustom(init, goal_state)
    
    # PickUp(R1, C2, D2) in level 1 is NOT (shouldn't be) POSSIBLE due to mutexes.
    """
    P = PlanningProblem(initial = init,
                    goals = goal_state,
                    precond='In(r, d) & In (c, d) & ~H
                                   olding(r)',
                                    effect='Holding(r) & ~In(c, d) & In(c, r)', 
                                    domain='Robot(r) & Place(d) & Container(c)'),
                             Action('PutDown(r, c, d)', 
                                    precond='In(r, d) & In(c, r) & Holding(r)',
                                    effect='~Holding(r) & ~In(c, r) & In(c, d)',
                                    domain='Robot(r) & Place(d) & Container(c)'),
                            Action('Move(r, d_start, d_end)',
                                   precond='In(r,d_start)',
                                   effect='~In(r, d_start) & In(r, d_end)',
                                   domain='Robot(r) & Place(d_start) & Place(d_end)')],
                domain='Container(C1) & Container(C2) & Place(D1) & Place(D2) & Robot(R1)')
    """
    #P = double_tennis_problem_simple2() 
    
    #P = rush_hour()
    P = rush_hour_optimized()
    #verify_solution(P)
    
    #GraphPlan(P).execute()
    #print(Linearize(P).execute())
    verify_solution(P)

 
"""
Standard logistics environment
Container(C1) & Container(C2) & Container(C3) & Place(D1) & Place(D2) & Place(D3) & Robot(R1)

Start:
In(C1, R1) & In(C2, D1) & In(C3, D2) & In(R1, D1) & Holding(R1)

Goal:
In(C1, D1) & In(C3, R1) & In(R1, D3)

Start:
 - C1 is in R1
 - C2 is in D1
 - C3 is in D2
 - R1 is in D1
 - R1 is currnetly holding

How to get to:
 - C1 in D1 (just put it down)
 - C3 in R1 (robot must move to D2, Pick up C3)
 - R1 in D3 (robot must move to D3)
 
So a valid solution is:
["PutDown(R1, C1, D1)", "Move(R1, D1, D2)", "PickUp(R1, C3, D2)", "Move(R1, D2, D3)"]
"""