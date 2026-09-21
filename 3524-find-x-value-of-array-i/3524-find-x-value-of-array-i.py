class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k

        # dp[r] = number of subarrays ending at current index
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            rem = num % k
            new_dp = [0] * k

            # Start a new subarray with only num
            new_dp[rem] += 1

            # Extend previous subarrays
            for r in range(k):
                new_rem = (r * rem) % k
                new_dp[new_rem] += dp[r]

            # Add current subarrays to final answer
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans