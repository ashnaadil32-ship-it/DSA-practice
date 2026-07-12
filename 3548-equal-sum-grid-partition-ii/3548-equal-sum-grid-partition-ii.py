from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        total_sum = sum(sum(row) for row in grid)
        
        # Helper function to check horizontal partitions
        def check_horizontal(g: list[list[int]]) -> bool:
            m, n = len(g), len(g[0])
            
            top_freq = Counter()
            bottom_freq = Counter()
            
            # Populate the bottom frequency map initially with all elements
            for r in range(m):
                for c in range(n):
                    bottom_freq[g[r][c]] += 1
            
            top_sum = 0
            bottom_sum = total_sum
            
            # Try cuts between row i and row i + 1
            for i in range(m - 1):
                for j in range(n):
                    val = g[i][j]
                    top_sum += val
                    bottom_sum -= val
                    top_freq[val] += 1
                    bottom_freq[val] -= 1
                
                # Case 1: Perfectly equal parts without discounting any cell
                if top_sum == bottom_sum:
                    return True
                
                # Case 2: Top section is heavier, try to discount an element from top
                if top_sum > bottom_sum:
                    diff = top_sum - bottom_sum
                    if top_freq[diff] > 0:
                        # Connectivity check for top section:
                        # 1. 2D regions (rows > 1 and cols > 1) always stay connected when removing a cell.
                        # 2. 1D boundaries/strips remain connected if the cell is on one of the corners/ends.
                        if (i + 1 > 1 and n > 1) or (i == 0 and (g[0][0] == diff or g[0][n - 1] == diff)) or (n == 1 and (g[0][0] == diff or g[i][0] == diff)):
                            return True
                            
                # Case 3: Bottom section is heavier, try to discount an element from bottom
                else:
                    diff = bottom_sum - top_sum
                    if bottom_freq[diff] > 0:
                        # Connectivity check for bottom section
                        if (m - i - 1 > 1 and n > 1) or (i == m - 2 and (g[i + 1][0] == diff or g[i + 1][n - 1] == diff)) or (n == 1 and (g[i + 1][0] == diff or g[m - 1][0] == diff)):
                            return True
                            
            return False

        # Check horizontal cuts on the original grid
        if check_horizontal(grid):
            return True
            
        # Transpose the grid to test vertical cuts using the same logic
        transpose = [list(x) for x in zip(*grid)]
        return check_horizontal(transpose)