import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        LOG = n.bit_length()
        mx = [nums[:]]
        mn = [nums[:]]

        j = 1
        while (1 << j) <= n:
            size = n - (1 << j) + 1
            prev = mx[-1]
            curr = [0] * size
            prev2 = mn[-1]
            curr2 = [0] * size

            half = 1 << (j - 1)
            for i in range(size):
                curr[i] = max(prev[i], prev[i + half])
                curr2[i] = min(prev2[i], prev2[i + half])

            mx.append(curr)
            mn.append(curr2)
            j += 1

        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1

        def value(l, r):
            p = log[r - l + 1]
            length = 1 << p
            maximum = max(mx[p][l], mx[p][r - length + 1])
            minimum = min(mn[p][l], mn[p][r - length + 1])
            return maximum - minimum

        heap = []

        for l in range(n):
            heapq.heappush(heap, (-value(l, n - 1), l, n - 1))

        ans = 0

        for _ in range(k):
            neg_val, l, r = heapq.heappop(heap)
            ans -= neg_val

            if r > l:
                heapq.heappush(
                    heap,
                    (-value(l, r - 1), l, r - 1)
                )

        return ans