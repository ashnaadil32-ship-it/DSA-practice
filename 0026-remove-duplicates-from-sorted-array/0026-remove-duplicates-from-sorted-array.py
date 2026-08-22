class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 1
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
               nums[k] = nums[j]
               k += 1
           
        return k      