class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        best_buy = prices[0]

        for price in prices:
           if price <= best_buy:
              best_buy = min(best_buy, price)

           if price > best_buy:
              maxprofit = max(maxprofit, price - best_buy)

        return maxprofit         