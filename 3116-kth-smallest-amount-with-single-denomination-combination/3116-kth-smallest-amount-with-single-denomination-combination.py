import math
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        
        # Precompute all subset LCMs and their sign (+1 for odd sizes, -1 for even)
        subsets = []
        for r in range(1, n + 1):
            sign = 1 if r % 2 == 1 else -1
            for combo in combinations(coins, r):
                lcm_val = combo[0]
                for coin in combo[1:]:
                    lcm_val = (lcm_val * coin) // math.gcd(lcm_val, coin)
                subsets.append((lcm_val, sign))
                
        def count_valid(X: int) -> int:
            """Returns count of numbers <= X formed by combinations of coins."""
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (X // lcm_val)
            return total

        # Binary search bounds
        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_valid(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1   # Need a larger amount to reach k

        return ans