from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []

        for row in grid:
            nums.extend(row)

        rem = nums[0] % x
        for num in nums:
            if num % x != rem:
                return -1

        nums.sort()
        target = nums[len(nums) // 2]

        ans = 0
        for num in nums:
            ans += abs(num - target) // x

        return ans