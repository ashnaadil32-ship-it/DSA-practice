class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        # In-place 2D prefix sum calculation
        for r in range(m):
            for c in range(n):
                if r > 0:
                    grid[r][c] += grid[r - 1][c]
                if c > 0:
                    grid[r][c] += grid[r][c - 1]
                if r > 0 and c > 0:
                    grid[r][c] -= grid[r - 1][c - 1]
                
                # Check if the submatrix from (0,0) to (r,c) has a sum <= k
                if grid[r][c] <= k:
                    count += 1
                else:
                    # Since grid values are non-negative, if the sum exceeds k, 
                    # expanding further right in this row will also exceed k.
                    break
                    
        return count