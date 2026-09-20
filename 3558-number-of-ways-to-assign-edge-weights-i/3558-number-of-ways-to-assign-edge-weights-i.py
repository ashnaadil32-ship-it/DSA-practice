class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [(1, 0, 0)]
        max_depth = 0

        while stack:
            node, parent, depth = stack.pop()
            max_depth = max(max_depth, depth)

            for nei in graph[node]:
                if nei != parent:
                    stack.append((nei, node, depth + 1))

        return pow(2, max_depth - 1, MOD)