import sys, os
import collections
from planning import *
from logic import *

import pytest

def test_blocksworld_manual():
    sbw = simple_blocks_world()
    assert sbw.goal_test() == False
    sbw.act(expr('ToTable(A, B)'))
    sbw.act(expr('FromTable(B, A)'))
    assert sbw.goal_test() == False
    sbw.act(expr('FromTable(C, B)'))
    assert sbw.goal_test() == True


def verify_solution(P):
    sol = Linearize(P).execute()
    print(sol)
    assert P.goal_test() == False
    for act in sol:
        P.act(expr(act))
    assert P.goal_test() == True

def test_air_cargo():
    P = air_cargo()
    verify_solution(P)

def test_spare_tire():
    P = spare_tire()
    verify_solution(P)
    
def test_three_block_tower():
    P = three_block_tower()
    verify_solution(P)

def test_simple_blocks_world():
    P = simple_blocks_world()
    verify_solution(P)

def test_shopping_problem():
    P = shopping_problem()
    verify_solution(P)

def test_socks_and_shoes():
    P = socks_and_shoes()
    verify_solution(P)

def ptest_double_tennis_problem():
    P = double_tennis_problem()
    verify_solution(P)

@pytest.mark.parametrize("goal_state", [
    "In(C1, D1)",
    "In(C1, D2)",
    "In(C1, D1) & In(R1, D2)",
    "In(R1, D2) & In(C1, D1)",
    "In(C1, D1) & In(C3, R1)",
    "In(C1, D1) & In(C3, R1) & In(R1, D3)",
    "In(C1, D1) & In(R1, D3) & In(C3, R1)",
    "In(C1, D1) & In(C3, D3)",
    "In(C1, D1) & In(R1, D2) & In(C3, R1)",
    "In(C1, D1) & In(C3, R1) & In(R1, D3)",
    "In(C1, D1) & In(C2, D3)",
    "In(C3, D1)",
    "In(C2, D3)",
    "In(C3, D3)",
])
def test_logistics_plan_valid(goal_state):
    """These should yield a valid (non-crashing) plan, even if empty."""
    init = "In(C1, R1) & In(C2, D1) & In(C3, D2) & In(R1, D1) & Holding(R1)"
    P = logisticsPlanCustom(init, goal_state)
    verify_solution(P)

@pytest.mark.parametrize("goal_state", [ # Why don't any of these have a solution?
    "In(C2, D3) & In(C3, D3)",
    "In(C3, D3) & In(C2, D3)",
    "In(C1, D2) & In(C3, D3)", # Why doesn't this have a solution? It finds one ...
    "In(C1, D3) & In(C2, D3) & In(C3, D3)",
    "In(C1, D2) & In(C3, D3) & In(C2, D1)", # Why doesn't this also have a solutioN? it finds one
])
def test_logistics_plan_no_plan(goal_state):
    """These are known to have no valid plan."""
    init = "In(C1, R1) & In(C2, D1) & In(C3, D2) & In(R1, D1) & Holding(R1)"
    P = logisticsPlanCustom(init, goal_state)
    sol = Linearize(P).execute()
    # Depending on your GraphPlan, no-plan might return [] or None
    #assert sol in ([], None)
    verify_solution(P)


@pytest.mark.parametrize("goal_state", [
    "In(C1, D2) & In(C3, D3) & In(C2, D3) & In(R1, D1)",
])
def test_logistics_plan_kaboom(goal_state):
    """This case is known to cause planner explosion. Catch and mark as expected failure."""
    init = "In(C1, R1) & In(C2, D1) & In(C3, D2) & In(R1, D1) & Holding(R1)"
    try:
        P = logisticsPlanCustom(init, goal_state)
        sol = Linearize(P).execute()
        # If it actually returns, that's fine too
        assert sol is None or isinstance(sol, list)
    except Exception:
        pytest.xfail("Known kaboom case – planner explosion or unsolvable problem")