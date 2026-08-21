from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for num in nums:
            current = max(rob1,rob2+num)

            rob2 = rob1
            rob1 = current

        return rob1   