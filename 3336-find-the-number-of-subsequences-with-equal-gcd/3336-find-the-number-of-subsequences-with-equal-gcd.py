import math
from functools import lru_cache

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        @lru_cache(None)
        def dp(idx, gcd1, gcd2):
            # Base case: if we've processed all elements
            if idx == n:
                # Both subsequences must be non-empty (gcd > 0) and have equal GCDs
                return 1 if gcd1 == gcd2 and gcd1 > 0 else 0
            
            # Choice 1: Skip the current number entirely
            res = dp(idx + 1, gcd1, gcd2)
            
            # Choice 2: Add nums[idx] to the first subsequence
            new_gcd1 = nums[idx] if gcd1 == 0 else math.gcd(gcd1, nums[idx])
            res = (res + dp(idx + 1, new_gcd1, gcd2)) % MOD
            
            # Choice 3: Add nums[idx] to the second subsequence
            new_gcd2 = nums[idx] if gcd2 == 0 else math.gcd(gcd2, nums[idx])
            res = (res + dp(idx + 1, gcd1, new_gcd2)) % MOD
            
            return res
        
        # Start the recursion from index 0 with empty subsequences (gcd = 0)
        return dp(0, 0, 0)