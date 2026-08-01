from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0] * (2 * limit + 2)
        n = len(nums)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b)
            high = max(a, b)
            s = a + b

            diff[2] += 2
            diff[low + 1] -= 1
            diff[s] -= 1
            diff[s + 1] += 1
            diff[high + limit + 1] += 1

        ans = float("inf")
        cur = 0

        for target in range(2, 2 * limit + 1):
            cur += diff[target]
            ans = min(ans, cur)

        return ans