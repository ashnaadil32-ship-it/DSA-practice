class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        rhombus_sums = set()
        
        # Iterate over all possible centers and sizes of a rhombus
        for r in range(m):
            for c in range(n):
                # A rhombus of size 0 is just a single cell
                rhombus_sums.add(grid[r][c])
                
                # Expand the rhombus size (radius)
                q = 1
                while r - q >= 0 and r + q < m and c - q >= 0 and c + q < n:
                    current_sum = 0
                    
                    # Top to Left, Top to Right, Bottom to Left, Bottom to Right borders
                    for i in range(q):
                        current_sum += grid[r - q + i][c - i]  # Top moving down-left
                        current_sum += grid[r + i][c - q + i]  # Left moving down-right
                        current_sum += grid[r + q - i][c + i]  # Bottom moving up-right
                        current_sum += grid[r - i][c + q - i]  # Right moving up-left
                        
                    rhombus_sums.add(current_sum)
                    q += 1
                    
        # Return the top 3 unique sums sorted in descending order
        return sorted(list(rhombus_sums), reverse=True)[:3]