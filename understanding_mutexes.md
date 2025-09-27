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

  All seem well, and sufficient
