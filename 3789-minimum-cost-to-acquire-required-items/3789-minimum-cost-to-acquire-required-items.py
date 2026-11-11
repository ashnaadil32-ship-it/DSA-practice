
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        only1 = cost1 * need1
        only2 = cost2 * need2

        both = costBoth * max(need1, need2)

        common = min(need1, need2)

        mixed = (common * costBoth +
                 (need1 - common) * cost1 +
                 (need2 - common) * cost2)

        return min(only1 + only2, both, mixed)
