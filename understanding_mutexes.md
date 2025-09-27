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