class Solution:
    def largestInteger(self, nums, k):
        count = {}

        # Count frequency of every number in all windows of size k
        for i in range(len(nums) - k + 1):
            window = set(nums[i:i + k])

            for num in window:
                count[num] = count.get(num, 0) + 1

        # Almost missing = appears in exactly one window
        ans = -1

        for num in count:
            if count[num] == 1:
                ans = max(ans, num)

        return ans