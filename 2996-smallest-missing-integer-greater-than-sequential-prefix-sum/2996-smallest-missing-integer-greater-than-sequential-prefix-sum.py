class Solution:
    def missingInteger(self, nums):
        s = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break
        
        x = s
        
        while x in nums:
            x += 1
        
        return x