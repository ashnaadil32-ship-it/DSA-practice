class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Precompute minimum changes for every substring
        cost = [[INF] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for r in range(d):
                        l, h = i + r, j - ((length - 1 - r) % d)

                        while l < h:
                            if s[l] != s[h]:
                                changes += 1
                            l += d
                            h -= d

                    cost[i][j] = min(cost[i][j], changes)

        # DP: dp[i][parts] = minimum changes
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for parts in range(1, k + 1):
                for j in range(i - 1):
                    if i - j >= 2:
                        dp[i][parts] = min(
                            dp[i][parts],
                            dp[j][parts - 1] + cost[j][i - 1]
                        )

        return dp[n][k]