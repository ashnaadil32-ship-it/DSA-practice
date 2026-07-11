from collections import deque
from sortedcontainers import SortedSet

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        # Segment states by parity to optimize boundaries checking
        ts = [SortedSet() for _ in range(2)]
        for i in range(n + 1):
            ts[i % 2].add(i)
            
        cnt0 = s.count('0')
        ts[cnt0 % 2].remove(cnt0)
        
        q = deque([cnt0])
        ans = 0
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == 0:
                    return ans
                
                # Minimum and maximum zero boundaries after flipping k elements
                l = cur + k - 2 * min(cur, k)
                r = cur + k - 2 * max(k - n + cur, 0)
                
                # Fetch target parity group
                t = ts[l % 2]
                
                # Find the first element >= l
                idx = t.bisect_left(l)
                while idx < len(t) and t[idx] <= r:
                    val = t[idx]
                    q.append(val)
                    t.remove(val)
                    # No need to increment idx because we removed the current element
                    
            ans += 1
            
        return -1