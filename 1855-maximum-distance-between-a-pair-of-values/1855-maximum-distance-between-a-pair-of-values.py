class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        max_dist = 0
        
        # Traverse both arrays using a two-pointer approach
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                # If valid, calculate distance and try to expand j further right
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                # If invalid, increment i to find a smaller value in nums1
                i += 1
                
        return max_dist