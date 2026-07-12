from collections import defaultdict
import math

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        # Group indices by their corresponding value
        index_map = defaultdict(list)
        for idx, val in enumerate(nums):
            index_map[val].append(idx)
            
        min_dist = math.inf
        
        # Check all value groups
        for indices in index_map.values():
            # A valid tuple requires at least 3 distinct indices
            if len(indices) >= 3:
                # To minimize, we look at consecutive triplets within the sorted index list
                for h in range(len(indices) - 2):
                    i = indices[h]
                    k = indices[h + 2]
                    # Distance formula simplifies to 2 * (k - i) when ordered
                    current_dist = 2 * (k - i)
                    min_dist = min(min_dist, current_dist)
                    
        return -1 if min_dist == math.inf else min_dist