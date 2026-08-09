from functools import cache
from itertools import accumulate
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # Prefix sum array to quickly calculate the sum of remaining piles in O(1)
        s = list(accumulate(piles, initial=0))
        
        @cache
        def dfs(i: int, m: int) -> int:
            # If we can take all remaining piles, take them all
            if 2 * m >= n - i:
                return s[n] - s[i]
            
            # Otherwise, try all possible choices for X (1 <= X <= 2M)
            # and minimize what is left for the opponent to maximize our score.
            return max(
                s[n] - s[i] - dfs(i + x, max(m, x))
                for x in range(1, 2 * m + 1)
            )
            
        return dfs(0, 1)