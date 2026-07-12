class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        
        # dp_max[r][c] and dp_min[r][c] store the max and min products to reach (r, c)
        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]
        
        # Base case: top-left corner
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        
        # Initialize the first row (can only come from the left)
        for c in range(1, n):
            dp_max[0][c] = dp_min[0][c] = dp_max[0][c - 1] * grid[0][c]
            
        # Initialize the first column (can only come from above)
        for r in range(1, m):
            dp_max[r][0] = dp_min[r][0] = dp_max[r - 1][0] * grid[r][0]
            
        # Fill the rest of the DP tables
        for r in range(1, m):
            for c in range(1, n):
                val = grid[r][c]
                if val >= 0:
                    dp_max[r][c] = max(dp_max[r - 1][c], dp_max[r][c - 1]) * val
                    dp_min[r][c] = min(dp_min[r - 1][c], dp_min[r][c - 1]) * val
                else:
                    dp_max[r][c] = min(dp_min[r - 1][c], dp_min[r][c - 1]) * val
                    dp_min[r][c] = max(dp_max[r - 1][c], dp_max[r][c - 1]) * val
                    
        max_product = dp_max[m - 1][n - 1]
        
        # If the maximum product is negative, it's impossible to get a non-negative path
        return max_product % MOD if max_product >= 0 else -1      