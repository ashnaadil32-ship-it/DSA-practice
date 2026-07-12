from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        index_map = defaultdict(list)
        min_span = float('inf')
        
        # Traverse the array sequentially
        for k, val in enumerate(nums):
            index_map[val].append(k)
            
            # If we have at least 3 occurrences of this value, calculate the span
            # The closest possible 'i' for our current 'k' is always index_map[val][-3]
            if len(index_map[val]) >= 3:
                i = index_map[val][-3]
                min_span = min(min_span, k - i)
                
        # If min_span remains unchanged, no valid triplet was found
        if min_span == float('inf'):
            return -1
            
        # Multiply the final minimal span by 2 to satisfy the simplified distance formula
        return 2 * min_span