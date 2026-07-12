from functools import reduce
from operator import xor

class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        # Process each query sequentially
        for l, r, k, v in queries:
            # Generate stepping indices from l to r inclusive with step size k
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD
                
        # Return the cumulative bitwise XOR of all post-query elements
        return reduce(xor, nums)