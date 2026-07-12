class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # prefix_x[r][c] will store the count of 'X's in the submatrix from (0,0) to (r-1, c-1)
        # prefix_y[r][c] will store the count of 'Y's in the submatrix from (0,0) to (r-1, c-1)
        prefix_x = [[0] * (n + 1) for _ in range(m + 1)]
        prefix_y = [[0] * (n + 1) for _ in range(m + 1)]
        
        ans = 0
        
        for r in range(m):
            for c in range(n):
                # Calculate current character weights
                is_x = 1 if grid[r][c] == 'X' else 0
                is_y = 1 if grid[r][c] == 'Y' else 0
                
                # 2D prefix sum formula: current + top + left - top_left
                prefix_x[r + 1][c + 1] = is_x + prefix_x[r][c + 1] + prefix_x[r + 1][c] - prefix_x[r][c]
                prefix_y[r + 1][c + 1] = is_y + prefix_y[r][c + 1] + prefix_y[r + 1][c] - prefix_y[r][c]
                
                # Valid submatrix requires at least one 'X' and an equal number of 'X' and 'Y'
                if prefix_x[r + 1][c + 1] > 0 and prefix_x[r + 1][c + 1] == prefix_y[r + 1][c + 1]:
                    ans += 1
                    
        return ans