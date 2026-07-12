from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        
        # Standard Union-Find 'find' function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        # Standard Union-Find 'union' function
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        # Step 1: Build connected components from allowed swaps
        for u, v in allowedSwaps:
            union(u, v)
            
        # Step 2: Map each component root to a frequency counter of its source values
        component_counts = defaultdict(Counter)
        for i in range(n):
            root = find(i)
            component_counts[root][source[i]] += 1
            
        # Step 3: Check targets against component inventory
        mismatches = 0
        for i in range(n):
            root = find(i)
            target_val = target[i]
            
            # If the value is available in the component, consume it
            if component_counts[root][target_val] > 0:
                component_counts[root][target_val] -= 1
            else:
                mismatches += 1
                
        return mismatches        