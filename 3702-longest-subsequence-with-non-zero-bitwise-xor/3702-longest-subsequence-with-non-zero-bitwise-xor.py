from typing import List
from functools import reduce

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # If all elements are 0, no non-zero XOR subsequence can be formed
        if not any(nums):
            return 0
        
        # Calculate the total XOR sum of the array
        total_xor = reduce(lambda acc, x: acc ^ x, nums, 0)
        
        # If total XOR is 0, we drop one non-zero element to make it non-zero (length - 1)
        # Otherwise, we can keep all elements (length)
        return len(nums) - (1 if total_xor == 0 else 0)