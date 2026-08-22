class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        best_buy = prices[0]

        for i in range(1,len(prices)):
            if prices[i] <= best_buy:
                best_buy = min(best_buy,prices[i])

            if prices[i] > maxprofit:
                maxprofit = max(maxprofit,prices[i] - best_buy)

        return maxprofit
      