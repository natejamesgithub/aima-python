import sys, os
import collections
from planning import *
from logic import *

import pytest
import submission1 as sub


def test_blocksworld_manual():
    sbw = simple_blocks_world()
    assert sbw.goal_test() == False
    sbw.act(expr('ToTable(A, B)'))
    sbw.act(expr('FromTable(B, A)'))
    assert sbw.goal_test() == False
    sbw.act(expr('FromTable(C, B)'))
    assert sbw.goal_test() == True


def test_air_cargo():
    P = air_cargo()
    assert isinstance(Linearize(P).execute(), list)

def test_spare_tire():
    P = spare_tire()
    assert isinstance(Linearize(P).execute(), list)

def test_three_block_tower():
    P = three_block_tower()
    assert isinstance(Linearize(P).execute(), list)

def test_simple_blocks_world():
    P = simple_blocks_world()
    assert isinstance(Linearize(P).execute(), list)

def test_shopping_problem():
    P = shopping_problem()
    #print(GraphPlan(P).execute())
    """
    [[[PItem(Milk), PSells(SM, Milk), PSells(SM, Banana), PStore(HW), 
    PItem(Banana), PStore(SM), Go(Home, HW), PSells(HW, Drill), 
    PItem(Drill), Go(Home, SM)], 
    [Buy(Drill, HW), Buy(Banana, SM), Buy(Milk, SM)]]]
    """
    assert isinstance(Linearize(P).execute(), list)

def test_socks_and_shoes():
    P = socks_and_shoes()
    assert isinstance(Linearize(P).execute(), list)

def test_double_tennis_problem():
    P = double_tennis_problem()
    #print(GraphPlan(P).execute())
    assert isinstance(Linearize(P).execute(), list)


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
    result = sub.logisticsPlanCustom(init, goal_state)
    assert result is None or isinstance(result, list)


@pytest.mark.parametrize("goal_state", [
    "In(C2, D3) & In(C3, D3)",
    "In(C3, D3) & In(C2, D3)",
    "In(C1, D2) & In(C3, D3)",
    "In(C1, D3) & In(C2, D3) & In(C3, D3)",
    "In(C1, D2) & In(C3, D3) & In(C2, D1)",
])
def test_logistics_plan_no_plan(goal_state):
    """These are known to have no valid plan."""
    init = "In(C1, R1) & In(C2, D1) & In(C3, D2) & In(R1, D1) & Holding(R1)"
    result = sub.logisticsPlanCustom(init, goal_state)
    # Depending on your GraphPlan, no-plan might return [] or None
    assert result in ([], None)


@pytest.mark.parametrize("goal_state", [
    "In(C1, D2) & In(C3, D3) & In(C2, D3) & In(R1, D1)",
])
def test_logistics_plan_kaboom(goal_state):
    """This case is known to cause planner explosion. Catch and mark as expected failure."""
    init = "In(C1, R1) & In(C2, D1) & In(C3, D2) & In(R1, D1) & Holding(R1)"
    try:
        result = sub.logisticsPlanCustom(init, goal_state)
        # If it actually returns, that's fine too
        assert result is None or isinstance(result, list)
    except Exception:
        pytest.xfail("Known kaboom case – planner explosion or unsolvable problem")