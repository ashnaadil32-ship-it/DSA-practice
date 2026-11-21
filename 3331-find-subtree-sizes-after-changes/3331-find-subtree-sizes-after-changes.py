class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        def dfs(u):
            ch = s[u]
            old = last.get(ch)

            if old is not None:
                new_parent[u] = old

            last[ch] = u

            for v in children[u]:
                dfs(v)

            if old is None:
                last.pop(ch)
            else:
                last[ch] = old

        dfs(0)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [1] * n

        def calculate(u):
            for v in new_children[u]:
                ans[u] += calculate(v)
            return ans[u]

        calculate(0)
        return ans