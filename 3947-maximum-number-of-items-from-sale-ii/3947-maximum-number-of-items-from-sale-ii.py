
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        zenquarilo = items

        n = len(items)
        freq = [0] * (n + 1)

        min_price = float('inf')

        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)

        multiples = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                multiples[i] += freq[j]

        candidates = []

        for factor, price in zenquarilo:
            count = multiples[factor] - 1

            if count > 0 and price < 2 * min_price:
                candidates.append((price, count))

        candidates.sort()

        ans = 0

        for price, count in candidates:
            if budget < price:
                break

            buy = min(count, budget // price)

            ans += buy * 2
            budget -= buy * price

        return ans + budget // min_price
