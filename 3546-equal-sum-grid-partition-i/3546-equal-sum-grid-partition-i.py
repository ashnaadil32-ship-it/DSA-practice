class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        # Calculate the total sum of all elements in the grid
        total_sum = sum(sum(row) for row in grid)
        
        # If the total sum is odd, it's impossible to partition into two equal halves
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        m, n = len(grid), len(grid[0])
        
        # 1. Check for a valid horizontal partition
        running_row_sum = 0
        for i in range(m - 1):  # m - 1 ensures the bottom partition is non-empty
            running_row_sum += sum(grid[i])
            if running_row_sum == target:
                return True
                
        # 2. Check for a valid vertical partition
        running_col_sum = 0
        for j in range(n - 1):  # n - 1 ensures the right partition is non-empty
            # Sum up elements of column j across all rows
            running_col_sum += sum(grid[i][j] for i in range(m))
            if running_col_sum == target:
                return True
                
        return False