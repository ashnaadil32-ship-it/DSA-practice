from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)

        for i, num in enumerate(nums):
            pos[num].append(i)

        ans = [0] * len(nums)

        for indices in pos.values():
            m = len(indices)

            prefix = [0] * (m + 1)
            for i in range(m):
                prefix[i + 1] = prefix[i] + indices[i]

            for i in range(m):
                idx = indices[i]

                left = idx * i - prefix[i]
                right = (prefix[m] - prefix[i + 1]) - idx * (m - i - 1)

                ans[idx] = left + right

        return ans