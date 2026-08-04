class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        min_val, max_val = min(nums), max(nums)
        nums_set = set(nums)
        
        # Find all numbers within the range that are missing from the set
        missing_elements = [x for x in range(min_val, max_val + 1) if x not in nums_set]
        
        
        return missing_elements