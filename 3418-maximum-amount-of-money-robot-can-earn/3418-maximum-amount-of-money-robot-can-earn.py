class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # Initialize a 3D DP table with negative infinity
        # Dimensions: (m + 1) x (n + 1) x 3
        # The extra row and column handle the boundary conditions gracefully.
        dp = [[[-float('inf')] * 3 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # Base case: At the destination cell, any extra moves out of bounds yield 0
        # This allows the boundary logic to correctly evaluate the bottom-right cell.
        for k in range(3):
            dp[m - 1][n][k] = 0
            dp[m][n - 1][k] = 0
            
        # Iterate backwards from the bottom-right corner to the top-left
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                for k in range(3):
                    # Option 1: Take the cell value normally
                    # The robot can go down (r + 1) or right (c + 1)
                    best_next = max(dp[r + 1][c][k], dp[r][c + 1][k])
                    no_neutralize = coins[r][c] + best_next
                    
                    # Option 2: Neutralize if it's a robber and we have neutralizations left
                    neutralize = -float('inf')
                    if coins[r][c] < 0 and k > 0:
                        best_next_k = max(dp[r + 1][c][k - 1], dp[r][c + 1][k - 1])
                        neutralize = 0 + best_next_k
                        
                    dp[r][c][k] = max(no_neutralize, neutralize)
                    
        # The answer is at the starting cell (0, 0) with all 2 neutralizations intact
        return dp[0][0][2]