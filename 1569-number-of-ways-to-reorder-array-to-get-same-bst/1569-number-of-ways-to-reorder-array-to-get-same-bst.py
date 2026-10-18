from math import comb

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            ways = comb(len(arr) - 1, len(left))
            ways *= dfs(left)
            ways *= dfs(right)

            return ways % MOD

        return (dfs(nums) - 1) % MOD