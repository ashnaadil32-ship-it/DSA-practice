class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1_000_000_007
        
        # dp[i][j][0] -> stable arrays with i zeros, j ones, ending in 0
        # dp[i][j][1] -> stable arrays with i zeros, j ones, ending in 1
        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base Cases: Filling configurations where only one type of digit exists
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        # Fill the DP table
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                
                # --- Ending in 0 ---
                # Total configurations by adding 0 to previous states
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                # Subtract invalid streaks where consecutive 0s > limit
                if i - limit - 1 >= 0:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD
                elif i - limit - 1 == -1 and j == 0:
                    # Corner case handled by base cases, but keep safe under modulo subtraction
                    pass
                
                # --- Ending in 1 ---
                # Total configurations by adding 1 to previous states
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                # Subtract invalid streaks where consecutive 1s > limit
                if j - limit - 1 >= 0:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD
                    
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD