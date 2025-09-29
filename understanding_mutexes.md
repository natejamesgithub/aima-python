Actions: Buy, Go

Go(Home, SM)
Go(Home, HW)

It includes Place, Store, Item, Sells in state (?)

Level 0: 

Correctly identifies it can go to HW, SM, adds as mutexes
 -  Relies on At(Home) precondition, notes this

Level 1:

Adds Place(SM), Place(HW) into state, adds NotAt(Home) to state (we still have At(Home)
 - Says no mutexes or actions - hasn't been generated yet.

Graph:

Level 1 is updated to have all applicable actions? Large mutex state:

Has prior current state

 - Adds Buy(all, hw/sm appropriate)
 - Mutex: 
  - not at home and at home
  - Go(Home, HW), At(Home) ? GPT tells me this means that Go deletes the At(Home), so in the next state, these are disjoint. (makes sense)
  - A mutex, therefore, means that two states or results of actions or intertwined, cannot have effects or states in the next state concurrently.


  Mutex: 
  {{PNotAt(Home), PAt(Home)}, 
  {Go(Home, HW), PAt(Home)}, 
  {Go(Home, SM), PAt(Home)}, 
  {Go(HW, Home), PNotAt(Home)}, 
  {Go(HW, Home), Go(Home, HW)}, 
  {Go(HW, Home), Go(Home, SM)}, 
  {Go(SM, Home), PNotAt(Home)}, 
  {Go(SM, Home), Go(Home, HW)}, #duplicate?
  {Go(SM, Home), Go(Home, SM)}, 
  {PAt(HW), Go(HW, Home)}, 
  {PAt(HW), Go(HW, SM)}, 
  {Go(HW, SM), Go(Home, HW)}, 
  {Go(HW, Home), Go(SM, HW)}, 
  {Go(HW, SM), Go(SM, HW)}, 
  {Go(SM, Home), PAt(SM)}, 
  {Go(SM, HW), PAt(SM)}, 
  {Go(Home, SM), Go(SM, HW)}, {Go(HW, SM), Go(SM, Home)}, {PNotAt(Home), Go(Home, HW)}, {PNotAt(Home), Go(Home, SM)}, {NotAt(Home), At(Home)}} # duplicate

  All seem well, and NOT sufficient






The issue is that:


At layer 1 (index -2), we have:

print(self.levels[index].mutex)
[{PAt(Home), PNotAt(Home)}, {Go(Home, HW), PAt(Home)}, {Go(Home, SM), PAt(Home)}, {Go(HW, Home), PNotAt(Home)}, {Go(Home, HW), Go(HW, Home)}, {Go(Home, SM), Go(HW, Home)}, {PNotAt(Home), Go(SM, Home)}, {Go(Home, HW), Go(SM, Home)}, {Go(Home, SM), Go(SM, Home)}, {Go(HW, Home), PAt(HW)}, {PAt(HW), Go(HW, SM)}, {Go(Home, HW), Go(HW, SM)}, {Go(HW, Home), Go(SM, HW)}, {Go(SM, HW), Go(HW, SM)}, {Go(SM, HW), PAt(SM)}, {Go(SM, Home), PAt(SM)}, {Go(SM, Home), Go(HW, SM)}, {Go(Home, SM), Go(SM, HW)}, {Go(Home, HW), PNotAt(Home)}, {Go(Home, SM), PNotAt(Home)}, {At(Home), NotAt(Home)}]

And our goal permutations is:

print(list(goal_perm))
[(At(SM), Sells(SM, Milk)), (At(SM), Store(SM)), (At(SM), Item(Milk)), (At(SM), At(SM)), (At(SM), Sells(SM, Banana)), (At(SM), Store(SM)), (At(SM), Item(Banana)), (At(SM), At(HW)), (At(SM), Sells(HW, Drill)), (At(SM), Store(HW)), (At(SM), Item(Drill)), (Sells(SM, Milk), Store(SM)), (Sells(SM, Milk), Item(Milk)), (Sells(SM, Milk), At(SM)), (Sells(SM, Milk), Sells(SM, Banana)), (Sells(SM, Milk), Store(SM)), (Sells(SM, Milk), Item(Banana)), (Sells(SM, Milk), At(HW)), (Sells(SM, Milk), Sells(HW, Drill)), (Sells(SM, Milk), Store(HW)), (Sells(SM, Milk), Item(Drill)), (Store(SM), Item(Milk)), (Store(SM), At(SM)), (Store(SM), Sells(SM, Banana)), (Store(SM), Store(SM)), (Store(SM), Item(Banana)), (Store(SM), At(HW)), (Store(SM), Sells(HW, Drill)), (Store(SM), Store(HW)), (Store(SM), Item(Drill)), (Item(Milk), At(SM)), (Item(Milk), Sells(SM, Banana)), (Item(Milk), Store(SM)), (Item(Milk), Item(Banana)), (Item(Milk), At(HW)), (Item(Milk), Sells(HW, Drill)), (Item(Milk), Store(HW)), (Item(Milk), Item(Drill)), (At(SM), Sells(SM, Banana)), (At(SM), Store(SM)), (At(SM), Item(Banana)), (At(SM), At(HW)), (At(SM), Sells(HW, Drill)), (At(SM), Store(HW)), (At(SM), Item(Drill)), (Sells(SM, Banana), Store(SM)), (Sells(SM, Banana), Item(Banana)), (Sells(SM, Banana), At(HW)), (Sells(SM, Banana), Sells(HW, Drill)), (Sells(SM, Banana), Store(HW)), (Sells(SM, Banana), Item(Drill)), (Store(SM), Item(Banana)), (Store(SM), At(HW)), (Store(SM), Sells(HW, Drill)), (Store(SM), Store(HW)), (Store(SM), Item(Drill)), (Item(Banana), At(HW)), (Item(Banana), Sells(HW, Drill)), (Item(Banana), Store(HW)), (Item(Banana), Item(Drill)), (At(HW), Sells(HW, Drill)), (At(HW), Store(HW)), (At(HW), Item(Drill)), (Sells(HW, Drill), Store(HW)), (Sells(HW, Drill), Item(Drill)), (Store(HW), Item(Drill))]

Notably, including

(At(SM), At(HW))

But, since we don't include our persistance state, it doesn't recognize the issue with this.



Then

we go to index -3, layer 0

print(supporting_actions_lists)
[[Go(Home, SM)], [PSells(SM, Milk)], [PStore(SM)], [PItem(Milk)], [Go(Home, SM)], [PSells(SM, Banana)], [PStore(SM)], [PItem(Banana)], [Go(Home, HW)], [PSells(HW, Drill)], [PStore(HW)], [PItem(Drill)]]

our supporting actions includes 

[Go(Home, SM)], [Go(Home, HW)]

But our mutexes only include:
[{Go(Home, HW), PAt(Home)}, {Go(Home, SM), PAt(Home)}]

Shouldn't we have {Go(Home, HW), Go(Home, SM)} ? This would solve the issue...




WHY do we not have a {Go(Home, HW), Go(Home, SM)} mutex?



Forward Search
<Graph>
  Objects: {RightBaseline, LeftNet, LeftBaseline, RightBaseLine, B, LeftBaseLine, RightNet, Ball, A}
Level 0:
<Level>
  Current State: 
  
  {At(A, LeftBaseLine), At(B, RightNet), Approaching(Ball, RightBaseLine), Partner(A, B), Partner(B, A), CourtLoc(LeftNet), CourtLoc(RightNet), CourtLoc(LeftBaseline), CourtLoc(RightBaseline)}

  Actions: 
  
  {
    PAt(A, LeftBaseLine), 
    PAt(B, RightNet), 
    PApproaching(Ball, RightBaseLine), 
    PPartner(A, B), PPartner(B, A), 
    PCourtLoc(LeftNet), PCourtLoc(RightNet), PCourtLoc(LeftBaseline), PCourtLoc(RightBaseline), 

    Go(B, RightBaseline, RightNet), Go(B, LeftNet, RightNet), Go(B, LeftBaseline, RightNet), Go(B, RightBaseLine, RightNet), Go(B, LeftBaseLine, RightNet), Go(B, Ball, RightNet), Go(B, A, RightNet), Go(A, RightBaseline, LeftBaseLine), Go(A, LeftNet, LeftBaseLine), Go(A, LeftBaseline, LeftBaseLine), Go(A, RightBaseLine, LeftBaseLine), Go(A, B, LeftBaseLine), Go(A, RightNet, LeftBaseLine), Go(A, Ball, LeftBaseLine)}

# Too unconstrained
 - Can go to ball?
 - Duplicate actions

  Mutex: 
  
  {{Go(B, RightBaseline, RightNet), PAt(B, RightNet)}, {Go(B, LeftNet, RightNet), PAt(B, RightNet)}, {Go(B, LeftBaseline, RightNet), PAt(B, RightNet)}, {Go(B, RightBaseLine, RightNet), PAt(B, RightNet)}, {Go(B, LeftBaseLine, RightNet), PAt(B, RightNet)}, {Go(B, Ball, RightNet), PAt(B, RightNet)}, {Go(B, A, RightNet), PAt(B, RightNet)}, {PAt(A, LeftBaseLine), Go(A, RightBaseline, LeftBaseLine)}, {PAt(A, LeftBaseLine), Go(A, LeftNet, LeftBaseLine)}, {PAt(A, LeftBaseLine), Go(A, LeftBaseline, LeftBaseLine)}, {PAt(A, LeftBaseLine), Go(A, RightBaseLine, LeftBaseLine)}, {Go(A, B, LeftBaseLine), PAt(A, LeftBaseLine)}, {PAt(A, LeftBaseLine), Go(A, RightNet, LeftBaseLine)}, {PAt(A, LeftBaseLine), Go(A, Ball, LeftBaseLine)}, {Go(B, LeftNet, RightNet), Go(B, RightBaseline, RightNet)}, {Go(B, LeftBaseline, RightNet), Go(B, RightBaseline, RightNet)}, {Go(B, RightBaseLine, RightNet), Go(B, RightBaseline, RightNet)}, {Go(B, LeftBaseLine, RightNet), Go(B, RightBaseline, RightNet)}, {Go(B, Ball, RightNet), Go(B, RightBaseline, RightNet)}, {Go(B, A, RightNet), Go(B, RightBaseline, RightNet)}, {Go(B, LeftNet, RightNet), Go(B, LeftBaseline, RightNet)}, {Go(B, LeftNet, RightNet), Go(B, RightBaseLine, RightNet)}, {Go(B, LeftBaseLine, RightNet), Go(B, LeftNet, RightNet)}, {Go(B, LeftNet, RightNet), Go(B, Ball, RightNet)}, {Go(B, LeftNet, RightNet), Go(B, A, RightNet)}, {Go(B, RightBaseLine, RightNet), Go(B, LeftBaseline, RightNet)}, {Go(B, LeftBaseLine, RightNet), Go(B, LeftBaseline, RightNet)}, {Go(B, Ball, RightNet), Go(B, LeftBaseline, RightNet)}, {Go(B, LeftBaseline, RightNet), Go(B, A, RightNet)}, {Go(B, LeftBaseLine, RightNet), Go(B, RightBaseLine, RightNet)}, {Go(B, RightBaseLine, RightNet), Go(B, Ball, RightNet)}, {Go(B, RightBaseLine, RightNet), Go(B, A, RightNet)}, {Go(B, LeftBaseLine, RightNet), Go(B, Ball, RightNet)}, {Go(B, LeftBaseLine, RightNet), Go(B, A, RightNet)}, {Go(B, Ball, RightNet), Go(B, A, RightNet)}, {Go(A, LeftNet, LeftBaseLine), Go(A, RightBaseline, LeftBaseLine)}, {Go(A, LeftBaseline, LeftBaseLine), Go(A, RightBaseline, LeftBaseLine)}, {Go(A, RightBaseLine, LeftBaseLine), Go(A, RightBaseline, LeftBaseLine)}, {Go(A, B, LeftBaseLine), Go(A, RightBaseline, LeftBaseLine)}, {Go(A, RightNet, LeftBaseLine), Go(A, RightBaseline, LeftBaseLine)}, {Go(A, Ball, LeftBaseLine), Go(A, RightBaseline, LeftBaseLine)}, {Go(A, LeftNet, LeftBaseLine), Go(A, LeftBaseline, LeftBaseLine)}, {Go(A, RightBaseLine, LeftBaseLine), Go(A, LeftNet, LeftBaseLine)}, {Go(A, B, LeftBaseLine), Go(A, LeftNet, LeftBaseLine)}, {Go(A, RightNet, LeftBaseLine), Go(A, LeftNet, LeftBaseLine)}, {Go(A, Ball, LeftBaseLine), Go(A, LeftNet, LeftBaseLine)}, {Go(A, RightBaseLine, LeftBaseLine), Go(A, LeftBaseline, LeftBaseLine)}, {Go(A, B, LeftBaseLine), Go(A, LeftBaseline, LeftBaseLine)}, {Go(A, RightNet, LeftBaseLine), Go(A, LeftBaseline, LeftBaseLine)}, {Go(A, Ball, LeftBaseLine), Go(A, LeftBaseline, LeftBaseLine)}, {Go(A, B, LeftBaseLine), Go(A, RightBaseLine, LeftBaseLine)}, {Go(A, RightNet, LeftBaseLine), Go(A, RightBaseLine, LeftBaseLine)}, {Go(A, Ball, LeftBaseLine), Go(A, RightBaseLine, LeftBaseLine)}, {Go(A, B, LeftBaseLine), Go(A, RightNet, LeftBaseLine)}, {Go(A, B, LeftBaseLine), Go(A, Ball, LeftBaseLine)}, {Go(A, RightNet, LeftBaseLine), Go(A, Ball, LeftBaseLine)}}

![alt text](<Screenshot from 2025-09-28 11-02-00.png>)

1. We don't have !Eaten as a starting propostion, or ever .. should we? Do we need this? Note - we miss a mutex here b/c of it.
2. We have (Bake, Have) in our mutexes, they do not. Is this valid?
3. We have an invalid mutex {have} .... ?
4. We are missing (have, eaten)
5. Can we differentiate between different types of mutexes? I.e. state-state vs action-state, etc.?
6. We have duplicate (have, notHave)



When I add in !Eaten in our start state


file:///home/carwyn/Pictures/Screenshots/Screenshot%20from%202025-09-28%2011-14-54.png 

1. We dont' have mutexes between (have, eaten), (!have, !eaten) in S1. 
 - Something is going wrong (lacking) in our inconsistent support checking
 - Two propositions a,b should be mutex if every actions that produce a is mutex with every action that can produce b.
2. (bake, have) in a2 shouldn't exist
 - This is correct - overriding SBU slides
3. (eat, !have) in a2 shouldn't exist
 - This is correct - overriding SBU slides 


https://www3.cs.stonybrook.edu/~sael/teaching/cse537/Slides/chapter10b.pdf 
TODO:
 - DONE: Remove my recursive backwards checker - it should be enough to just check final state mutexes
 - Fix inconsistent support check
 - Validate improvement on cake problem, where I expect to see mutexes between (have, eaten), (!have, !eaten) in S1
 - Debug shopping problem




ISSUE IDENTIFIED IN INCONSISTENT SUPPORT CHECK:
file:///home/carwyn/Pictures/Screenshots/Screenshot%20from%202025-09-28%2021-02-27.png

Now I'm getting these concerning (incorrect) mutexes on level 2:

{Eaten(Cake), Have(Cake)}
{Have(Cake)}, 
{Eaten(Cake), NotHave(Cake)}, 
{NotHave(Cake)}

1. Enforce no single atom mutexes
2. Identify where these incorrect mutexes are coming in (note - they are valid on layer 1 ...)

Level 1:
<Level>
  Current State: {NotEaten(Cake), Eaten(Cake), Have(Cake), NotHave(Cake)}
  Actions: {PNotEaten(Cake), PEaten(Cake), PHave(Cake), PNotHave(Cake), Eat(Cake), Bake(Cake)}
  Mutex: {{PEaten(Cake), PNotEaten(Cake)}, {Eat(Cake), PNotEaten(Cake)}, {PNotHave(Cake), PHave(Cake)}, {Eat(Cake), PHave(Cake)}, {PNotHave(Cake), Bake(Cake)}, {Bake(Cake), Eat(Cake)}, {Bake(Cake), PHave(Cake)}, {PNotHave(Cake), Eat(Cake)}, {NotEaten(Cake), Eaten(Cake)}, {NotEaten(Cake), NotHave(Cake)}, {Have(Cake), NotHave(Cake)}, {Eaten(Cake), Have(Cake)}, {Have(Cake)}, {Eaten(Cake), NotHave(Cake)}, {NotHave(Cake)}}


  Mutex: {{PEaten(Cake), PNotEaten(Cake)}, {Eat(Cake), PNotEaten(Cake)}, {PNotHave(Cake), PHave(Cake)}, {Eat(Cake), PHave(Cake)}, {PNotHave(Cake), Bake(Cake)}, {Eat(Cake), Bake(Cake)}, {Bake(Cake), PHave(Cake)}, {PNotHave(Cake), Eat(Cake)}, {Eaten(Cake), NotEaten(Cake)}, {NotEaten(Cake), NotHave(Cake)}, {Eaten(Cake), Have(Cake)}, {Have(Cake), NotHave(Cake)}}

  Probably issue:
   - propositions are maintained in mutexes similarly to actions. I dont' think I'm accounting for this difference when I move to the next state level
    - do we even have the correct logic for moving from action levels to state levels?


    I think we conclude at s2 because we can satisfy with eat -> bake