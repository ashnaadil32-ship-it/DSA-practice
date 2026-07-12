class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Define directions in clockwise order: North, East, South, West
        # North: (0, 1), East: (1, 0), South: (0, -1), West: (-1, 0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Start facing North (index 0) at origin (0, 0)
        dir_idx = 0
        x, y = 0, 0
        
        # Convert obstacles to a hash set for O(1) coordinate lookups
        obstacle_set = {tuple(obs) for obs in obstacles}
        
        max_dist_sq = 0
        
        for cmd in commands:
            if cmd == -1:
                # Turn right 90 degrees
                dir_idx = (dir_idx + 1) % 4
            elif cmd == -2:
                # Turn left 90 degrees
                dir_idx = (dir_idx - 1) % 4
            else:
                # Move forward cmd steps
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    next_x = x + dx
                    next_y = y + dy
                    
                    # If the next position hits an obstacle, stop moving along this command
                    if (next_x, next_y) in obstacle_set:
                        break
                        
                    x, y = next_x, next_y
                    # Calculate and update the maximum Euclidean distance squared
                    max_dist_sq = max(max_dist_sq, x * x + y * y)
                    
        return max_dist_sq