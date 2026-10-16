
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, left, right):
            if lazy[node]:
                mid = (left + right) // 2
                for child, length in (
                    (node * 2, mid - left + 1),
                    (node * 2 + 1, right - mid)
                ):
                    d = lazy[node]
                    tree_sq[child] = (
                        tree_sq[child]
                        + 2 * d * tree_sum[child]
                        + length * d * d
                    ) % MOD
                    tree_sum[child] = (
                        tree_sum[child] + length * d
                    ) % MOD
                    lazy[child] += d
                lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                d = 1
                length = right - left + 1
                tree_sq[node] = (
                    tree_sq[node]
                    + 2 * tree_sum[node]
                    + length
                ) % MOD
                tree_sum[node] = (tree_sum[node] + length) % MOD
                lazy[node] += 1
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD
            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i)
            ans = (ans + tree_sq[1]) % MOD
            last[x] = i

        return ans
