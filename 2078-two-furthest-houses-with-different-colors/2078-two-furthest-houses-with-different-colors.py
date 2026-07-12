class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        max_dist = 0
        
        # Scenario 1: Check distances from the first house (index 0)
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                max_dist = max(max_dist, j)
                break
                
        # Scenario 2: Check distances from the last house (index n - 1)
        for i in range(n):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, (n - 1) - i)
                break
                
        return max_dist