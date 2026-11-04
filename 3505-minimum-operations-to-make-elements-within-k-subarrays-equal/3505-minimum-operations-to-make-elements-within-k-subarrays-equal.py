
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)

        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            step >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}

        count = Fenwick(m)
        sums = Fenwick(m)

        def update(v, delta):
            r = rank[v]
            count.add(r, delta)
            sums.add(r, v * delta)

        def get_cost():
            mid_rank = count.kth((x + 1) // 2)
            med = vals[mid_rank - 1]

            left_count = count.query(mid_rank)
            left_sum = sums.query(mid_rank)

            total_sum = sums.query(m)
            right_count = x - left_count
            right_sum = total_sum - left_sum

            return (
                med * left_count - left_sum
                + right_sum - med * right_count
            )

        costs = []

        for i in range(x):
            update(nums[i], 1)

        costs.append(get_cost())

        for i in range(x, n):
            update(nums[i - x], -1)
            update(nums[i], 1)
            costs.append(get_cost())

        INF = 10**18

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
