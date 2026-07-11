class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # 1. Count trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            zeros = 0
            for val in reversed(row):
                if val == 0:
                    zeros += 1
                else:
                    break
            trailing_zeros.append(zeros)
            
        swaps = 0
        
        # 2. Greedy simulation to satisfy row requirements
        for i in range(n):
            required = n - 1 - i
            satisfied_idx = -1
            
            for j in range(i, n):
                if trailing_zeros[j] >= required:
                    satisfied_idx = j
                    break
            
            if satisfied_idx == -1:
                return -1
                
            swaps += satisfied_idx - i
            
            # Pop and insert to simulate swapping rows
            activated_row = trailing_zeros.pop(satisfied_idx)
            trailing_zeros.insert(i, activated_row)
            
        return swaps