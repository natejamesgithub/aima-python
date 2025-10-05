import re
from typing import List, Set, Any
from logic import expr, Expr


"""
PlanDebugger.run("logistics_trace1.txt", self.graph)
"""

def rund(graph):
    return PlanDebugger.run("logistics_trace1.txt", graph)


class PlanLevel:
    def __init__(self, current_state: Set[Any], actions: Set[Any], next_state: Set[Any]):
        self.current_state = current_state
        self.actions = actions
        self.next_state = next_state

    def __repr__(self):
        return (f"<PlanLevel>\n"
                f"  Current State: {self.current_state}\n"
                f"  Actions: {self.actions}\n"
                f"  Next State: {self.next_state}\n")

class PlanDebugger:
    """
    Utility to parse a plan trace from file and check it against a GraphPlan graph.
    """


    @staticmethod
    def parse_plan_file(filename: str) -> List[PlanLevel]:
        plan_levels = []
        current_level = None

        state_prefixes = ('In(', 'Holding(', 'NotHolding(') # , 'PIn(', 'PHolding('

        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                tokens = [expr(tok.strip()) for tok in line.split("&") if tok.strip()]

                # Heuristic: starts with state prefixes → state line
                if all(str(t).startswith(state_prefixes) for t in tokens):
                    # Start a new level
                    if current_level is not None:
                        # Assign previous level's next_state
                        current_level.next_state = set(tokens)
                        plan_levels.append(current_level)

                    current_level = PlanLevel(current_state=set(tokens), actions=set(), next_state=set())

                else:
                    # Action line → assign to current level
                    if current_level is None:
                        raise ValueError("File starts with actions before any state.")
                    current_level.actions = set(tokens)

        # Append the last level
        if current_level is not None:
            plan_levels.append(current_level)

        return plan_levels


    @staticmethod
    def check_plan_against_graph(plan_levels: List[PlanLevel], graph) -> str:
        
        for i, plan_level in enumerate(plan_levels):
            plan_states = plan_level.current_state
            plan_actions = plan_level.actions
            next_plan_states = plan_level.next_state

            level = graph.levels[i]
            print("# Levels: ", len(plan_levels))
            
            # --- State check ---
            graph_states = set(level.current_state)
            missing_states = plan_states - graph_states
            #print("PLAN_STATES: ", plan_states, "\nGRAPH_STATES: ", graph_states)
            if missing_states:
                return (f"❌ Divergence at LEVEL {i}: plan states not in graph level. "
                        f"Missing states: {missing_states}")

            # --- Action check ---
            if plan_actions:
                # Check applicability
                for act in plan_actions:
                    if act not in level.next_action_links:
                        print(f"At level {i}, {level}")
                        return f"❌ Divergence at LEVEL {i}: action {act} not applicable"

                # Check mutex
                if i == 7:
                    print(level.mutex)
                for a1 in plan_actions:
                    for a2 in plan_actions:
                        if a1 != a2 and {a1, a2} in level.mutex:
                            return f"❌ Divergence at LEVEL {i}: actions {a1} and {a2} are mutex"

                # Verify successor states
                successor_states = set()
                for act in plan_actions:
                    if act in level.next_action_links:
                        successor_states.update(level.next_action_links[act])
                missing_next_states = next_plan_states - successor_states
                if missing_next_states:
                    return (f"❌ Divergence at LEVEL {i}: next states don’t match action effects. "
                            f"Missing next states: {missing_next_states}")

            # --- State mutex check ---
            for s1 in plan_states:
                for s2 in plan_states:
                    if s1 != s2 and {s1, s2} in level.state_mutexes:
                        return f"❌ Divergence at LEVEL {i}: states {s1} and {s2} are mutex"

        return "✅ Plan is valid against the graph!"


    @staticmethod
    def run(filename: str, graph) -> str:
        """
        Convenience wrapper to parse a plan file and check it against a graph.
        """
        plan_levels = PlanDebugger.parse_plan_file(filename)
        print("Plan: ", plan_levels)
        result = PlanDebugger.check_plan_against_graph(plan_levels, graph)
        return result
    