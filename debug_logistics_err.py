
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
