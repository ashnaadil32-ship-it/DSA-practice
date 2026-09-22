class Node:
    def __init__(self, k):
        self.prod = 1
        self.cnt = [0] * k


class SegmentTree:
    def __init__(self, nums, k):
        self.k = k
        self.n = len(nums)
        self.tree = [None] * (4 * self.n)
        self.build(1, 0, self.n - 1, nums)

    def merge(self, left, right):
        k = self.k

        node = Node(k)

        # Product of the whole combined segment
        node.prod = (left.prod * right.prod) % k

        # Prefixes completely inside left
        for r in range(k):
            node.cnt[r] = left.cnt[r]

        # Prefixes that use all of left + part of right
        for r in range(k):
            new_r = (left.prod * r) % k
            node.cnt[new_r] += right.cnt[r]

        return node

    def build(self, idx, l, r, nums):
        if l == r:
            node = Node(self.k)

            value = nums[l] % self.k
            node.prod = value
            node.cnt[value] = 1

            self.tree[idx] = node
            return

        mid = (l + r) // 2

        self.build(idx * 2, l, mid, nums)
        self.build(idx * 2 + 1, mid + 1, r, nums)

        self.tree[idx] = self.merge(
            self.tree[idx * 2],
            self.tree[idx * 2 + 1]
        )

    def update(self, idx, l, r, pos, value):
        if l == r:
            node = Node(self.k)

            value %= self.k
            node.prod = value
            node.cnt[value] = 1

            self.tree[idx] = node
            return

        mid = (l + r) // 2

        if pos <= mid:
            self.update(idx * 2, l, mid, pos, value)
        else:
            self.update(idx * 2 + 1, mid + 1, r, pos, value)

        self.tree[idx] = self.merge(
            self.tree[idx * 2],
            self.tree[idx * 2 + 1]
        )

    def query(self, idx, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree[idx]

        mid = (l + r) // 2

        if qr <= mid:
            return self.query(idx * 2, l, mid, ql, qr)

        if ql > mid:
            return self.query(idx * 2 + 1, mid + 1, r, ql, qr)

        left = self.query(idx * 2, l, mid, ql, qr)
        right = self.query(idx * 2 + 1, mid + 1, r, ql, qr)

        return self.merge(left, right)


class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        tree = SegmentTree(nums, k)

        ans = []

        for index, value, start, x in queries:

            # 1. Update nums[index]
            tree.update(1, 0, n - 1, index, value)

            # 2. Query [start, n-1]
            node = tree.query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            # Number of prefixes having product % k == x
            ans.append(node.cnt[x])

        return ans