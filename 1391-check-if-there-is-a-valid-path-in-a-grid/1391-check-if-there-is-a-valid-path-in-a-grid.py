from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        directions = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)]       # right, up
        }

        visited = set()

        def dfs(r, c):
            if (r, c) == (m - 1, n - 1):
                return True

            visited.add((r, c))

            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # Check if the neighbor connects back
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        if dfs(nr, nc):
                            return True

            return False

        return dfs(0, 0)