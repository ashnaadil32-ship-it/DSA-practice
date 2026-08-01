from bisect import bisect_left
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        nums = []

        for x, y in points:
            if x == 0:
                nums.append(y)
            elif y == side:
                nums.append(side + x)
            elif x == side:
                nums.append(3 * side - y)
            else:
                nums.append(4 * side - x)

        nums.sort()
        n = len(nums)
        total = 4 * side

        def check(d):
            for start in nums:
                end = start + total - d
                cur = start
                ok = True

                for _ in range(k - 1):
                    idx = bisect_left(nums, cur + d)
                    if idx == n or nums[idx] > end:
                        ok = False
                        break
                    cur = nums[idx]

                if ok:
                    return True
            return False

        left, right = 1, side

        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left