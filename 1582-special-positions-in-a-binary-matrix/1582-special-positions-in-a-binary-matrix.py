class Solution:
    def numSpecial(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Precompute the total number of 1s in each row and column
        row_counts = [0] * rows
        col_counts = [0] * cols
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
                    
        special_count = 0
        
        # Check every element to see if it qualifies as "special"
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # It must be the absolute only 1 in its row and column
                    if row_counts[r] == 1 and col_counts[c] == 1:
                        special_count += 1
                        
        return special_count