class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        
        # Array to store the prefix products for the flattened grid
        prefix = [1]
        for row in grid:
            for num in row:
                prefix.append((prefix[-1] * num) % MOD)
        
        # Traverse in reverse to maintain and multiply the suffix product dynamic tracker
        suffix = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                # Index in the flattened prefix array matches (i * n + j)
                ans[i][j] = (prefix[i * n + j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD
                
        return ans