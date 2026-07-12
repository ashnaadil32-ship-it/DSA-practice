class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        m = n * 2
        
        # Array to store the minimum distance for each position in the doubled array
        d = [m] * m
        
        # Step 1: Left-to-Right scan to find the closest identical element to the left
        left_seen = {}
        for i in range(m):
            val = nums[i % n]
            if val in left_seen:
                d[i] = min(d[i], i - left_seen[val])
            left_seen[val] = i
            
        # Step 2: Right-to-Left scan to find the closest identical element to the right
        right_seen = {}
        for i in range(m - 1, -1, -1):
            val = nums[i % n]
            if val in right_seen:
                d[i] = min(d[i], right_seen[val] - i)
            right_seen[val] = i
            
        # Step 3: Combine distances from both halves for the first n elements
        for i in range(n):
            d[i] = min(d[i], d[i + n])
            
        # Step 4: Answer each query in O(1) time
        ans = []
        for q in queries:
            # If the closest distance takes a full circle (>= n), no other equal element exists
            if d[q] >= n:
                ans.append(-1)
            else:
                ans.append(d[q])
                
        return ans     