from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        LOG = n.bit_length()

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        up = [[0] * (n + 1) for _ in range(LOG)]

        stack = [(1, 0)]

        while stack:
            u, p = stack.pop()
            up[0][u] = p

            for v in graph[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u))

        for j in range(1, LOG):
            for v in range(1, n + 1):
                up[j][v] = up[j - 1][up[j - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return up[0][u]

        ans = []

        for u, v in queries:
            d = depth[u] + depth[v] - 2 * depth[lca(u, v)]

            if d == 0:
                ans.append(0)
            else:
                ans.append(pow(2, d - 1, MOD))

        return ans