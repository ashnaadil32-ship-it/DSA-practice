from collections import deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build the graph adjacency list
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 1: Find all suspicious methods starting from k using BFS
        suspicious = {k}
        q = deque([k])
        
        while q:
            curr = q.popleft()
            for neighbor in graph[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    q.append(neighbor)
                    
        # Step 2: Check if any non-suspicious method invokes a suspicious method
        for u in range(n):
            if u not in suspicious:
                for v in graph[u]:
                    if v in suspicious:
                        # External dependency found; cannot remove any methods
                        return list(range(n))
                        
        # Step 3: Collect and return all remaining (non-suspicious) methods
        return [i for i in range(n) if i not in suspicious]