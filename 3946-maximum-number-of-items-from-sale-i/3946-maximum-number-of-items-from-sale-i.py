
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        free = [0] * n
        cheapest = float('inf')

        # Count free items for each item
        for i in range(n):
            factor = items[i][0]
            cheapest = min(cheapest, items[i][1])

            for j in range(n):
                if i != j and items[j][0] % factor == 0:
                    free[i] += 1

        # 0/1 Knapsack DP
        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            gain = free[i] + 1

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + gain)

        # Spend remaining budget on cheapest items
        ans = 0

        for b in range(budget + 1):
            ans = max(ans, dp[b] + (budget - b) // cheapest)

        return ans
