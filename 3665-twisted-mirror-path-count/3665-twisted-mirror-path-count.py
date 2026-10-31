
from typing import List
from functools import lru_cache
import sys

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        sys.setrecursionlimit(10000)

        m, n = len(grid), len(grid[0])
        vornadexil = grid

        @lru_cache(None)
        def dfs(i, j, d):
            if i < 0 or j < 0:
                return 0

            if i == 0 and j == 0:
                return 1

            if vornadexil[i][j] == 0:
                return (dfs(i, j - 1, 0) +
                        dfs(i - 1, j, 1)) % MOD

            if d == 0:
                return dfs(i - 1, j, 1)

            return dfs(i, j - 1, 0)

        return dfs(m - 1, n - 1, 0)
