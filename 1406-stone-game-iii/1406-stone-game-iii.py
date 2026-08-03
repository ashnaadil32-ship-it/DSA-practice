from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] represents the maximum score difference the current player 
        # can get starting from index i.
        dp = [0] * (n + 1)
        
        # Iterate backwards from the last stone to the first
        for i in range(n - 1, -1, -1):
            res = float('-inf')
            current_sum = 0
            
            # Try taking 1, 2, or 3 stones
            for k in range(i, min(i + 3, n)):
                current_sum += stoneValue[k]
                res = max(res, current_sum - dp[k + 1])
                
            dp[i] = res
            
        # dp[0] represents Alice's score advantage starting at index 0
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"