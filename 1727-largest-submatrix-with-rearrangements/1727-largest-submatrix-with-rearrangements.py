class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        # Track the heights of consecutive 1s for each column
        heights = [0] * n
        
        for r in range(m):
            for c in range(n):
                # If matrix[r][c] is 1, increment height; otherwise reset to 0
                if matrix[r][c] == 1:
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            # Create a sorted copy of the current row's column heights in descending order
            sorted_heights = sorted(heights, reverse=True)
            
            # Calculate the maximum rectangle area possible at this row
            for i in range(n):
                base = i + 1
                height = sorted_heights[i]
                max_area = max(max_area, base * height)
                
        return max_area