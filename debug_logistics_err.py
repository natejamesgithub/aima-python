
# In(C1, R1) & In(C2, D1) & In(C3, D2) & In(R1, D1) & Holding(R1)
# In(C3, D3)

# Sol should be:
# putdown(c1), move(r1, d2), pickup c3, move d3, putdown d3a


ISSUE:
    PickUp(R1, C1, D2),
    PickUp(R1, C3, D2),
in same layer.
    
[
    [
        [
            PHolding(R1),
            PContainer(C3),
            PIn(C1, R1),
            PPlace(D2),
            PPlace(D3),
            PContainer(C1),
            PRobot(R1),
            Move(R1, D1, D2),
            PIn(C3, D2),
        ],
        [
            PutDown(R1, C1, D2),
            PContainer(C3),
            PPlace(D2),
            PPlace(D3),
            PIn(R1, D2),
            PContainer(C1),
            PRobot(R1),
            PIn(C3, D2),
        ],
        [
            PContainer(C3),
            PPlace(D2),
            PPlace(D3),
            PickUp(R1, C1, D2),
            PIn(R1, D2),
            PRobot(R1),
            PickUp(R1, C3, D2),
        ],
        [
            PHolding(R1),
            PContainer(C3),
            Move(R1, D2, D3),
            PPlace(D3),
            PIn(C3, R1),
            PRobot(R1),
        ],
        [PutDown(R1, C3, D3)],
    ],
    [
        [
            PutDown(R1, C1, D1),
            PContainer(C3),
            PPlace(D2),
            PPlace(D3),
            PIn(R1, D1),
            PPlace(D1),
            PRobot(R1),
            PIn(C3, D2),
        ],
        [
            PContainer(C3),
            PPlace(D2),
            PPlace(D3),
            PRobot(R1),
            PNotHolding(R1),
            Move(R1, D1, D2),
            PIn(C3, D2),
        ],
        [
            PContainer(C3),
            PPlace(D2),
            PPlace(D3),
            PIn(R1, D2),
            PRobot(R1),
            PickUp(R1, C3, D2),
        ],
        [
            PHolding(R1),
            PContainer(C3),
            Move(R1, D2, D3),
            PPlace(D3),
            PIn(C3, R1),
            PRobot(R1),
        ],
        [PutDown(R1, C3, D3)],
    ],
]






goal: 
[Robot(R1), In(C3, R1), Place(D3), In(R1, D3), Container(C3), In(R1, D3), In(C1, D3), NotHolding(R1), Robot(R1), Place(D3), Container(C1), In(C2, D3)]

These non mutex actions that lead to above

[[PRobot(R1), PIn(C3, R1), PPlace(D3), PIn(R1, D3), PContainer(C3), PickUp(R1, C1, D3), PIn(C2, D3)]]



 

# Why is `PIn(C3, R1)`  not mutex with `PickUp(R1, C1, D3)`?


Technically, no direct precondition error
PIn(C3,R1) required a PickUp(R1, C3, ?) at some point, 


[PRobot(R1)], [PPlace(D3)], [PContainer(C3)], PHolding(R1), [PIn(C2, D3)] [ Move(R1, D2, D3), Move(R1, D1, D3)]], PIn(C3, R1)

# (PHolding(R1), PIn(C2, D3)) is mutex @ -3 level

"""
goal state -1
putdown layer
previous_layer -2
wacky_actions - (PHolding(R1), PIn(C2, D3)) is mutex - shoudl be move to d3
previous_layer -3 - (Holding(R1), In(C2, D3)) is mutex
should be pickup(c3) - 


Not inconsistent effects
Not interference
Has to be competing needs - preconditions are mutex
 - Therefore, (Holding(R1), In(C2, D3)) is likely mutex - it is

Why are these mutex? Props are only mutex if actions that cause it in prior layer are ...
 - (pickup anything, holding(r1)), (In(C2, D3), putdown(d2,d3))
 - Pickup(R1, C3, D2), PIn(C2, D3) shouldn't be mutex, but it is
 - 

"""

PickUp(R1, C1, D2), PickUp(R1, C3, D2) are not mutex
Why?
Preconds: 
    In(r, d) & In (c, d) & ~Holding(r)
Effects:
    Holding(r) & ~In(c, d) & In(c, r)
    
    
They negate the same precondition? One makes the others precondition false


(PIn(C2, D3), Move(R1, D2, D3), PIn(C3, R1), PHolding(R1), PRobot(R1), PPlace(D3), PContainer(C3))  failed due to  (PIn(C2, D3), PHolding(R1))  in mutex

mutex (PHolding(R1), PIn(C2, D3)) excludes our action set from being applicable.
