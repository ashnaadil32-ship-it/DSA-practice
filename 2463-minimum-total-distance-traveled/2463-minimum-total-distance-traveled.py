from functools import cache
import math

class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        # Sort both elements to ensure non-crossing optimal assignments
        robot.sort()
        factory.sort(key=lambda x: x[0])
        
        num_robots = len(robot)
        num_factories = len(factory)
        
        @cache
        def dfs(i: int, j: int) -> int:
            # Base Case 1: All robots have been successfully assigned
            if i == num_robots:
                return 0
            # Base Case 2: Out of factories but robots remain unassigned
            if j == num_factories:
                return math.inf
            
            # Option 1: Skip the current factory completely
            min_dist = dfs(i, j + 1)
            
            cumulative_dist = 0
            limit = factory[j][1]
            factory_pos = factory[j][0]
            
            # Option 2: Assign k robots to the current factory j
            for k in range(1, limit + 1):
                # If adding more robots exceeds the total available robots, stop
                if i + k - 1 >= num_robots:
                    break
                
                # Add the distance of the current robot to factory j
                cumulative_dist += abs(robot[i + k - 1] - factory_pos)
                
                # Calculate the cost of this sub-problem choice
                remaining_cost = dfs(i + k, j + 1)
                
                if remaining_cost != math.inf:
                    min_dist = min(min_dist, cumulative_dist + remaining_cost)
                    
            return min_dist
            
        return dfs(0, 0)