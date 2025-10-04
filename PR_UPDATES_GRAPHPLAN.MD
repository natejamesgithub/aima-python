# Improvements / Necessary Fixes to GraphPlan in AIMA

## Fixes to the double tennis environment

 - Original env used `a`, `b` in goals rather than `A`, `B` as defined in initial.
  - IIRC, `a` and `b`, that is, lowercase variables, can be satisfied by any other variable? Hence, the test still passed, but it was probably not the intention
 - Environment failed to search `LeftNet` because it doesn't show up in initial or domain, only goal.
 - Original env:
    """
    return PlanningProblem(
        initial='At(A, LeftBaseLine) & At(B, RightNet) & Approaching(Ball, RightBaseLine) & Partner(A, B) & Partner(B, A)',
        goals='Returned(Ball) & At(a, LeftNet) & At(a, RightNet)',
        actions=[Action('Hit(actor, Ball, loc)',
                        precond='Approaching(Ball, loc) & At(actor, loc)',
                        effect='Returned(Ball)'),
                 Action('Go(actor, to, loc)',
                        precond='At(actor, loc)',
                        effect='At(actor, to) & ~At(actor, loc)')])
    """
 - Note - this passed the pytest manual tests, but not GraphPlan algorithm natively (although that was broken in general ...)
 

## Explicit state and action mutexes

 - In the original implementation, state and action layers, as well as state (proposition) and action mutexes were jumbled together, with no differentiation.
 - Technically, I'm not certain that an issue existed with this presentation, but it doesn't follow any of the learner-friendly material on GraphPlan that exists. 
 - I repurposed the `GraphPlan.graph.levels[i].mutex` to refer to action mutexes, and added a `state_mutexes` attribute to refer to state mutexes.

## No Interference Computation

 - In the original implementation, I don't see interference (one action deletes the precondition of another) being computed anywhere.
 - I have added interference explicitly.

## Linearization Error?

 - TODO

## Level compute/expand issue

 - In the original implementation, mutexes were computed after expanding a level and performing goal tests. Therefore, the goal test would not be able to test the goals until one extra layer had been expanded. I reordered the `expand_graph` method to expand a layer, and populate `state_mutexes` before the goal test.

## Extract_Solution Issue

 - `extract_solution` is a method with the purpose of expanding the graph backwards to the start, identifying subgoals for each next layer, and selecting a set of actions that fulfill this layers subgoals, proceeding to the next layer with the preconditions of those actions as new subgoals. However, the authors wrote this implementation with `itertools.product(*actions)`, which chooses combinations of specifically one action that satisfies each goal. Unfortunately, this is not satisfactory, and certain combinations may not provide necessary support for later layers, despite not having explicit mutexes for these dependencies.
 - I have replaced this with a full recursive DFS backwards search, with early exiting. This is required to make it efficient, as technically now this backwards search is a Cartesian product of the powerset of actions, which is 2^(2n) different action sets to test (infeasible)

## Added debugging tools

## Added actual GraphPlan tests

 - Currently tests exist for environments, with hardcoded solutions encoded to verify that the goal state actually is achievable.
 - However, there are no GraphPlan algorithm tests (?)
 - I've created a pytest file and added it to the test dir to improve reliability (and for my own debugging)


## Separated Environments from Algorithms

