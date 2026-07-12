class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        # Helper function to reverse an integer mathematically
        def reverse_num(x: int) -> int:
            rev = 0
            while x > 0:
                rev = rev * 10 + (x % 10)
                x //= 10
            return rev

        # Map to store: key = reverse(nums[i]), value = latest index i
        seen_reversed = {}
        min_dist = float('inf')

        for i, val in enumerate(nums):
            # Check if any prior index is waiting for this specific value
            if val in seen_reversed:
                min_dist = min(min_dist, i - seen_reversed[val])
            
            # Precompute what a future right endpoint would need to match this element
            rev_val = reverse_num(val)
            # Store the latest index to guarantee the minimum absolute distance
            seen_reversed[rev_val] = i

        return -1 if min_dist == float('inf') else min_dist