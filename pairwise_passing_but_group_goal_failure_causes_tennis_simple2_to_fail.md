# Goal States:
[
    At(A, LeftNet), 
    Returned(ball), 
    At(B, LeftNet)
]

#Action sets that lead to goal states
[
    [PAt(A, LeftNet), Go(A, LeftNet, ball), Go(A, LeftNet, B), Go(A, LeftNet, RightNet)], 
    [Hit(A, ball, RightNet), Hit(B, ball, RightNet)], 
    [PAt(B, LeftNet), Go(B, LeftNet, ball), Go(B, LeftNet, A), Go(B, LeftNet, RightNet)]
]

# Allegedly, all combinations are disjoint

Hit(A, ball, RightNet), Hit(B, ball, RightNet)
 - Requires either A or B to be in RightNet
 - First list requires A to move to LeftNet
 - Last list requires B to move to LeftNet

These are disjoint in total, but none of the two are disjoint