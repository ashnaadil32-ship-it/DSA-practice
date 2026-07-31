from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1: max money from two houses ago
        # rob2: max money from the previous house
        rob1, rob2 = 0, 0
        
        for n in nums:
            # At each house, choose the max between:
            # 1. Skipping current house (rob2)
            # 2. Robbing current house and adding to rob1 (n + rob1)
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2