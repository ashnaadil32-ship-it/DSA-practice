class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n = len(positions)
        # Create an array of indices from 0 to n-1 and sort them by their position
        indices = sorted(range(n), key=lambda i: positions[i])
        
        stack = []  # Stores indices of surviving 'R' moving robots
        
        for idx in indices:
            if directions[idx] == 'R':
                stack.append(idx)
            else:
                # Current robot is moving 'L', check for collisions with 'R' robots in stack
                while stack and healths[idx] > 0:
                    top_idx = stack[-1]
                    
                    if healths[top_idx] > healths[idx]:
                        # Stack robot survives, current 'L' robot is destroyed
                        healths[top_idx] -= 1
                        healths[idx] = 0
                    elif healths[top_idx] < healths[idx]:
                        # Current 'L' robot survives, stack robot is destroyed
                        healths[idx] -= 1
                        healths[top_idx] = 0
                        stack.pop()
                    else:
                        # Both robots have equal health and destroy each other
                        healths[idx] = 0
                        healths[top_idx] = 0
                        stack.pop()
                        
        # Return healths of all robots that survived (health > 0) in their original index order
        return [h for h in healths if h > 0]
        