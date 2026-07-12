class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        # Flip the k x k submatrix vertically by swapping rows equidistant from the center
        for i in range(x, x + k // 2):
            # Calculate the mirror row index from the bottom of the submatrix
            i2 = x + k - 1 - (i - x)
            
            # Swap elements inside the submatrix across columns y to y + k - 1
            for j in range(y, y + k):
                grid[i][j], grid[i2][j] = grid[i2][j], grid[i][j]
                
        return grid