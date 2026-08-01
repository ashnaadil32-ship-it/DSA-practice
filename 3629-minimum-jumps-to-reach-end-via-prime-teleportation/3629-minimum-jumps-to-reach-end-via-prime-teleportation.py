from collections import defaultdict, deque
from typing import List

MX = 10 ** 6 + 1

factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]:
        for j in range(i, MX, i):
            factors[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        graph = defaultdict(list)
        for i, x in enumerate(nums):
            for p in factors[x]:
                graph[p].append(i)

        vis = [False] * n
        vis[0] = True

        q = deque([(0, 0)])

        while q:
            i, dist = q.popleft()

            if i == n - 1:
                return dist

            # Adjacent moves
            if i > 0 and not vis[i - 1]:
                vis[i - 1] = True
                q.append((i - 1, dist + 1))

            if i + 1 < n and not vis[i + 1]:
                vis[i + 1] = True
                q.append((i + 1, dist + 1))

            # Prime teleportation
            if nums[i] in graph:
                for nxt in graph[nums[i]]:
                    if not vis[nxt]:
                        vis[nxt] = True
                        q.append((nxt, dist + 1))
                del graph[nums[i]]