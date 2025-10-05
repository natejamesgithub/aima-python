
class Linearize:

    def __init__(self, planning_problem):
        self.planning_problem = planning_problem

    def filter(self, solution):
        """Filter out persistence actions from a solution"""

        new_solution = []
        for section in solution[0]:
            new_section = []
            for operation in section:
                if not (operation.op[0] == 'P' and operation.op[1].isupper()):
                    new_section.append(operation)
            new_solution.append(new_section)
        return new_solution

    def orderlevel(self, level, planning_problem):
        """Return valid linear order of actions for a given level"""

        for permutation in itertools.permutations(level):
            print(f"TRYING PARTIAL PLAN: {permutation}")  ## Bill's hack                
            temp = copy.deepcopy(planning_problem)
            count = 0
            ## print(f"PERMUTATION: {permutation}")  ## Bill's hack
            for action in permutation:
                try:
                    # print(f"TRY ACTION: {action}")  ## Bill's hack
                    temp.act(action)
                    count += 1
                    # print(f"TRY ACTION: {action} SUCCESS!")  ## Bill's hack
                except:
                    # print(f"TRY ACTION: {action} FAIL!")  ## Bill's hack
                    count = 0
                    temp = copy.deepcopy(planning_problem)
                    continue     ##break
            if count == len(permutation):
                print(f"\nSUCCESSFUL PARTIAL PLAN ORDERING: {permutation}")  ## Bill's hack
                return list(permutation), temp
        print(f"NO SUCCESSFUL PARTIAL PLAN: {level}")  ## Bill's hack                
        return None, planning_problem  ## added planning_problem... its gotta return a planning problem and start over if it fails, but maybe this is saying return fail and the unsolved planning problem

    def execute(self):
        """Finds total-order solution for a planning graph"""

        graphPlan_solution = GraphPlan(self.planning_problem).execute()

        ## Bill's stuff from playing around
        ## print(f"UNFILTERED PLAN: {graphPlan_solution}")  ## Bill's hack
        ## pnl(graphPlan_solution)
        ## for possible_plan in graphPlan_solution:
        ##    possible_plan = [possible_plan]
        ##    filtered_possible_plan = self.filter(possible_plan)
        ##    print(f"POSSIBLE PLAN: {filtered_possible_plan}")  ## Bill's hack
        ## flattened_graphplan = self.filter(graphPlan_solution)
        ## flattened_graphplan = sum(graphPlan_solution, [])  ## Bill's hack
        ## flattened_graphplan = sum(flattened_graphplan, [])  ## Bill's hack
        ##  flattened_graphplan = [flattened_graphplan]
        ## graphPlan_solution = [flattened_graphplan]  ## Bill's hack
        ##  pnl(flattened_graphplan)

        ## I think I have to go over all permutations of possbile partial graphplans
        
        for possible_plan in itertools.permutations(graphPlan_solution):   ## Bill's hack

            ## possible_plan = [possible_plan]  ## Bill's hack, stuff below expect a list with one element which is also a list
            ## filtered_solution = self.filter(graphPlan_solution)   # original

            filtered_solution = self.filter(possible_plan)   # my mod

            print(f"TRYING FILTERED PLAN: {filtered_solution}")  ## Bill's hack
                        
            ## filtered_solution = self.filter(possible_plan)  # mod
            ## print(f"\nFILTERED PLAN: {filtered_solution}")  ## Bill's hack
            ## pnl(filtered_solution)
            ## filtered_solution = possible_plan
            
            ordered_solution = []
            planning_problem = self.planning_problem
            for level in filtered_solution:

                ## print(f"TRYING SOLUTION LEVEL: {level}")  ## Bill's hack

                ## the below is a key line, the key line
                level_solution, planning_problem = self.orderlevel(level, planning_problem)  ## actions get applied
                if not level_solution:  # This checks if level_solution is None or an empty list
                    print(f"PLAN FAIL: {filtered_solution}")  ## Bill's hack
                    continue   ## Bill's hack!!  if empty, continue looking.  

                print(f"LEVEL SOLUTION: {level_solution}")  ## Bill's hack
                ##print(f"CURRENT STATE: {planning_problem.initial}\n")  ## Bill's hack                
                ## for action in level_solution:
                ##    print(f"APPLY ACTION: {action}")  ## Bill's hack                    
                ##    planning_problem.act(action)           # complete guess, apply action to the problem and keep going

                ## I think we need to apply the plan to the planning problem and modify it
                for element in level_solution:   
                    ordered_solution.append(element)

            if not ordered_solution:
                continue  ## no plan possible from the partial plan at the level
            else:
                print(f"WORKING SOL'N: {ordered_solution}")  ## Bill's hack
                break
            
        return ordered_solution

