from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):
            arr = []

            top, left = layer, layer
            bottom, right = m - layer - 1, n - layer - 1

            # Top row
            for j in range(left, right + 1):
                arr.append(grid[top][j])

            # Right column
            for i in range(top + 1, bottom):
                arr.append(grid[i][right])

            # Bottom row
            for j in range(right, left - 1, -1):
                arr.append(grid[bottom][j])

            # Left column
            for i in range(bottom - 1, top, -1):
                arr.append(grid[i][left])

            k1 = k % len(arr)
            arr = arr[k1:] + arr[:k1]

            idx = 0

            # Top row
            for j in range(left, right + 1):
                grid[top][j] = arr[idx]
                idx += 1

            # Right column
            for i in range(top + 1, bottom):
                grid[i][right] = arr[idx]
                idx += 1

            # Bottom row
            for j in range(right, left - 1, -1):
                grid[bottom][j] = arr[idx]
                idx += 1

            # Left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = arr[idx]
                idx += 1

        return grid