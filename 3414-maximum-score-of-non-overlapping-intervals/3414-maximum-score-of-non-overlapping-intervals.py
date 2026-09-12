class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = []
        for i, (start, end, weight) in enumerate(intervals):
            arr.append((start, end, weight, i))

        arr.sort(key=lambda x: x[1])

        # prev[i] = last interval that doesn't overlap with i
        prev = [0] * n

        for i in range(n):
            start = arr[i][0]

            left = 0
            right = i - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid][1] < start:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1

            prev[i] = ans

        # dp[i][k] = (maximum weight, selected indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n)]

        for i in range(n):
            for k in range(1, 5):

                # Don't take current interval
                if i > 0:
                    dp[i][k] = dp[i - 1][k]

                # Take current interval
                p = prev[i]

                if p == -1:
                    old_weight = 0
                    old_indices = []
                else:
                    old_weight, old_indices = dp[p][k - 1]

                new_weight = old_weight + arr[i][2]
                new_indices = old_indices + [arr[i][3]]

                if new_weight > dp[i][k][0]:
                    dp[i][k] = (new_weight, new_indices)

                elif new_weight == dp[i][k][0]:
                    if sorted(new_indices) < sorted(dp[i][k][1]):
                        dp[i][k] = (new_weight, new_indices)

        return sorted(dp[n - 1][4][1])