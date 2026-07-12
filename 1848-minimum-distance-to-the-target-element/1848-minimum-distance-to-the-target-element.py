class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        min_dist = float('inf')
        
        # Iterate through the array tracking both index and value
        for i, num in enumerate(nums):
            if num == target:
                # Calculate the absolute distance to the start index
                current_dist = abs(i - start)
                # Keep track of the minimum distance found so far
                if current_dist < min_dist:
                    min_dist = current_dist
                    
        return min_dist       